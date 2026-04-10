def is_balanced(text: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    opening = set(pairs.values())
    stack: list[str] = []

    for char in text:
        if char in opening:
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack


if __name__ == "__main__":
    print(is_balanced("([]{})"))
    print(is_balanced("([)]"))
    print(is_balanced("((())"))
