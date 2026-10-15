from workflow_engine.engine import run_workflow


events: list[str] = []


def task_a() -> str:
    events.append("A")
    print("Task A completed")
    return "A-result"


def task_b() -> str:
    events.append("B")
    print("Task B is about to fail")
    raise RuntimeError("simulated failure")


def task_c() -> str:
    events.append("C")
    print("Task C completed")
    return "C-result"


print("Prediction: write down what you think will happen before reading the output.\n")

try:
    results = run_workflow([task_a, task_b, task_c])
    print("Results returned:", results)
except RuntimeError as exc:
    print("Workflow failed:", exc)

print("Tasks that actually executed:", events)
