# День 7 — Мини-проект: калькулятор


def add(a, b):
    pass


def sub(a, b):
    pass


def mul(a, b):
    pass


def div(a, b):
    pass


def read_number(prompt):
    return print("Число: ") 


def main():
    print("Консольный калькулятор, выбери пункт меню и введи символ.")

    menu = {
        "+":"сложение",
        "-":"вычитание",
        "*":"умножение",
        "/":"деление",
        "q":"выход"
    }
 
    while True:
        for key in menu.items():
            print(f"{key}")

        menu_choice = input("Ваш выбор: ")

        if menu_choice == "q":
            print("Выход")
            break
        elif menu_choice == "+":
            print("Сложение чисел:")
            add(a, b)


if __name__ == "__main__":
    main()
