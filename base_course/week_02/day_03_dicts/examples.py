# Неделя 2, День 3 — Примеры: словари

user = {"name": "Sergey", "role": "QA", "active": True}
print(user["name"])
print(user.get("level", "junior"))

user["level"] = "middle"
print(user)

for key, value in user.items():
    print(f"{key}: {value}")

api_stats = {
    "ok": 120,
    "client_error": 14,
    "server_error": 3,
}

print(api_stats.keys())
print(api_stats.values())
print(api_stats.items())

del api_stats["server_error"]
print(api_stats)
