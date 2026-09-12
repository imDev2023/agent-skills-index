# SkillSpector Security Scan

NVIDIA SkillSpector v2.11.2 run against the agent-skill repositories in this index.

## Scope and method

29 of the 115 repositories in this index are installable agent skills or skill packs, as opposed to applications that merely ship a `SKILL.md` for their own contributors.
Scope was determined by listing every repository tree through the GitHub API and keeping those whose purpose is to be installed into an agent, not those that happen to contain a skill file.
That check found 73 repositories containing `SKILL.md` or a plugin manifest, but most are product repositories such as PostHog, Ghost and Penpot, which are not things you would install as a skill.

Every target was scanned with static analysis (`--no-llm`), which runs 71 vulnerability patterns across 17 categories plus YARA signatures and taint tracking.
A subset was then re-scanned with the semantic LLM pass enabled through the local Claude CLI session, which needs no API key.

## Headline: do not read the raw verdict

SkillSpector returned `DO_NOT_INSTALL` for 22 of 28 completed scans, and a maximum risk score of 100 for 21 of them.

That verdict list includes `anthropics/claude-plugins-community`, which is Anthropic's own marketplace where every plugin has already passed automated security scanning and human review.
It also includes `openai/skills`, OpenAI's official catalogue for Codex.
When a scanner flags both vendors' own reviewed repositories as "do not install", the raw verdict is not a usable install gate.

Two things drive this.
The risk score saturates: any repository with enough files accumulates enough pattern hits to reach 100, so score stops discriminating above a low threshold.
And the static patterns match text literally, with no notion of whether the match is an instruction, an example, documentation, or binary noise.

### Verified false positives

Each of these was opened and read, not assumed.

| Repository | Finding | What it actually is |
|---|---|---|
| `anthropics/claude-plugins-community` | `YR4` HIGH, "MCP tool metadata poisoning" | The literal strings `tools:` and `"description":` inside `marketplace.json` |
| `anthropics/claude-plugins-community` | `SC9` HIGH x20, "Concealed executable artifact" | Ordinary CI shell scripts under `.github/actions/` |
| `anthropics/claude-plugins-community` | `TM2` HIGH, "Tool chaining abuse" | The substring `; rm -` in a CI script |
| `openai/skills` | `YR2` HIGH, "Python webshell" | A secure-coding guide's own "Insecure patterns" section, which documents the anti-pattern |
| `freestylefly/awesome-gpt-image-2` | `YR2` CRITICAL, "Known PHP webshell (WSO)" | The three bytes `Wso` occurring inside `data/images/case333.png` |
| `blader/humanizer` | `AR2` HIGH, "Anti-refusal statement" | The phrase "without warning" inside an example sentence demonstrating em dash removal |
| `daymade/claude-code-skills` | `TT3` CRITICAL, "Credential exfiltration" | An IMA API key read from the environment and sent as an auth header to `ima.qq.com`, its own API |
| `affaan-m/ECC` | `AST8` CRITICAL, "exec() wrapping compile" | Test code in `tests/test_taste_transport.py` compiling a validator AST |
| `mukul975/Anthropic-Cybersecurity-Skills` | `YR1` CRITICAL x40, "C2 framework indicators" | MITRE technique names such as `powershell-empire` listed in `ATTACK_COVERAGE.md` |
| `zhaoxuya520/reverse-skill` | `PE3` HIGH x472, "Credential access" | Largely the bare word `keychain` appearing in config and documentation |
| `virgiliojr94/book-to-skill` | `AE1` HIGH x3, "analysis-evasion" | Not evasion: the explanation text reads "Referenced artifact was not completely inspected", a coverage limitation reported as a HIGH finding |

## Calibrated results

A fairer signal is findings per file, measured against Anthropic's reviewed marketplace as the noise floor.
That baseline is **0.60 HIGH-or-CRITICAL findings per file**.
Anything at or below it is statistically indistinguishable from a repository that has already passed human security review.

Exactly one repository exceeds the baseline.

