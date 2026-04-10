def classify_problem(problem_name: str) -> str:
    mapping = {
        "pair sum": "hash or two pointers",
        "range sum": "prefix sums",
        "shortest path unweighted": "bfs",
        "top k": "heap",
    }
    return mapping.get(problem_name, "analyze manually")


if __name__ == "__main__":
    print(classify_problem("pair sum"))
    print(classify_problem("top k"))
    print(classify_problem("unknown"))
