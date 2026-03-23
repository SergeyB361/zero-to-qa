def risk_score(probability: int, impact: int) -> int:
    return probability * impact


if __name__ == "__main__":
    print(risk_score(5, 5))
