def show_set_basics() -> None:
    skills = {"python", "pytest", "api", "pytest"}
    print(skills)
    skills.add("playwright")
    print("python" in skills)
