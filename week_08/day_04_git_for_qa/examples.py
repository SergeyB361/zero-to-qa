GIT_FLOW = [
    "git checkout -b feature/new-tests",
    "git status",
    "git add .",
    'git commit -m "feat: add api tests"',
    "git push -u origin feature/new-tests",
]

def show_git_flow() -> None:
    for command in GIT_FLOW:
        print(command)

if __name__ == "__main__":
    show_git_flow()
