# SkillSpector Security Scan

NVIDIA SkillSpector v2.11.2 run against the agent-skill repositories in this index.
`OpenSenseNova/SenseNova-Skills`, added later, was reviewed by reading and running its code instead; see [Manual review: SenseNova-Skills API key routing](#manual-review-sensenova-skills-api-key-routing) at the end.

## Scope and method

29 of the 115 repositories in this index are installable agent skills or skill packs, as opposed to applications that merely ship a `SKILL.md` for their own contributors.
Scope was determined by listing every repository tree through the GitHub API and keeping those whose purpose is to be installed into an agent, not those that happen to contain a skill file.
That check found 73 repositories containing `SKILL.md` or a plugin manifest, but most are product repositories such as PostHog, Ghost and Penpot, which are not things you would install as a skill.

Every target was scanned with static analysis (`--no-llm`), which runs 71 vulnerability patterns across 17 categories plus YARA signatures and taint tracking.
A subset was then re-scanned with the semantic LLM pass enabled through the local Claude CLI session, which needs no API key.

## Headline: do not read the raw verdict

SkillSpector returned `DO_NOT_INSTALL` for 23 of the 29 scans, and a maximum risk score of 100 for 22 of them.

That verdict list includes `anthropics/claude-plugins-community`, which is Anthropic's own marketplace where every plugin has already passed automated security scanning and human review.
It also includes `openai/skills` and `openai/plugins`, OpenAI's official catalogue and plugin examples for Codex, the latter carrying 9 CRITICAL findings.
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
| `openai/plugins` | `YR1` CRITICAL x6, "Credential exfiltration webhook" | Official Zoom and Twilio integration docs, matched because `process.env.`, `fetch(` and `ngrok.io` appear on the same page |
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
| `openai/plugins` | 100 | 9 | 96 | 5244 | 0.02 | 0.0% | below |
| `K-Dense-AI/scientific-agent-skills` | 100 | 0 | 6 | 2421 | 0.002 | 0.8% | below |
| `jakubkrehel/make-interfaces-feel-better` | 20 | 0 | 0 | 13 | 0.00 | 100% | **SAFE** |
| `millwright-labs/minto-pyramid-skill` | 25 | 0 | 0 | 12 | 0.00 | 91.7% | below |
| `heygen-com/hyperframes` | 24 | 0 | 0 | 4 | 0.00 | 100% | incomplete clone, disregard |

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

Raw JSON reports for all 29 scans are in `data/skillspector/`, and the calibrated table is in `data/scan-results.csv`.

## Manual review: SenseNova-Skills API key routing

`OpenSenseNova/SenseNova-Skills` joined the index on 2026-10-28 and has not been through SkillSpector.
Its code was read by hand at upstream commit `0ee34f3` and then run with dummy keys instead, and that review found one issue to deal with before installing it.

### Unset base URLs fall back to SenseNova

The skills are written for SenseNova's own API, but `sn-image-base` can also drive Gemini, OpenAI and Anthropic models.
Each call takes a key and a base URL from environment variables, and when no base URL is set it uses SenseNova's mainland-China endpoint instead of failing.

| Call | Key (first one set wins) | Base URL (first one set wins) | Built-in fallback |
|---|---|---|---|
| Image generation and editing | `SN_IMAGE_GEN_API_KEY`, `SN_API_KEY` | `SN_IMAGE_GEN_BASE_URL`, `SN_BASE_URL` | `https://token.sensenova.cn/v1` |
| Text (`sn-text-optimize`) | `SN_TEXT_API_KEY`, `SN_CHAT_API_KEY`, `SN_API_KEY` | `SN_TEXT_BASE_URL`, `SN_CHAT_BASE_URL`, `SN_BASE_URL` | `https://token.sensenova.cn/v1` |
| Vision (`sn-image-recognize`) | `SN_VISION_API_KEY`, `SN_CHAT_API_KEY`, `SN_API_KEY` | `SN_VISION_BASE_URL`, `SN_CHAT_BASE_URL`, `SN_BASE_URL` | `https://token.sensenova.cn/v1` |
| `sn-da-image-caption` | `SN_VISION_API_KEY`, `SN_CHAT_API_KEY`, `SN_API_KEY` | `SN_VISION_BASE_URL`, `SN_CHAT_BASE_URL`, `SN_BASE_URL` | `https://token.sensenova.cn/v1` |

The fallbacks are hard-coded in `skills/sn-image-base/scripts/sn_image_base/configs.py` at lines 99 and 109, and in `skills/sn-da-image-caption/scripts/caption.py` at line 48.
Command-line flags such as `--base-url` take precedence when passed, but `sn-infographic` tells the agent not to pass them, so in practice the environment decides.
A Gemini key set as `SN_IMAGE_GEN_API_KEY` without `SN_IMAGE_GEN_BASE_URL`, or an OpenAI or Anthropic key set as `SN_CHAT_API_KEY` without `SN_CHAT_BASE_URL`, is therefore sent to SenseNova in the request headers.
The image base URL is marked `required=True`, but that check never fires because the built-in default means the value is never empty.
`sn-infographic`, `sn-image-imitate` and `sn-image-resume` all run through `sn-image-base`, so they inherit the same behaviour.
`sn-ppt-tools` has no built-in endpoint and fails instead, so it is not affected.

### Safe configuration

Four rules make these skills safe to run on your own keys.

1. **Set a tripwire base URL.**
   Set `SN_BASE_URL` to a host that can never resolve, such as `https://sn-base-url-not-set.invalid/v1`.
   Every lookup in the table checks `SN_BASE_URL` before the built-in fallback, so a call you forgot to configure fails with a DNS error naming that host instead of reaching SenseNova.
   The `.invalid` top-level domain is reserved by RFC 2606 and never resolves.
2. **Give every call you use its own key and base URL, and leave `SN_API_KEY` unset.**
   `SN_API_KEY` feeds every call at once, which is how a key meant for one provider ends up at another.
3. **Use dedicated, spend-capped keys.**
   Create separate keys for these skills instead of reusing your main ones, so a mistake costs one revocation.
4. **Pin the reviewed commit and do not use `sn-update`.**
   `sn-update` hard-resets to upstream `main` on every run, so a new built-in endpoint would arrive without notice.
   After any manual update, run `grep -rnE 'https?://[a-z0-9.-]*sensenova' --include='*.py' --include='*.js' --include='*.mjs' --include='*.sh' skills/` in the clone.
   At `0ee34f3` it prints the three fallbacks above plus one documentation example in `generation/sensenova.py`, so anything beyond that needs reading before you trust the update.

The example below runs image generation on Gemini and the prompt rewriting and vision review on Claude.
The endpoints, model types and Gemini model come from `skills/sn-image-base/README.md`, and the Claude model is the current Sonnet.

```bash
# Tripwire: any call without its own base URL fails here instead of reaching SenseNova
export SN_BASE_URL="https://sn-base-url-not-set.invalid/v1"

# Image generation on Gemini
export SN_IMAGE_GEN_MODEL_TYPE="nano-banana"
export SN_IMAGE_GEN_BASE_URL="https://generativelanguage.googleapis.com"
export SN_IMAGE_GEN_MODEL="gemini-3.1-flash-image-preview"
export SN_IMAGE_GEN_API_KEY="<dedicated Gemini key>"

# Prompt rewriting and vision review on Claude
export SN_CHAT_TYPE="anthropic-messages"
export SN_CHAT_BASE_URL="https://api.anthropic.com/v1"
export SN_CHAT_MODEL="claude-sonnet-5-5"
export SN_CHAT_API_KEY="<dedicated Anthropic key>"
```

For OpenAI instead, use `SN_IMAGE_GEN_MODEL_TYPE="openai-image"` with `SN_IMAGE_GEN_BASE_URL="https://api.openai.com/v1"`, or `SN_CHAT_TYPE="openai-completions"` with `SN_CHAT_BASE_URL="https://api.openai.com/v1"`.
If you never use SenseNova, blocking `token.sensenova.cn` and `token.sensenova.ai` in a firewall or `/etc/hosts` adds a last line of defence; an `HTTPS_PROXY` filter does not, because the image client ignores proxy settings.

### The workbench servers can pick up your Anthropic key

`sn-ppt-workbench` and `sn-deep-research` each start a local web server from `workbench-runtime/dist-server/index.mjs`, a minified bundle of about 1.9 MB whose source is not in the repository.
When no workbench-specific key is set, that server falls back to `ANTHROPIC_API_KEY` from the environment for its agent bridge, so starting it from a shell that exports your main Anthropic key hands that key over.
Where the bridge sends it could not be traced through the minified code, so start the workbench only from an environment without your main keys.

### How this was checked

The fallbacks were found by reading the code at commit `0ee34f3` and confirmed on 2026-10-28 by running the real scripts with dummy keys in a clean environment.
Text, vision and `sn-da-image-caption` requests went through a local proxy that recorded the destination host and refused the connection.
Image requests ignored the proxy, so their destination comes from the error each one returned, except in the last setup, where the tripwire pointed at the recorder itself and the request was seen arriving.

| Setup | Image generation | Text, vision and `sn-da-image-caption` |
|---|---|---|
| Keys set, no base URLs | `token.sensenova.cn`, whose live server answered HTTP 404 | `token.sensenova.cn` |
| The safe configuration above | `generativelanguage.googleapis.com` | `api.anthropic.com` |
| The same without `SN_CHAT_BASE_URL` | `generativelanguage.googleapis.com` | `sn-base-url-not-set.invalid`, the tripwire |
| The same without `SN_IMAGE_GEN_BASE_URL`, tripwire set to the local recorder | The tripwire, with the Gemini key in `x-goog-api-key` | `api.anthropic.com` |

The image client ignores proxy settings because `utils/httpx_client.py` passes its own transport to `httpx.AsyncClient`, which switches off httpx's `HTTPS_PROXY` handling despite the comment there saying otherwise.
That is why SenseNova's live server received the request carrying the dummy Gemini key in the first setup, which is direct proof of the leak.
The last setup used a local address as the tripwire so the misdirected request could be observed; with the recommended `.invalid` value the same request fails at the DNS lookup instead.
Together, the last two setups show the tripwire catching a forgotten base URL for every call, including the image call that carries the Gemini key.

### Re-running the check

`tools/sensenova_route_test.py` re-runs the four setups and checks each result against the table above, so it also works as a check after an upstream update.
It runs SenseNova's code, so read the checkout first.
In setups A to C the image request still reaches the real host carrying the dummy Gemini key, while `--setups D` stays on your machine.

```bash
D=$(mktemp -d)

# Only the skills folder at the reviewed commit, about 15 MB instead of 146 MB
git clone --quiet --filter=blob:none --no-checkout https://github.com/OpenSenseNova/SenseNova-Skills.git "$D/sensenova"
git -C "$D/sensenova" sparse-checkout set skills
git -C "$D/sensenova" checkout --quiet 0ee34f37b969011d527eba348d1bec220fd1a7dd

# The libraries the skills import, at the versions behind the table
uv venv --quiet --python 3.12 "$D/venv"
uv pip install --quiet --python "$D/venv/bin/python" httpx==0.28.1 openai==3.40.0 pillow==13.0.0 python-dotenv==1.2.4 typing-extensions==4.16.0

python3 tools/sensenova_route_test.py --skills "$D/sensenova/skills" --python "$D/venv/bin/python"
```

To check a newer upstream commit, check that one out instead of `0ee34f3`.
All 16 checks passing means the table still holds; any FAIL means this section needs revisiting.
