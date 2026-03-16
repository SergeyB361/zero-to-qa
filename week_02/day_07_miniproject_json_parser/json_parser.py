import json
from pathlib import Path


BASE_DIR = Path(__file__).parent
USERS_FILE = BASE_DIR / "users.json"


def load_users(path):
    with open(path, "r") as f:
        users = json.load(f)
    return users

def get_names(users):
    names = [user["name"] for user in users]

    return names

def get_active_users(users):
    active_users = [user for user in users if (user["active"])]
    return active_users

def get_active_users_names(users):
    active_users_names = [user["name"] for user in users if (user["active"])]
    return active_users_names


def get_average_age(users):
    sum_age = sum([user["age"] for user in users])
    quantity = len(users)
    average_age = round(sum_age / quantity,2)
    return average_age

def main():
    users = load_users(USERS_FILE)
    print("Total users:", len(users))

    names = get_names(users)
    print("Names:", names)

    active_users = get_active_users(users)
    print("Active users:", len(active_users))

    active_users_names = get_active_users_names(users)
    print("Active users names:", active_users_names)

    average_age = get_average_age(users)
    print("Average age:", average_age)


if __name__ == "__main__":
    main()





