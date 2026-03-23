def choose_oracle(requirement_defined: bool, domain_rule_defined: bool) -> str:
    if requirement_defined:
        return "requirements"
    if domain_rule_defined:
        return "domain rules"
    return "needs clarification"


if __name__ == "__main__":
    print(choose_oracle(True, False))
