---
description: "Task list for Basic Todo CLI Application"
---

# Tasks: Basic Todo CLI App

**Input**: Design documents from `/specs/001-basic-level-core-todo-essentials/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Constitution Compliance**: All tasks must align with constitution principles:
- Spec-Driven First: Implementation follows specs defined in Markdown
- AI-Native Architecture: AI-governable and spec-compliant design
- Test-First: Tests written before implementation with clear acceptance criteria
- Cloud-Native by Design: Progressive evolution approach (Console → API → AI → Cloud → Production)
- Reusable Intelligence: Modular and spec-defined components

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Initialize uv project with pyproject.toml configuration
- [x] T002 [P] Create project directory structure (src/todo_cli/, tests/, etc.)
- [x] T003 [P] Add initial __init__.py files to package directories
- [x] T004 Configure dependencies in pyproject.toml (inquirer, rich, pytest)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T005 Create Task model class in src/todo_cli/models/task.py
- [x] T006 Create TaskList model class in src/todo_cli/models/task.py
- [x] T007 [P] Implement Task validation logic (title length, required fields)
- [x] T008 [P] Implement Task ID generation and uniqueness
- [x] T009 [P] Implement Task timestamps (created_at, updated_at)
- [x] T010 Create TaskService class in src/todo_cli/services/task_service.py
- [x] T011 [P] Implement TaskService foundational methods (add_task, get_all_tasks)
- [x] T012 [P] Implement TaskService remaining methods (get_task_by_id, update_task, delete_task, mark_complete)
- [x] T013 Create basic CLI structure in src/todo_cli/cli/main.py
- [x] T014 Configure test framework with pytest and conftest.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to create new todo items with title and optional description

**Independent Test**: Can be fully tested by creating new tasks and verifying they appear in the system. The system should accept task creation requests and store them successfully.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T015 [P] [US1] Unit test for Task creation with valid title in tests/unit/test_task.py
- [x] T016 [P] [US1] Unit test for Task validation (empty title rejection) in tests/unit/test_task.py

### Implementation for User Story 1

- [x] T017 [P] [US1] Implement Task creation with validation in src/todo_cli/models/task.py
- [x] T018 [US1] Implement add_task method in TaskService with validation in src/todo_cli/services/task_service.py
- [x] T019 [US1] Create CLI interface for adding tasks in src/todo_cli/cli/main.py
- [x] T020 [US1] Add user prompts for task title and description using inquirer
- [x] T021 [US1] Integrate CLI add task with TaskService in src/todo_cli/cli/main.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Task List (Priority: P2)

**Goal**: Enable users to view all tasks with completion status indicators

**Independent Test**: Can be fully tested by creating several tasks and then viewing the complete task list. The system should display all stored tasks with their relevant information.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [x] T022 [P] [US2] Unit test for get_all_tasks functionality in tests/unit/test_task_service.py
- [x] T023 [P] [US2] Test for task list display formatting in tests/unit/test_task_service.py

### Implementation for User Story 2

- [x] T024 [P] [US2] Implement get_all_tasks method in TaskService in src/todo_cli/services/task_service.py
- [x] T025 [US2] Create CLI interface for viewing tasks in src/todo_cli/cli/main.py
- [x] T026 [US2] Implement rich formatting for task list display
- [x] T027 [US2] Add visual indicators for task completion status
- [x] T028 [US2] Integrate CLI view tasks with TaskService in src/todo_cli/cli/main.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Tasks as Complete (Priority: P3)

**Goal**: Enable users to mark tasks as complete/incomplete to track progress

**Independent Test**: Can be fully tested by marking tasks as complete and verifying their status changes. The system should update the completion status and reflect this change in displays.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [x] T029 [P] [US3] Unit test for mark_task_complete functionality in tests/unit/test_task_service.py
- [x] T030 [P] [US3] Unit test for mark_task_incomplete functionality in tests/unit/test_task_service.py

### Implementation for User Story 3

- [x] T031 [P] [US3] Implement mark_task_complete method in TaskService in src/todo_cli/services/task_service.py
- [x] T032 [P] [US3] Implement mark_task_incomplete method in TaskService in src/todo_cli/services/task_service.py
- [x] T033 [US3] Create CLI interface for marking tasks in src/todo_cli/cli/main.py
- [x] T034 [US3] Add user prompts for task selection and status toggle
- [x] T035 [US3] Integrate CLI mark task with TaskService in src/todo_cli/cli/main.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Update Task Details (Priority: P4)

**Goal**: Enable users to modify task titles or details to keep tasks accurate and up-to-date

**Independent Test**: Can be fully tested by updating existing tasks and verifying the changes are preserved. The system should allow modification of task information while maintaining the task identity.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [x] T036 [P] [US4] Unit test for update_task functionality in tests/unit/test_task_service.py
- [x] T037 [P] [US4] Test for task update validation in tests/unit/test_task_service.py

### Implementation for User Story 4

- [x] T038 [P] [US4] Enhance update_task method in TaskService with validation in src/todo_cli/services/task_service.py
- [x] T039 [US4] Create CLI interface for updating tasks in src/todo_cli/cli/main.py
- [x] T040 [US4] Add user prompts for task selection and new details
- [x] T041 [US4] Implement update validation and error handling
- [x] T042 [US4] Integrate CLI update task with TaskService in src/todo_cli/cli/main.py

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Delete Tasks (Priority: P5)

**Goal**: Enable users to remove tasks they no longer need to keep task list relevant and manageable

**Independent Test**: Can be fully tested by deleting tasks and verifying they are removed from the system. The system should properly remove tasks and not display them in the task list.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [x] T043 [P] [US5] Unit test for delete_task functionality in tests/unit/test_task_service.py
- [x] T044 [P] [US5] Test for delete validation (non-existent task handling) in tests/unit/test_task_service.py

### Implementation for User Story 5

- [x] T045 [P] [US5] Enhance delete_task method in TaskService with validation in src/todo_cli/services/task_service.py
- [x] T046 [US5] Create CLI interface for deleting tasks in src/todo_cli/cli/main.py
- [x] T047 [US5] Add user prompts for task selection and confirmation
- [x] T048 [US5] Implement delete validation and error handling for non-existent tasks
- [x] T049 [US5] Integrate CLI delete task with TaskService in src/todo_cli/cli/main.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T050 [P] Create main application loop with menu interface in src/todo_cli/cli/main.py
- [x] T051 [P] Add error handling and user feedback throughout CLI
- [x] T052 [P] Implement edge case handling (empty title rejection, non-existent task handling)
- [x] T053 [P] Add input validation and sanitization
- [x] T054 [P] Create comprehensive README.md with usage instructions
- [x] T055 [P] Add proper exit functionality to CLI
- [x] T056 [P] Run end-to-end tests to verify all functionality
- [x] T057 [P] Performance testing to ensure <200ms response times
- [x] T058 [P] Update quickstart.md with final usage instructions

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P4 → P5)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services (if not already created in foundational phase)
- Services before CLI interface
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

### Constitution Compliance Checkpoints

- At each phase completion, verify alignment with constitution principles:
  - Spec-Driven First: All behavior defined in specs before implementation
  - AI-Native Architecture: Implementation is AI-governable and spec-compliant
  - Test-First: Tests written before implementation with clear acceptance criteria
  - Cloud-Native by Design: Progressive evolution approach maintained
  - Reusable Intelligence: Components remain modular and spec-defined

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Run basic functionality tests
6. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently
4. Final integration and polish phase

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
