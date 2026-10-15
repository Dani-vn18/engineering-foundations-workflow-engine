# Engineering Foundations Through Building a Workflow Engine

A learning-by-doing bootcamp for developing engineering judgment by building one system progressively in Python.

## Core idea

We do not add technology because it is popular. A new abstraction, library, service, pattern, database, queue, cloud component, or architecture must earn its place by solving a problem we have already observed.

The learning loop is:

**Problem → Mental model → Minimal theory → Prediction → Experiment → Alternatives → Trade-offs → Decision → Implementation → Tests → Failure experiment → Review → Reflection**

## AI modes

- `TEACH` — explain from first principles.
- `SOCRATIC` — ask questions and give hints; do not reveal the solution.
- `HINT 1` — conceptual hint only.
- `HINT 2` — more concrete hint, still no complete solution.
- `REVIEW` — review my work without rewriting it.
- `DEBUG` — help investigate without automatically fixing the code.
- `CHALLENGE` — test whether I really understand the topic.
- `DEEP DIVE` — go one level lower into internals and mechanisms.

## Start here

1. Read `course/methodology.qmd`.
2. Read `course/00_bootcamp/lego_00.qmd`.
3. Read `exercises/lego_00/README.md`.
4. Run:

```bash
uv sync
uv run pytest tests/test_lego_00.py -q
```

The tests are expected to fail initially. That is intentional.

## Important rule

Passing tests is not the definition of learning.

For each concept, aim to reach:

1. I can explain it.
2. I can build a simple version.
3. I know what problem it solves.
4. I know relevant alternatives.
5. I can justify when **not** to use it.
6. Eventually: I understand approximately how it works internally.