| Repository | Score | C | H | Files | HIGH+/file | Coverage | vs baseline |
|---|---|---|---|---|---|---|---|
| `zhaoxuya520/reverse-skill` | 100 | 60 | 1046 | 596 | **1.86** | 0.0% | **ABOVE** |
| `anthropics/claude-plugins-community` *(baseline)* | 100 | 0 | 73 | 122 | 0.60 | 90.2% | baseline |
| `witt3rd/oh-my-hermes` | 100 | 0 | 61 | 121 | 0.50 | 99.2% | below |
| `mukul975/Anthropic-Cybersecurity-Skills` | 100 | 77 | 517 | 1274 | 0.47 | 0.0% | below |
| `ayghri/i-have-adhd` | 100 | 0 | 26 | 62 | 0.42 | 100% | below |
| `cathrynlavery/diagram-design` | 100 | 0 | 107 | 426 | 0.25 | 97.4% | below |
| `Graphify-Labs/graphify` | 100 | 0 | 200 | 880 | 0.23 | 0.0% | below |
| `humanlayer/skills` | 100 | 0 | 8 | 36 | 0.22 | 94.4% | below |
| `mksglu/context-mode` | 100 | 0 | 124 | 587 | 0.21 | 0.0% | below |
| `DietrichGebert/ponytail` | 100 | 0 | 32 | 156 | 0.21 | 92.9% | below |
| `openai/skills` | 100 | 0 | 154 | 750 | 0.21 | 0.0% | below |
| `aerovato/magic-compact` | 100 | 0 | 13 | 65 | 0.20 | 78.5% | below |
| `blader/humanizer` | 47 | 0 | 2 | 10 | 0.20 | 100% | below |
| `addyosmani/agent-skills` | 100 | 0 | 39 | 198 | 0.20 | 95.5% | below |
| `virgiliojr94/book-to-skill` | 100 | 0 | 18 | 103 | 0.18 | 98.1% | below |
| `JetBrains/go-modern-guidelines` | 64 | 0 | 6 | 36 | 0.17 | 100% | below |
| `daymade/claude-code-skills` | 100 | 1 | 146 | 1047 | 0.14 | 0.0% | below |
| `affaan-m/ECC` | 100 | 1 | 332 | 3656 | 0.09 | 0.0% | below |
| `mattpocock/skills` | 100 | 0 | 14 | 165 | 0.09 | 98.2% | below |
| `harryvondiesel-web/5-persona-advisory-board` | 44 | 0 | 1 | 14 | 0.07 | 100% | below |
| `RiyaParikh0112/vibe-coding-playbook` | 29 | 0 | 1 | 17 | 0.06 | 100% | below |
| `JuliusBrussee/caveman` | 100 | 0 | 67 | 1326 | 0.05 | 0.0% | below |
| `tt-a1i/archify` | 100 | 0 | 19 | 592 | 0.03 | 17.7% | below |
| `freestylefly/awesome-gpt-image-2` | 100 | 1 | 1 | 461 | 0.004 | 12.1% | below |
| `K-Dense-AI/scientific-agent-skills` | 100 | 0 | 6 | 2421 | 0.002 | 0.8% | below |
| `jakubkrehel/make-interfaces-feel-better` | 20 | 0 | 0 | 13 | 0.00 | 100% | **SAFE** |
| `millwright-labs/minto-pyramid-skill` | 25 | 0 | 0 | 12 | 0.00 | 91.7% | below |
| `heygen-com/hyperframes` | 24 | 0 | 0 | 4 | 0.00 | 100% | incomplete clone, disregard |

`openai/plugins` did not finish within the session and is not included.

## What is actually worth acting on

Nothing in this set looks like a backdoored or malicious skill.
Five things are still worth knowing before you install.

**1. `zhaoxuya520/reverse-skill` is the one genuine outlier.**
At 1.86 HIGH-per-file it sits three times above the reviewed baseline, with 60 CRITICAL findings.
Most individual matches are nominal, but the repository really is a reverse-engineering and penetration-testing toolkit that bootstraps offensive tooling on demand.
That is its stated purpose rather than a defect, and it is the one item here that should be a deliberate, isolated install rather than a casual one.

**2. `blader/humanizer` rewrites your files in place with no confirmation and no backup.**
This came from the semantic pass, not the static one, and it is the single most practically useful finding in the whole run.
The skill's file mode writes only the final text back to the path you give it, offers the summary after the write, and never warns that the original is gone.
Since the skill deletes sentences and whole closing paragraphs by design, run it only on files that are committed to git first.

**3. Unpinned installers are universal, not a differentiator.**
26 of 28 repositories carry `npx`/`uvx` install instructions without a version pin, which SkillSpector flags as rug-pull exposure: 904 instances in `affaan-m/ECC`, 329 in `openai/skills`, 28 even in Anthropic's own marketplace.
This is an ecosystem-wide norm, so it tells you nothing about any single repository, but it does mean that pinning versions is on you.

**4. `daymade/claude-code-skills` reads browser cookies.**
Its `youtube-downloader` skill uses yt-dlp's `--cookies-from-browser` path to get past YouTube gating.
That is a documented feature rather than anything covert, but it is real browser-credential access and worth knowing about before installing that specific skill.

**5. `mukul975/Anthropic-Cybersecurity-Skills` scores 77 CRITICAL purely for describing attacks.**
Its findings are MITRE technique names in documentation.
It sits below the baseline once normalised, and the score reflects its subject matter, not its behaviour.

## Limitations

These results are weaker than the numbers suggest, and the caveats matter.

Coverage was partial on every large repository.
Nine of the biggest reported 0% fully-inspected files, and `K-Dense-AI/scientific-agent-skills` reached 0.8%, because the analyzers degrade once they hit an internal findings ceiling.
Findings that were reported are real matches, but absence of findings in those repositories is not evidence of safety.

Six repositories exceeded SkillSpector's 100 MiB ingest cap or failed to clone remotely and had to be shallow-cloned and scanned as local directories.
`heygen-com/hyperframes` cloned incompletely, reaching only 3 skill files, so its clean result is meaningless and it is effectively unscanned.

The semantic pass raises scores rather than lowering them.
On `blader/humanizer` it went from 47/MEDIUM to 56/HIGH by adding findings.
It does not retract the static false positives, so enabling the LLM will not clean up the noise; it adds a separate and more useful layer on top of it.

## Reproducing this

```bash
uv tool install git+https://github.com/NVIDIA/skillspector.git

# static scan of a repo
skillspector scan https://github.com/owner/repo --no-llm -f json -o report.json

# semantic scan using the local Claude CLI session, no API key needed
SKILLSPECTOR_PROVIDER=claude_cli skillspector scan https://github.com/owner/repo

# large repos exceed the 100 MiB ingest cap; clone shallow and scan the directory
git clone --depth 1 https://github.com/owner/repo /tmp/repo
skillspector scan /tmp/repo --no-llm
```

Raw JSON reports for all 28 completed scans are in `data/skillspector/`, and the calibrated table is in `data/scan-results.csv`.
