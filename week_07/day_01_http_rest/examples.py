HTTP_METHODS = {
    "get_user": "GET",
    "create_user": "POST",
    "update_user": "PUT",
    "delete_user": "DELETE",
}

def show_methods() -> None:
    for name, method in HTTP_METHODS.items():
        print(name, method)

if __name__ == "__main__":
    show_methods()
