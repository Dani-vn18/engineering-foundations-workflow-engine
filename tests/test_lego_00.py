import pytest

from workflow_engine.engine import run_workflow


def test_runs_tasks_in_order_and_returns_results() -> None:
    events: list[str] = []

    def task_a() -> str:
        events.append("A")
        return "result-A"

    def task_b() -> str:
        events.append("B")
        return "result-B"

    def task_c() -> str:
        events.append("C")
        return "result-C"

    results = run_workflow([task_a, task_b, task_c])

    assert events == ["A", "B", "C"]
    assert results == ["result-A", "result-B", "result-C"]


def test_empty_workflow_returns_empty_list() -> None:
    assert run_workflow([]) == []


def test_stops_immediately_when_a_task_fails() -> None:
    events: list[str] = []

    def task_a() -> str:
        events.append("A")
        return "result-A"

    def task_b() -> str:
        events.append("B")
        raise RuntimeError("B failed")

    def task_c() -> str:
        events.append("C")
        return "result-C"

    with pytest.raises(RuntimeError, match="B failed"):
        run_workflow([task_a, task_b, task_c])

    assert events == ["A", "B"]


def test_each_task_runs_only_once() -> None:
    executions = {"count": 0}

    def task() -> str:
        executions["count"] += 1
        return "ok"

    assert run_workflow([task]) == ["ok"]
    assert executions["count"] == 1
