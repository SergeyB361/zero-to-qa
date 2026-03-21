CICD_IMPROVEMENTS = [
    "cache dependencies",
    "separate jobs",
    "store artifacts",
    "publish reports",
]

def show_cicd_improvements() -> None:
    for item in CICD_IMPROVEMENTS:
        print(item)

if __name__ == "__main__":
    show_cicd_improvements()
