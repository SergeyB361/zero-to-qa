# День 7 — Мини-проект: калькулятор


def add(a, b):
    return round((a+b), 2)


def sub(a, b):
    return round((a-b), 2)


def mul(a, b):
    return round((a*b), 2)


def div(a, b):
    return round((a/b), 2) if b !=0 else "Division by zero"


def read_number(prompt):
    while True:
        try:
            input_number = float(input(f"{prompt} = "))
            return input_number
        except ValueError:
            print("Это не число!")
    
def main():
    print("Консольный калькулятор, выбери пункт меню и введи символ.")

    menu = {
        "+": "сложение",
        "-": "вычитание",
        "*": "умножение",
        "/": "деление",
        "q": "выход"
    }
 
    while True:
        a = b = 0.0
        for key, value in menu.items():
            print(f"{key} {value}")

        menu_choice = input("Ваш выбор: ")

        if menu_choice == "q":
            print("Выход")
            break

        elif menu_choice == "+":
            a = read_number("Введите первое число:")
            b = read_number("Введите второе число")
            print(f"Результат: {add(a, b)}")

        elif menu_choice == "-":
            a = read_number("Введите первое число:")
            b = read_number("Введите второе число")
            print(f"Результат: {sub(a, b)}")

        elif menu_choice == "*":
            a = read_number("Введите первое число:")
            b = read_number("Введите второе число")
            print(f"Результат: {mul(a, b)}")

        elif menu_choice == "/":
            a = read_number("Введите первое число:")
            b = read_number("Введите второе число")
            print(f"Результат: {div(a, b)}")    
        else: 
            print("Unknown operation")      



if __name__ == "__main__":
    main()
