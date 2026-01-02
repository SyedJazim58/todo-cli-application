<!--
Sync Impact Report:
- Version change: 1.0.0 → 2.0.0
- Modified principles:
  - Spec-Driven First (replaces Library-First)
  - AI-Native Architecture (replaces CLI Interface)
  - Test-First (NON-NEGOTIABLE) (updated focus)
  - Integration Testing (updated focus)
  - Cloud-Native by Design (new principle)
  - Reusable Intelligence (new principle)
- Added sections: Additional Constraints, Development Workflow
- Removed sections: None
- Templates requiring updates:
  - .specify/templates/plan-template.md ✅ updated
  - .specify/templates/spec-template.md ✅ updated
  - .specify/templates/tasks-template.md ✅ updated
- Follow-up TODOs: None
-->

# Hackathon II – Evolution of Todo Constitution

## Core Principles

### Spec-Driven First
All behavior must be defined in Markdown specs before implementation; No manual code without corresponding spec; Specs serve as the single source of truth for all functionality.

### AI-Native Architecture
Engineers act as system architects, not syntax writers; All implementations must be AI-governable and spec-compliant; Natural-language processing and tool usage must be governed by specifications.

### Test-First (NON-NEGOTIABLE)
TDD mandatory: Tests written → User approved → Tests fail → Then implement; Red-Green-Refactor cycle strictly enforced; All features require acceptance criteria defined in specs.

### Integration Testing
Focus areas requiring integration tests: AI chatbot interactions, API contract tests, Cloud-native deployment validation, Spec-implementation alignment verification.

### Cloud-Native by Design
Containers, Kubernetes, scalability, and observability included from phase 1; Progressive evolution: Console → API → AI → Cloud → Production; All phases must build strictly on previous phase.

### Reusable Intelligence
Agent skills and subagents must be modular and spec-defined; Code must be reusable as cloud-native blueprints; Intelligence artifacts (specs, plans, tasks) must be systematically captured and maintained.

## Additional Constraints
Technology stack requirements: Backend (FastAPI, SQLModel, Neon), Frontend (Next.js), AI (OpenAI Chatkit, Agents SDK, MCP SDK), Infra (Docker, Kubernetes, Minikube, Helm, DOKS), Ops/Eventing (Kafka, Dapr, kubectl-ai, kagent); Manual coding is prohibited; Every feature requires a spec + acceptance criteria.

## Development Workflow
Progressive Evolution: Each phase builds strictly on the previous phase; AI requirements include natural-language Todo management, tool usage and reasoning governed by specs, ambiguity handled via clarification flows; Feature scope includes Basic (Add, Delete, Update, View, Complete), Intermediate (Priorities/Tags, Search/Filter, Sort), Advanced (Recurring Tasks, Due Dates, Reminders).

## Governance
Constitution supersedes all other practices; All implementations must comply with Spec-Driven Development requirements; Amendments require documentation, approval, and migration plan; All PRs/reviews must verify compliance with spec-driven principles and AI-native architecture; Complexity must be justified through clear architectural decisions.

**Version**: 2.0.0 | **Ratified**: 2025-06-13 | **Last Amended**: 2025-12-29
