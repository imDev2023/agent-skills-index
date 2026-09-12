# Agent Skills and Tools Index

A sorted, categorised and deduplicated index of 115 GitHub repositories, built from a flat list of saved links.
Every entry carries a short description of what the repository is and a note on how to use it.

Metadata (stars, language, licence, last push) was pulled from the GitHub API on 2026-09-12 and is a point-in-time snapshot.

The 29 repositories here that are installable agent skills were scanned with NVIDIA SkillSpector.
See [SECURITY-SCAN.md](SECURITY-SCAN.md) for the results, including why the scanner's raw `DO_NOT_INSTALL` verdict should not be taken at face value.

## Contents

- [Agent Skills & Skill Packs](#agent-skills--skill-packs) (11)
- [Agent Behaviour & Output Quality](#agent-behaviour--output-quality) (8)
- [Context & Token Optimization](#context--token-optimization) (8)
- [Agent Memory & Knowledge Graphs](#agent-memory--knowledge-graphs) (5)
- [Coding Agents & Harnesses](#coding-agents--harnesses) (12)
- [LLM Gateways & Model Routing](#llm-gateways--model-routing) (3)
- [Local Inference & Models](#local-inference--models) (5)
- [Web Data, Scraping & Browser Automation](#web-data-scraping--browser-automation) (7)
- [Diagrams, Docs & Writing](#diagrams-docs--writing) (7)
- [Video, Image & Audio](#video-image--audio) (9)
- [Security, OSINT & Privacy](#security-osint--privacy) (9)
- [Self-Hosted Apps & OSS Alternatives](#self-hosted-apps--oss-alternatives) (15)
- [Developer Tools & Desktop](#developer-tools--desktop) (6)
- [Finance & Business](#finance--business) (3)
- [Awesome Lists, Learning & Career](#awesome-lists-learning--career) (7)

---

## Agent Skills & Skill Packs

Collections you install wholesale, plus the marketplaces they come from.

### [mattpocock/skills](https://github.com/mattpocock/skills)

`★ 259.9k` · `Shell` · `MIT` · last push 2026-09-04

Matt Pocock's personal `.agents` directory published as a skill pack: TDD, debugging, code review, domain modelling, merge conflicts.
**Use it for:** Clone into `~/.claude/skills/` or add as a plugin marketplace; you already have several of these loaded as `mattpocock-skills:*`.

### [affaan-m/ECC](https://github.com/affaan-m/ECC)

`★ 256.6k` · `JavaScript` · `MIT` · last push 2026-09-12

An opinionated agent-harness optimisation system bundling skills, "instincts", memory, security and research-first workflow rules across Claude Code, Codex, OpenCode and Cursor.
**Use it for:** Install as a harness layer over your existing setup; treat it as a reference for how to structure your own global rules.

### [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)

`★ 93.6k` · `JavaScript` · `MIT` · last push 2026-09-12

Production-grade engineering skills for AI coding agents from Addy Osmani, oriented at web performance, accessibility and code quality.
**Use it for:** Install the skills you want into `~/.claude/skills/`, then invoke them by name when working on frontend code.

### [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)

`★ 44.5k` · `Python` · `MIT` · last push 2026-09-12

165 validated science skills plus 100+ scientific databases covering biology, chemistry, medicine and drug discovery.
**Use it for:** Install the domain packs you need; useful if you ever want an agent to do literature or dataset work rather than code.

### [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill)

`★ 30.1k` · `Python` · `MIT` · last push 2026-09-12

Converts a technical book PDF into a structured Claude Code skill you can reference while working.
**Use it for:** Point it at a PDF you own and it emits a `SKILL.md` plus reference files; good for turning standards documents into agent-usable context.

### [openai/skills](https://github.com/openai/skills)

`★ 26.9k` · `Python` · `No licence` · last push 2026-09-08

The official skills catalogue for OpenAI Codex, portable to any agent that reads the open Agent Skills format.
**Use it for:** Browse `skills/` and copy individual `SKILL.md` folders into your own agent's skills directory.

### [openai/plugins](https://github.com/openai/plugins)

`★ 6.5k` · `JavaScript` · `No licence` · last push 2026-09-11

Curated Codex plugin examples, each with a `.codex-plugin/plugin.json` manifest plus optional skills, agents, commands, hooks and MCP config.
**Use it for:** Use it as the reference template when authoring your own plugin; the Figma and design-system examples are the richest.

### [anthropics/claude-plugins-community](https://github.com/anthropics/claude-plugins-community)

`★ 3.8k` · `Python` · `Apache-2.0` · last push 2026-08-25

Read-only mirror of the community plugin marketplace for Claude Code and Claude Cowork, synced nightly after security review.
**Use it for:** Add it as a marketplace with `/plugin marketplace add anthropics/claude-plugins-community`, then install plugins from the directory.

### [humanlayer/skills](https://github.com/humanlayer/skills)

`★ 3.8k` · `TypeScript` · `MIT` · last push 2026-08-13

Small, sharp Claude Code skills from HumanLayer: `improve-claude-md`, `narrow-react-prop-types`, iterative build loops.
**Use it for:** Install per-skill with `npx skills add humanlayer/skills --skill <name>`, then run the matching slash command.

### [daymade/claude-code-skills](https://github.com/daymade/claude-code-skills)

`★ 1.4k` · `Python` · `MIT` · last push 2026-09-12

A Claude Code skills marketplace; your saved link points specifically at its `pdf-creator` skill for generating PDFs from agent output.
**Use it for:** Add the repo as a plugin marketplace, or copy `daymade-docs/pdf-creator` straight into `~/.claude/skills/`.

### [witt3rd/oh-my-hermes](https://github.com/witt3rd/oh-my-hermes)

`★ 321` · `Python` · `MIT` · last push 2026-08-05

Multi-agent orchestration skills for the Hermes agent runtime, rebuilt from the oh-my-claudecode ideas on Hermes primitives.
**Use it for:** Only relevant if you run Hermes; otherwise read it for the orchestration patterns.

---

## Agent Behaviour & Output Quality

Single-purpose skills that change how the agent thinks or writes rather than what it can reach.

### [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)

`★ 135.9k` · `JavaScript` · `MIT` · last push 2026-09-07

Makes the agent behave like a YAGNI-minded senior dev so it stops over-engineering and writing code you did not ask for.
**Use it for:** Install as a skill or plugin; pairs well with your "prefer simplicity and long-term maintainability" rule.

### [blader/humanizer](https://github.com/blader/humanizer)

`★ 47k` · `Python` · `MIT` · last push 2026-09-06

Strips the tells of AI-generated prose (em dashes, "delve", tricolon padding) out of text.
**Use it for:** Run it over drafts before publishing; note it targets exactly the em-dash habit you already ban globally.

### [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)

`★ 42.2k` · `Python` · `MIT` · last push 2026-09-10

Forces the agent to lead with the answer instead of burying it under preamble, with ADHD-friendly short output.
**Use it for:** Install as a skill and enable it when you want terse, answer-first responses.

### [jakubkrehel/make-interfaces-feel-better](https://github.com/jakubkrehel/make-interfaces-feel-better)

`★ 3.4k` · `Markdown` · `MIT` · last push 2026-08-29

A skill that teaches the agent micro-interaction and polish heuristics so generated UI feels considered rather than default.
**Use it for:** Load it before frontend work; complements your pixel-perfection standard for E2E UI review.

### [JetBrains/go-modern-guidelines](https://github.com/JetBrains/go-modern-guidelines)

`★ 3.4k` · `Go` · `Apache-2.0` · last push 2026-09-10

JetBrains' guidelines that push AI agents to write modern idiomatic Go rather than dated patterns.
**Use it for:** Drop into a Go project's agent rules so generated Go uses current stdlib and error-handling idioms.

### [RiyaParikh0112/vibe-coding-playbook](https://github.com/RiyaParikh0112/vibe-coding-playbook)

`★ 371` · `n/a` · `No licence` · last push 2025-09-23

A methodology and prompt-framework toolkit for keeping AI-assisted development disciplined rather than ad hoc.
**Use it for:** Read it as process guidance; lift the prompting framework into your own CLAUDE.md if any of it fits.

### [harryvondiesel-web/5-persona-advisory-board](https://github.com/harryvondiesel-web/5-persona-advisory-board)

`★ 113` · `n/a` · `MIT` · last push 2026-07-28

Stress-tests a high-leverage decision through five strategic lenses and returns one clear next action.
**Use it for:** Invoke before launches, pricing changes or pivots; it is a decision skill, not a coding one.

### [millwright-labs/minto-pyramid-skill](https://github.com/millwright-labs/minto-pyramid-skill)

`★ 71` · `n/a` · `MIT` · last push 2026-08-16

Makes the agent write in Barbara Minto's Pyramid Principle: answer first, then grouped reasons, then evidence.
**Use it for:** Use for reports, proposals and decision memos rather than code.

---

## Context & Token Optimization

Tools that shrink what reaches the model, ordered roughly from broadest to most specific.

### [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)

`★ 105.1k` · `Go` · `Custom licence` · last push 2026-09-11

A skill that cuts roughly 65% of tokens by making the agent communicate in compressed "caveman" phrasing.
**Use it for:** Enable on long sessions where context pressure matters more than readable narration.

### [rtk-ai/rtk](https://github.com/rtk-ai/rtk)

`★ 80k` · `Rust` · `Apache-2.0` · last push 2026-09-11

A single-binary Rust CLI proxy that wraps common dev commands and cuts their LLM token consumption by 60-90%.
**Use it for:** Put it in front of noisy commands (builds, test runs, greps) so the agent sees a compact summary rather than raw output.

### [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)

`★ 71.6k` · `Python` · `Apache-2.0` · last push 2026-09-12

Compresses tool output, logs, files and RAG chunks before they reach the model; ships as a library, proxy and MCP server.
**Use it for:** Run the MCP server or proxy to cut 60-95% of tokens on JSON-heavy tool results without changing your agent.

### [mksglu/context-mode](https://github.com/mksglu/context-mode)

`★ 22.2k` · `TypeScript` · `Custom licence` · last push 2026-09-11

Sandboxes tool output for ~98% reduction, persists session memory and enforces routing rules across 17 agent platforms via MCP plus hooks.
**Use it for:** Install as MCP plus hooks; the strongest option here if you want one system rather than several point tools.

### [teamchong/pxpipe](https://github.com/teamchong/pxpipe)

`★ 7.4k` · `TypeScript` · `MIT` · last push 2026-09-11

Renders text context as images so Claude Code consumes it through the vision path at lower token cost.
**Use it for:** Pipe large text blobs through it; a genuinely unusual trick worth benchmarking before trusting.

### [ooples/token-optimizer-mcp](https://github.com/ooples/token-optimizer-mcp)

`★ 519` · `JavaScript` · `MIT` · last push 2026-09-11

Measures per-agent token savings, optimises context and shares a local knowledge graph across 16 CLI clients.
**Use it for:** Attach as an MCP server when you want hard numbers on what your context changes actually save.

### [jia-gao/leanctx](https://github.com/jia-gao/leanctx)

`★ 326` · `Python` · `MIT` · last push 2026-08-22

Drop-in prompt compression for production LLM apps using LLMLingua-2, claiming 40-60% token reduction with no code changes.
**Use it for:** Wrap your prompts with the Python SDK in app code rather than in the agent harness.

### [aerovato/magic-compact](https://github.com/aerovato/magic-compact)

`★ 167` · `TypeScript` · `BSD-3-Clause` · last push 2026-08-24

Lossless context compression plugin for Claude Code and OpenCode, aimed at surviving auto-compact without losing detail.
**Use it for:** Install as a plugin if you routinely hit compaction mid-task.

---

## Agent Memory & Knowledge Graphs

Persistent, queryable context that survives beyond one session.

### [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)

`★ 117k` · `Python` · `Apache-2.0` · last push 2026-09-10

Turns a codebase plus its docs, SQL schemas, configs and PDFs into a queryable knowledge graph using deterministic AST parsing, no vector store.
**Use it for:** You already have this installed as the `/graphify` skill; run it to index a repo before deep architectural work.

### [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)

`★ 43k` · `C` · `MIT` · last push 2026-09-12

High-performance MCP server that indexes a codebase into a persistent knowledge graph across 158 languages with sub-millisecond queries.
**Use it for:** Add as an MCP server for fast symbol and dependency lookups instead of repeated greps.

### [volcengine/OpenViking](https://github.com/volcengine/OpenViking)

`★ 36.7k` · `Python` · `AGPL-3.0` · last push 2026-09-11

A self-evolving context database that unifies agent memory, knowledge RAG and skills behind one store.
**Use it for:** Run it as the shared memory backend if you want several agents drawing on the same evolving context.

### [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)

`★ 26.4k` · `TypeScript` · `Custom licence` · last push 2026-09-11

Team-level memory hub that turns conversations, docs and code into four governed assets: chat memory, skills, an LLM wiki and a code graph.
**Use it for:** Aimed at teams rather than solo use; relevant if you want shared, reviewable agent memory.

### [semantica-agi/semantica](https://github.com/semantica-agi/semantica)

`★ 12.7k` · `Python` · `MIT` · last push 2026-09-11

Graph-native infrastructure for context and auditable AI systems, built around accountability of what the model was told.
**Use it for:** Infrastructure-level; use when you need provenance on every fact an agent acted on.

---

## Coding Agents & Harnesses

Alternative runtimes and orchestrators to Claude Code itself.

### [anomalyco/opencode](https://github.com/anomalyco/opencode)

`★ 206.8k` · `TypeScript` · `MIT` · last push 2026-09-12

A fully open-source terminal coding agent, model-agnostic and the base that several other tools here build on.
**Use it for:** Install the CLI as an alternative harness when you want to drive a non-Claude model with a Claude-Code-like workflow.

### [openai/codex](https://github.com/openai/codex)

`★ 123.4k` · `Rust` · `Apache-2.0` · last push 2026-09-12

OpenAI's lightweight Rust coding agent that runs in your terminal.
**Use it for:** Install via npm or Homebrew; worth having alongside Claude Code for cross-checking a second model on the same repo.

### [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC)

`★ 35.9k` · `TypeScript` · `MIT` · last push 2026-09-12

Open multi-agent interactive classroom that spins up an immersive multi-agent learning session in one click.
**Use it for:** Educational rather than production; useful for seeing multi-agent choreography end to end.

### [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix)

`★ 35.5k` · `Go` · `MIT` · last push 2026-09-12

A DeepSeek-native terminal coding agent engineered around prefix-cache stability so long-running sessions stay cheap.
**Use it for:** Use with DeepSeek models; the caching design is the interesting part even if you do not adopt it.

### [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude)

`★ 33.2k` · `TypeScript` · `Custom licence` · last push 2026-09-12

An open terminal agent that runs anywhere and talks to any LLM provider, positioned as a provider-neutral Claude Code.
**Use it for:** Use when you want the Claude Code interaction model pointed at local or cheap models.

### [block/buzz](https://github.com/block/buzz)

`★ 32.6k` · `Rust` · `Apache-2.0` · last push 2026-09-12

A self-hosted relay workspace where humans and agents coordinate in shared channels and threads.
**Use it for:** Run it when several agents and people need one place to talk rather than isolated sessions.

### [different-ai/openwork](https://github.com/different-ai/openwork)

`★ 23.5k` · `TypeScript` · `Custom licence` · last push 2026-09-12

Open-source alternative to Claude Cowork, built on OpenCode, for longer-running non-terminal agent work.
**Use it for:** Self-host it if you want Cowork-style task delegation without the hosted product.

### [apache/maka](https://github.com/apache/maka)

`★ 5.3k` · `TypeScript` · `Apache-2.0` · last push 2026-09-12

Apache incubating project: a high-performance agent workspace that keeps a complete auditable record of everything the agent did.
**Use it for:** Use where you need a replayable audit trail of agent actions rather than scrollback.

### [Bino5150/lumina](https://github.com/Bino5150/lumina)

`★ 168` · `Python` · `Apache-2.0` · last push 2026-09-11

A desktop agent harness designed for local inference on consumer hardware, with memory that grows over time.
**Use it for:** Run it when you want an agent that stays entirely on your machine.

### [RealDealCPA-VR/Iron-Jarvis](https://github.com/RealDealCPA-VR/Iron-Jarvis)

`★ 56` · `Python` · `Custom licence` · last push 2026-09-12

A local-first "AI operating system": a fleet of agents that plan, build, review, schedule and remember, with every action logged and secrets encrypted on disk.
**Use it for:** Self-host as an orchestration layer; heavier than a CLI agent, so only worth it if you want scheduled autonomous work.

### [DusanCar-sudo/aura-code](https://github.com/DusanCar-sudo/aura-code)

`★ 43` · `TypeScript` · `MIT` · last push 2026-09-09

A TUI coding agent whose distinguishing feature is persistent memory across sessions.
**Use it for:** Try it if session-to-session recall matters more to you than raw model quality.

### [rutvej/DAA](https://github.com/rutvej/DAA)

`★ 42` · `Python` · `MIT` · last push 2026-09-08

A self-hosted debugging agent that triages production errors and opens pull requests with fixes, built on LangChain with Gemini, GPT-4o or Claude.
**Use it for:** Deploy with its Docker setup and wire it to your error tracker for overnight triage.

---

## LLM Gateways & Model Routing

One endpoint in front of many providers, for failover and cost control.

### [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute)

`★ 65k` · `TypeScript` · `MIT` · last push 2026-09-12

MIT AI gateway exposing one endpoint over 352 providers and 1200+ models, with quota-aware fallback and built-in token compression.
**Use it for:** Point Claude Code, Codex or Cursor at its endpoint to fail over automatically when a provider rate-limits you.

### [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi)

`★ 25.6k` · `TypeScript` · `MIT` · last push 2026-09-10

Aggregates 34 free LLM providers and 635 free model endpoints behind one OpenAI-compatible `/v1` endpoint with smart routing and failover.
**Use it for:** Explicitly for personal experimentation; use it for throwaway testing, not production work.

### [NVIDIA-NeMo/Switchyard](https://github.com/NVIDIA-NeMo/Switchyard)

`★ 2.9k` · `Python` · `Apache-2.0` · last push 2026-09-11

NVIDIA's router that spreads traffic across models and providers while preserving native OpenAI and Anthropic API compatibility.
**Use it for:** Use for benchmarking and cost/performance tuning without rewriting client code.

---

## Local Inference & Models

Running and training models on your own hardware.

### [jingyaogong/minimind](https://github.com/jingyaogong/minimind)

`★ 60.7k` · `Python` · `Apache-2.0` · last push 2026-09-10

Trains a 64M-parameter LLM from scratch in about two hours, with the full pipeline exposed.
**Use it for:** The clearest hands-on way to understand pretraining, SFT and LoRA end to end.

### [lyogavin/airllm](https://github.com/lyogavin/airllm)

`★ 34.2k` · `Jupyter Notebook` · `Apache-2.0` · last push 2026-09-11

Runs 70B-parameter inference on a single 4GB GPU by streaming layers rather than loading the whole model.
**Use it for:** Use when you want to run a large model locally on modest hardware and can accept slow throughput.

### [google-research/timesfm](https://github.com/google-research/timesfm)

`★ 32.3k` · `Python` · `Apache-2.0` · last push 2026-09-09

Google Research's pretrained time-series foundation model for forecasting.
**Use it for:** Use for zero-shot forecasting on your own series instead of fitting a bespoke model.

### [modular/modular](https://github.com/modular/modular)

`★ 29.7k` · `Mojo` · `Custom licence` · last push 2026-09-11

The Modular Platform: the MAX inference framework and the Mojo language, for high-performance AI serving.
**Use it for:** Use MAX to serve models fast; Mojo is only worth the learning cost if you are writing kernels.

### [cactus-compute/needle](https://github.com/cactus-compute/needle)

`★ 10.9k` · `Python` · `Apache-2.0` · last push 2026-09-08

A 14MB foundation model for phones, wearables, smart home devices and robots.
**Use it for:** Embed on-device where a full LLM will not fit; expect narrow capability at that size.

---

## Web Data, Scraping & Browser Automation

Getting the outside world into an agent's context.

### [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)

`★ 179.3k` · `TypeScript` · `AGPL-3.0` · last push 2026-09-12

The context API to search, scrape and interact with the web at scale, returning LLM-ready markdown.
**Use it for:** You already have Firecrawl skills installed; self-host this repo if you want to stop paying per-credit.

### [browser-use/browser-use](https://github.com/browser-use/browser-use)

`★ 114.3k` · `Python` · `MIT` · last push 2026-09-10

Python framework that lets an LLM drive a real browser to complete tasks.
**Use it for:** Use for agentic flows that need clicking and logins; note your own preference is the `agent-browser` CLI first.

### [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)

`★ 79.5k` · `Python` · `MIT` · last push 2026-09-01

One CLI that reads and searches Twitter, Reddit, YouTube, GitHub, Bilibili and XiaoHongShu without paying platform API fees.
**Use it for:** Install the CLI and call it from an agent for social research across sites your other scrapers gate.

### [kepano/defuddle](https://github.com/kepano/defuddle)

`★ 9.4k` · `TypeScript` · `MIT` · last push 2026-09-11

Extracts the main content of any page as clean Markdown, stripping chrome and boilerplate.
**Use it for:** Use as a lightweight local alternative when you only need readable text and not a full scraping service.

### [aldinokemal/go-whatsapp-web-multidevice](https://github.com/aldinokemal/go-whatsapp-web-multidevice)

`★ 4.7k` · `Go` · `MIT` · last push 2026-09-09

A memory-efficient Go WhatsApp REST API with UI, multi-account support, webhooks, MCP and Chatwoot integration.
**Use it for:** Self-host to give agents or a support desk programmatic WhatsApp access.

### [mvanhorn/agentcookie](https://github.com/mvanhorn/agentcookie)

`★ 827` · `Go` · `MIT` · last push 2026-09-10

Continuously syncs Chrome sessions from your daily-driver Mac to an agent machine over Tailscale so automation wakes up already authenticated.
**Use it for:** Relevant to your setup: it solves logged-in-session reuse without handing over passwords, though Google sessions stay out of scope.

### [zapier/connectors](https://github.com/zapier/connectors)

`★ 166` · `TypeScript` · `Custom licence` · last push 2026-08-25

Lets an agent connect to the apps you already use, with or without Zapier in the middle.
**Use it for:** Use to give an agent authenticated access to SaaS tools without writing each integration.

---

## Diagrams, Docs & Writing

Producing readable artefacts rather than code.

### [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)

`★ 131.6k` · `TypeScript` · `MIT` · last push 2026-09-11

Virtual whiteboard for hand-drawn-style diagrams, with real-time collaboration.
**Use it for:** Self-host or use the hosted app; you already have an Excalidraw MCP connector available.

### [facebook/docusaurus](https://github.com/facebook/docusaurus)

`★ 66.2k` · `TypeScript` · `MIT` · last push 2026-09-11

The standard React-based static site generator for documentation sites.
**Use it for:** Scaffold with `npx create-docusaurus@latest`; the default choice when a project needs real docs.

### [tt-a1i/archify](https://github.com/tt-a1i/archify)

`★ 58.7k` · `JavaScript` · `MIT` · last push 2026-09-12

Agent skill that produces verifiable architecture, sequence, data-flow and lifecycle diagrams as self-contained animated HTML.
**Use it for:** Invoke when documenting a system; output is standalone HTML with crisp export, no Mermaid.

### [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)

`★ 38.6k` · `HTML` · `MIT` · last push 2026-09-10

38 editorial diagram types as self-contained HTML plus SVG, deliberately avoiding shadow-heavy Mermaid defaults.
**Use it for:** Use for explanatory or presentation diagrams where visual quality matters.

### [languagetool-org/languagetool](https://github.com/languagetool-org/languagetool)

`★ 15k` · `Java` · `LGPL-2.1` · last push 2026-09-11

Open-source style and grammar checker covering 25+ languages.
**Use it for:** Self-host the server and point editors at it to keep proofreading local rather than sending text to a cloud service.

### [stephengpope/shockwave](https://github.com/stephengpope/shockwave)

`★ 206` · `TypeScript` · `MIT` · last push 2026-08-09

A local, file-based notes app where notes stay as plain `.md` files you own, with a coding agent built in and GitHub as the sync layer.
**Use it for:** Use if you want agent-editable notes without a proprietary store.

### [Onyx-Dev-Labs/doodle-note](https://github.com/Onyx-Dev-Labs/doodle-note)

`★ 167` · `TypeScript` · `MIT` · last push 2026-09-11

Privacy-first, local-first meeting capture with AI notes.
**Use it for:** Run locally for meeting transcription and summaries that never leave the machine.

---

## Video, Image & Audio

Media generation, capture and parsing.

### [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo)

`★ 122.6k` · `Python` · `MIT` · last push 2026-09-11

Generates HD short-form videos from a topic or keyword through an automated AI workflow.
**Use it for:** Run locally to batch-produce short-form content; quality depends heavily on the models you wire in.

### [remotion-dev/remotion](https://github.com/remotion-dev/remotion)

`★ 59k` · `TypeScript` · `Custom licence` · last push 2026-09-11

Make videos programmatically with React, with a full preview studio and render pipeline.
**Use it for:** Use when you want video-as-code in a React codebase; HyperFrames targets the same problem for agents.

### [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)

`★ 49.1k` · `TypeScript` · `Apache-2.0` · last push 2026-09-12

Write HTML, render video: a composition framework built specifically for agents to author motion graphics.
**Use it for:** You already have the `hyperframes` skills installed; it is the default path when an agent needs to produce video.

### [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2)

`★ 31.4k` · `JavaScript` · `MIT` · last push 2026-09-11

A prompt-as-code library for GPT Image 2 and 2.5 with 530+ worked cases, 20+ industrial templates and reusable skills.
**Use it for:** Mine it for prompt patterns before writing image prompts from scratch.

### [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR)

`★ 25.5k` · `Python` · `MIT` · last push 2026-07-29

Baidu's OCR model aimed at one-shot parsing of very long documents.
**Use it for:** Use for bulk document parsing where page-by-page OCR loses structure.

### [CapSoftware/Cap](https://github.com/CapSoftware/Cap)

`★ 22.1k` · `Rust` · `Custom licence` · last push 2026-09-12

Open-source Loom alternative for beautiful, shareable screen recordings.
**Use it for:** Install on macOS as a self-hosted replacement for Loom.

### [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice)

`★ 11.5k` · `Swift` · `GPL-3.0` · last push 2026-09-11

macOS dictation app with on-device speech-to-text and a custom AI enhancement model, positioned as a local Wispr Flow alternative.
**Use it for:** Install on your Mac for dictation that does not send audio to a cloud service.

### [mat-nolen/tldr-radio](https://github.com/mat-nolen/tldr-radio)

`★ 95` · `Python` · `MIT` · last push 2026-08-29

Turns the daily TLDR newsletters into a podcast, deterministically and without an LLM in the loop.
**Use it for:** Run on a schedule if you would rather listen to TLDR than read it.

### [AhmedAburady/imagine-cli](https://github.com/AhmedAburady/imagine-cli)

`★ 57` · `Go` · `AGPL-3.0` · last push 2026-09-09

A single Go binary for image generation configured entirely by one YAML file, with no environment variables.
**Use it for:** Install with `go install` and point it at a provider; good for scripted batch image generation.

---

## Security, OSINT & Privacy

Defensive tooling, authorised research, and self-hosted privacy infrastructure.

### [dani-garcia/vaultwarden](https://github.com/dani-garcia/vaultwarden)

`★ 67.2k` · `Rust` · `AGPL-3.0` · last push 2026-09-09

A lightweight Rust server that is API-compatible with Bitwarden clients.
**Use it for:** Self-host to run your own password vault while keeping the official Bitwarden apps.

### [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill)

`★ 35.6k` · `PowerShell` · `MIT` · last push 2026-09-03

A reverse-engineering and authorised-penetration-testing skill router that bootstraps toolchains on demand and keeps a self-evolving knowledge base.
**Use it for:** For authorised security research only; it assumes you have permission for the target.

### [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)

`★ 32.6k` · `Python` · `Apache-2.0` · last push 2026-08-31

817 structured cybersecurity skills mapped to MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, D3FEND and NIST AI RMF across 29 domains.
**Use it for:** Install the domains you need for defensive security work; Apache 2.0 and platform-agnostic.

### [goauthentik/authentik](https://github.com/goauthentik/authentik)

`★ 25.4k` · `Python` · `Custom licence` · last push 2026-09-12

Self-hosted identity provider covering SSO, SAML, OAuth2, OIDC and LDAP.
**Use it for:** Deploy as the auth layer in front of your other self-hosted services.

### [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector)

`★ 17k` · `Python` · `Apache-2.0` · last push 2026-09-11

Security scanner for AI agent skills: detects prompt injection, data exfiltration, malicious patterns and supply-chain risk in Claude Code, Codex and MCP skills.
**Use it for:** Run it over any skill in this list before you install it; the single most useful safety tool here given how many third-party skills you are collecting.

### [megadose/holehe](https://github.com/megadose/holehe)

`★ 14.9k` · `Python` · `GPL-3.0` · last push 2024-09-10

Checks whether an email address is registered on a range of sites by probing forgotten-password flows.
**Use it for:** OSINT tool for authorised investigations; note it has not been updated since 2024.

### [kubescape/kubescape](https://github.com/kubescape/kubescape)

`★ 11.7k` · `Go` · `Apache-2.0` · last push 2026-09-11

Kubernetes security platform covering risk analysis, compliance and misconfiguration scanning in IDE, CI and cluster.
**Use it for:** Run in CI against your manifests; the fastest way to catch misconfigured workloads.

### [veracrypt/VeraCrypt](https://github.com/veracrypt/VeraCrypt)

`★ 11.6k` · `C` · `Custom licence` · last push 2026-07-15

Strong disk and volume encryption, the maintained successor to TrueCrypt.
**Use it for:** Use for encrypted containers or full-disk encryption on external drives.

### [antoniaci/blackbird](https://github.com/antoniaci/blackbird)

`★ 8.1k` · `Python` · `No licence` · last push 2025-07-13

OSINT tool that searches for accounts by username or email across social networks.
**Use it for:** Use for authorised footprint checks; the repo moved from `p1ngul1n0/blackbird` and last shipped in 2025.

---

## Self-Hosted Apps & OSS Alternatives

Replacements for commercial SaaS that you run yourself.

### [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk)

`★ 123.2k` · `Rust` · `AGPL-3.0` · last push 2026-09-12

Open-source remote desktop designed for self-hosting, as a TeamViewer alternative.
**Use it for:** Run your own relay server so remote sessions never touch a third party.

### [immich-app/immich](https://github.com/immich-app/immich)

`★ 113.9k` · `TypeScript` · `AGPL-3.0` · last push 2026-09-12

High-performance self-hosted photo and video management with mobile apps and ML-powered search.
**Use it for:** The strongest Google Photos replacement; run it with Docker Compose on a machine with real storage.

### [AppFlowy-IO/AppFlowy](https://github.com/AppFlowy-IO/AppFlowy)

`★ 76.5k` · `Dart` · `AGPL-3.0` · last push 2026-09-10

Open-source Notion alternative for projects, wikis and teams, with AI built in and your data kept local.
**Use it for:** Install the desktop app or self-host the backend if you want Notion without the lock-in.

### [penpot/penpot](https://github.com/penpot/penpot)

`★ 59.9k` · `Clojure` · `MPL-2.0` · last push 2026-09-11

Open-source design and prototyping platform built on open web standards, with real designer-developer handoff.
**Use it for:** Self-host as a Figma alternative; files are SVG-native so they stay portable.

### [twentyhq/twenty](https://github.com/twentyhq/twenty)

`★ 56.6k` · `TypeScript` · `Custom licence` · last push 2026-09-11

Open alternative to Salesforce, designed around AI workflows.
**Use it for:** Self-host as a CRM; the data model is far more approachable than Salesforce's.

### [TryGhost/Ghost](https://github.com/TryGhost/Ghost)

`★ 55.3k` · `TypeScript` · `MIT` · last push 2026-09-12

Publishing platform with memberships, subscriptions and newsletters built in.
**Use it for:** Self-host for a blog or paid newsletter without Substack's revenue share.

### [calcom/cal.diy](https://github.com/calcom/cal.diy)

`★ 48.4k` · `TypeScript` · `MIT` · last push 2026-09-11

Cal.com's scheduling infrastructure, open-sourced for embedding booking into your own products.
**Use it for:** Self-host as a Calendly replacement or use it as a scheduling API.

### [PostHog/posthog](https://github.com/PostHog/posthog)

`★ 39.8k` · `Python` · `Custom licence` · last push 2026-09-12

Product analytics platform bundling session replay, feature flags, experiments, error tracking, logs and AI observability.
**Use it for:** Self-host or use the cloud tier; it replaces four or five separate SaaS tools.

### [nextcloud/server](https://github.com/nextcloud/server)

`★ 36.8k` · `PHP` · `AGPL-3.0` · last push 2026-09-12

The mature self-hosted file sync, sharing and groupware platform.
**Use it for:** Deploy as your own Google Drive; the app ecosystem covers calendar, contacts and office.

### [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot)

`★ 36.7k` · `Ruby` · `Custom licence` · last push 2026-09-11

Open-source omnichannel customer support desk: live chat, email and social inboxes.
**Use it for:** Self-host as an Intercom or Zendesk replacement; pairs with the WhatsApp API above.

### [dubinc/dub](https://github.com/dubinc/dub)

`★ 24.7k` · `TypeScript` · `Custom licence` · last push 2026-09-12

Modern link attribution and short-link platform used by Framer, Perplexity and Twilio.
**Use it for:** Self-host for branded short links with real click analytics.

### [knadh/listmonk](https://github.com/knadh/listmonk)

`★ 23.4k` · `Go` · `AGPL-3.0` · last push 2026-09-06

High-performance self-hosted newsletter and mailing list manager shipped as a single Go binary.
**Use it for:** Run it with Postgres and an SMTP provider for cheap, unlimited list sending.

### [every-app/open-seo](https://github.com/every-app/open-seo)

`★ 18.5k` · `TypeScript` · `MIT` · last push 2026-09-12

Open-source alternative to Semrush and Ahrefs for keyword, backlink and site analysis.
**Use it for:** Self-host for SEO research without an enterprise subscription.

### [documenso/documenso](https://github.com/documenso/documenso)

`★ 15k` · `TypeScript` · `AGPL-3.0` · last push 2026-09-12

Open-source DocuSign alternative for e-signatures.
**Use it for:** Self-host when you need signed documents but not a per-seat SaaS contract.

### [plankanban/planka](https://github.com/plankanban/planka)

`★ 12.5k` · `JavaScript` · `Custom licence` · last push 2026-09-11

Elegant self-hosted Kanban project tracking for teams.
**Use it for:** Deploy as a Trello replacement; the free community edition is fully featured.

---

## Developer Tools & Desktop

General-purpose utilities that are not agent-specific.

### [mui/material-ui](https://github.com/mui/material-ui)

`★ 99k` · `JavaScript` · `MIT` · last push 2026-09-11

Comprehensive React component library implementing Google's Material Design.
**Use it for:** Install with npm when you need a complete, accessible component set rather than building from primitives.

### [abi/screenshot-to-code](https://github.com/abi/screenshot-to-code)

`★ 78.6k` · `Python` · `MIT` · last push 2026-09-09

Drop in a screenshot and it produces clean HTML/Tailwind, React or Vue code.
**Use it for:** Use to bootstrap a layout from a design image, then refine by hand.

### [omacom/omarchy](https://github.com/omacom/omarchy)

`★ 40.4k` · `Shell` · `MIT` · last push 2026-09-12

DHH's opinionated Arch plus Hyprland Linux setup, packaged as a turnkey developer environment.
**Use it for:** Only relevant on Linux; your saved `basecamp/omarchy` link now redirects here.

### [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view)

`★ 27.4k` · `JavaScript` · `Custom licence` · last push 2026-09-12

A browser-based spy-satellite simulator on a photorealistic 3D globe, driven by real open-source spatial intelligence data.
**Use it for:** Run it in the browser; a good reference for WebGL globe rendering with live data.

### [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi)

`★ 20.7k` · `Rust` · `Apache-2.0` · last push 2026-09-10

Native local-first Rust alternative to Logitech Options+ that remaps buttons, DPI and SmartShift over HID++.
**Use it for:** Install on macOS to configure Logitech peripherals without an account or telemetry.

### [agavra/tuicr](https://github.com/agavra/tuicr)

`★ 3.1k` · `Rust` · `MIT` · last push 2026-09-11

A terminal code-review UI with vim keybindings.
**Use it for:** Install if you would rather review diffs in the terminal than in the GitHub web UI.

---

## Finance & Business

Money, accounting and decision tooling.

### [securo-finance/securo](https://github.com/securo-finance/securo)

`★ 3.3k` · `Python` · `AGPL-3.0` · last push 2026-09-10

Self-hosted, privacy-first personal finance manager.
**Use it for:** Deploy to track accounts and spending without handing a third party your bank data.

### [VonHoltenCodes/SlowBooks-Pro-2026](https://github.com/VonHoltenCodes/SlowBooks-Pro-2026)

`★ 477` · `Python` · `Custom licence` · last push 2026-09-12

Source-available desktop accounting with double-entry bookkeeping, invoicing, US payroll, inventory and bank feeds, no cloud or Docker required.
**Use it for:** Positioned as a QuickBooks 2003 Pro replacement; US-centric, so payroll is only useful there.

### [vikd1000/investment-council](https://github.com/vikd1000/investment-council)

`★ 68` · `Python` · `MIT` · last push 2026-08-10

Simulates 21 legendary investors debating a stock pick and shows where they agree and disagree.
**Use it for:** Runs without an API key; treat it as a structured second opinion, not advice.

---

## Awesome Lists, Learning & Career

Curated indexes and study material, including the upstream sources for this list.

### [public-apis/public-apis](https://github.com/public-apis/public-apis)

`★ 479.1k` · `Python` · `MIT` · last push 2026-09-10

A collective list of free public APIs across every category.
**Use it for:** Search it before paying for a data source or writing a scraper.

### [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer)

`★ 369.5k` · `Python` · `Custom licence` · last push 2026-03-20

The canonical guide to designing large-scale systems, with Anki flashcards for interview prep.
**Use it for:** Work through it for architecture fundamentals; still the best free resource of its kind.

### [jaywcjlove/awesome-mac](https://github.com/jaywcjlove/awesome-mac)

`★ 113.6k` · `Swift` · `CC0-1.0` · last push 2026-09-11

Systematically categorised collection of high-quality macOS software.
**Use it for:** Browse by category when looking for a Mac tool; it is far better curated than a web search.

### [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners)

`★ 68.4k` · `Jupyter Notebook` · `MIT` · last push 2026-09-04

Microsoft's 12-week, 24-lesson AI curriculum with Jupyter notebooks.
**Use it for:** Follow the notebooks for structured fundamentals rather than piecemeal tutorials.

### [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)

`★ 53.9k` · `Python` · `Custom licence` · last push 2026-09-12

The main curated index of Claude Code resources: skills, agents, status lines, plugins and tooling.
**Use it for:** Start here when hunting for new skills; it is the upstream source for much of this list.

### [SimplifyJobs/Summer2027-Internships](https://github.com/SimplifyJobs/Summer2027-Internships)

`★ 47.4k` · `Python` · `No licence` · last push 2026-09-12

Daily-updated listings of Summer 2027 software, data, AI, quant, PM and hardware internships.
**Use it for:** Watch the repo for notifications if you or someone you know is hiring-cycle bound.

### [discoveredlabs/awesome-aeo-seo](https://github.com/discoveredlabs/awesome-aeo-seo)

`★ 110` · `n/a` · `Custom licence` · last push 2026-06-27

Curated AEO and SEO resources for engineers and growth marketers: research, tooling and implementation guides.
**Use it for:** Read alongside `open-seo` if you are working on answer-engine visibility.

---
