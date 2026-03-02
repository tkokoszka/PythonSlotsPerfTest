---
name: review
description: "Review code for consistency, correctness, and potential mistakes. Use when the user asks to review code, check quality, or audit the codebase."
argument-hint: "[all|changed] [--fix]"
---

# Code Review

Review code in this benchmarking project. Focus on real problems — skip cosmetic nitpicks that ruff/pyright already catch.

## Scope

Determine scope and mode from `$ARGUMENTS`:

**Scope** (first positional argument):
- **`changed`** — only uncommitted + staged files. Run `git diff --name-only` and `git diff --cached --name-only` to get the file list. Review `.py` and `.md` files from that list.
- **`all`** (default, also when no argument given) — all `.py` files under `src/`, plus `README.md` and `CLAUDE.md` at the repo root.

**Mode** (flag):
- Without `--fix` — review only. Report findings, do not modify files.
- With `--fix` — review, then fix all found issues. Apply edits directly to files. After fixing, run `uv run pre-commit run -a` to validate changes pass linting/typing.

Read every file in scope before producing findings.

## Review checklist

### 1. Naming consistency

- Scenario classes: `{Feature}Scenario` (e.g. `PythonClassScenario`, `NamedTupleScenario`)
- Each scenario module defines a local `User` type (class, dataclass, NamedTuple, TypedDict, etc.)
- User fields are exactly: `id: str`, `name: str`, `surname: str`, `age: int` (or equivalent for the data structure)
- Functions/variables: snake_case
- Private helpers: prefixed with `_`
- Reporter classes: `{Format}Reporter`
- All scenario modules registered in `all_scenarios.py`

### 2. Scenario consistency

Every scenario must follow the same pattern:

- Inherit `BaseScenario[T]` with the local `User` type as `T`
- Implement `name` property (short display name), `description` property, and `create_one(self, seq_no: int) -> T`
- `create_one` must generate: `id=str(uuid4())`, `name=str(uuid4())`, `surname=str(uuid4())`, `age=random.randint(1, 100)` — same random data strategy across all scenarios so measurements are comparable
- No extra computation in `create_one` that would skew timing (validation overhead from Pydantic is expected and intentional — flag anything else)

### 3. Measurement correctness

In `runner/run.py` and related:

- `gc.collect()` must be called before each scenario run
- The results list must stay alive during measurement — if it's garbage-collected or overwritten, memory delta is invalid
- No stray `gc.collect()` between start and end snapshots (would deflate memory readings)

### 4. Potential mistakes

- Missing type annotations on function signatures
- Imports that don't match the module's purpose
- Mutable default arguments
- Scenarios creating objects with different fields or field types than the canonical User
- Reporter accessing stats fields that don't exist on `ExecutionStats`
- Off-by-one in sequence numbering or table indexing
- Any `type: ignore` comments — flag and evaluate necessity

### 5. Documentation (`.md` files)

- README accurately describes the project, how to run it, and listed scenarios match what's actually implemented
- CLAUDE.md instructions are consistent with actual tooling config (`pyproject.toml`, `.pre-commit-config.yaml`)
- No stale references to removed/renamed files, functions, or scenarios

### 6. Architecture / module hygiene

- `__init__.py` files should be empty (no re-exports) unless there's a reason
- No circular imports
- `all_scenarios.py` should list every scenario module and nothing else

## Output format

Produce a structured review report:

```
## Review: [scope]

### Findings

For each finding:
- **[Category]** file_path:line — description of the issue
  - Suggested fix (if applicable)

### Summary

- Total files reviewed: N
- Issues found: N (X critical, Y minor)
- Overall assessment: one sentence
```

Categorize severity:
- **Critical**: incorrect measurement, data inconsistency across scenarios, bugs
- **Minor**: style inconsistency, missing annotation, naming deviation

If no issues are found, say so clearly — do not invent problems.

## Fix mode (`--fix`)

When `--fix` is present:

1. First, complete the full review and present findings as above.
2. Then fix each issue using Edit tool. Do not fix cosmetic issues that ruff/pyright handle — only fix issues from the checklist above.
3. After all edits, run `uv run pre-commit run -a` and resolve any failures.
4. Append a summary of changes made:

```
### Changes applied

- file_path:line — what was changed and why
```

Do not create new files. Do not refactor beyond what's needed to fix the finding.
