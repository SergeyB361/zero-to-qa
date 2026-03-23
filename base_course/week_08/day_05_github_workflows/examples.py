WORKFLOW_STEPS = [
    "checkout repository",
    "setup python",
    "install dependencies",
    "run pytest",
]

def show_workflow_steps() -> None:
    for step in WORKFLOW_STEPS:
        print(step)

if __name__ == "__main__":
    show_workflow_steps()
