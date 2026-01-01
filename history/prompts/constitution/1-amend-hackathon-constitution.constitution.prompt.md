---
id: 1
title: Amend Hackathon Constitution
stage: constitution
date: 2025-12-29
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: user
command: /sp.constitution
labels: ["constitution", "hackathon", "spec-driven"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
  - .specify/templates/plan-template.md
  - .specify/templates/spec-template.md
  - .specify/templates/tasks-template.md
  - history/prompts/constitution/1-amend-hackathon-constitution.constitution.prompt.md
tests: []
---

# Amend Hackathon Constitution

## Prompt

```
Project: Hackathon II – Evolution of Todo (AI-Native, Spec-Driven, Cloud-Native)

Purpose:
Iteratively evolve a Todo application from a console app into a cloud-native AI chatbot
using strictly Spec-Driven Development and AI-generated implementations.

Core principles:
- Spec-Driven First: No manual code; all behavior defined in Markdown specs
- AI-Native Architecture: Engineers act as system architects, not syntax writers
- Reusable Intelligence: Agent skills and subagents must be modular and spec-defined
- Progressive Evolution: Each phase builds strictly on the previous phase
- Cloud-Native by Design: Containers, Kubernetes, scalability, and observability included

Phases (mandatory):
1. Console Todo (CRUD)
2. API-based Backend
3. AI Chatbot Integration (Chatkit, Agents SDK)
4. Cloud-Native Deployment (Docker, Minikube, Helm, MCP)
5. Production Deployment (DOKS, scalability, governance)

Feature scope:
- Basic: Add, Delete, Update, View, Complete
- Intermediate: Priorities/Tags, Search/Filter, Sort
- Advanced: Recurring Tasks, Due Dates, Reminders

AI requirements (Phases III–V):
- Natural-language Todo management
- Tool usage and reasoning governed by specs
- Ambiguity handled via clarification flows

Tech standards:
- Backend: FastAPI, SQLModel, Neon
- Frontend: Next.js
- AI: OpenAI Chatkit, Agents SDK, MCP SDK
- Infra: Docker, Kubernetes, Minikube, Helm, DOKS
- Ops/Eventing: Kafka, Dapr, kubectl-ai, kagent

Constraints:
- Manual coding prohibited
- Every feature requires a spec + acceptance criteria
- Specs are the single source of truth

Success criteria:
- All 5 phases completed via Spec-Driven Development
- AI chatbot correctly manages Todos
- Deployed on Minikube and DigitalOcean Kubernetes
- Specs reusable as cloud-native blueprints
```

## Response

Updated the constitution file to reflect the Hackathon II project principles, including:

- Spec-Driven First: All behavior defined in Markdown specs before implementation
- AI-Native Architecture: Engineers act as system architects, not syntax writers
- Test-First (NON-NEGOTIABLE): TDD approach with acceptance criteria in specs
- Integration Testing: Focus on AI chatbot interactions and API contracts
- Cloud-Native by Design: Progressive evolution from console to cloud-native
- Reusable Intelligence: Modular, spec-defined components

Updated dependent templates to align with the new constitution principles and added constitution compliance checkpoints to the development workflow.

## Outcome

The constitution has been successfully updated from version 1.0.0 to 2.0.0, with all dependent templates updated to maintain consistency with the new principles. The project now has a clear governance document that aligns with the Hackathon II objectives.

## Evaluation

The updated constitution properly reflects the project requirements with clear, testable principles that will guide the development process. The templates have been updated to ensure continued alignment throughout the development lifecycle.