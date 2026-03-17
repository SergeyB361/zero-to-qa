# Неделя 3, День 4 — Примеры

import re

text = "Ticket #4821 created"
match = re.search(r"\d+", text)
if match:
    print("First number:", match.group())

line = "Codes: 200 404 500"
print("All numbers:", re.findall(r"\d+", line))

email = "user@example.com"
print("Looks like email:", bool(re.search(r"\w+@\w+\.\w+", email)))

message = "Build 2025 failed"
print(re.sub(r"\d+", "X", message))
