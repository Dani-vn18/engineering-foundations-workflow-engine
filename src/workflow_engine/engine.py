from collections.abc import Callable


Task = Callable[[], str]


def run_workflow(tasks: list[Task]) -> list[str]:
    """Execute tasks in order and return their results.

    LEGO 00:
    Implement the smallest solution that satisfies the current requirements.
    Do not add retries, persistence, concurrency, queues, or framework code.
    """
    raise NotImplementedError("Lego 00: implement run_workflow")
