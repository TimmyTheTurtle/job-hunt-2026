# AGENTS.md

## Purpose

This repository contains a personal deep research tool project.

The project is a learning vehicle, portfolio project, and applied AI systems engineering exercise.

It should help the owner build a system that can:

- ingest papers, articles, notes, and other document-heavy sources
- normalize them into project-owned artifacts
- retrieve evidence deterministically and semantically
- link ideas across documents, papers, and article drafts
- produce grounded research outputs with citations, uncertainty, and open questions
- preserve durable project memory in repo-visible artifacts

## Project Identity

This project is best understood as a:

**repo-native evidence engine for deep research**

It is not:

- a generic chatbot
- a shallow "chat with PDFs" demo
- a premature SaaS platform
- a black-box answer engine

## Design Principles

1. Evidence first.
2. Project-owned artifacts over opaque vendor-owned meaning.
3. Hybrid retrieval over vector-only retrieval.
4. Human review is part of the system.
5. Explicit links and semantic links must remain distinguishable.
6. Durable memory matters more than context hoarding.
7. Use lightweight but disciplined SDLC.

## Architectural Shape

The intended architecture is:

- corpus and source manifests
- normalization pipeline
- explicit graph substrate
- vector sidecar for semantic similarity
- retrieval and ranking layer
- synthesis layer
- evaluation layer
- artifact promotion layer

## Working Rules

- prefer small inspectable steps
- do not overbuild infrastructure early
- deterministic layers should remain explicit
- semantic results are suggestions until reviewed
- repo-visible artifacts matter more than assistant private memory
- if uncertain between flashy and sober, choose sober

## Agent Startup

Read in this order:

1. `AGENTS.md`
2. `README.md`
3. the smallest relevant subset of `docs/` for the current task

Do not front-load every document in the repository unless the task genuinely requires it.

