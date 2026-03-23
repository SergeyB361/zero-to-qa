# Дополнительное задание — Зоопарк
#
# Задача:
# Создай систему управления зоопарком, используя все базовые принципы ООП.
#
# Что нужно сделать:
#
#
# Шаг 3 — Полиморфизм
# Переопредели метод play() в каждом классе:
# - Лев — "Симба охотится" и энергия -40
# - Попугай — "Кеша летает" и энергия -20
# - Черепаха — "Тортилла ползает" и энергия -10
#
# Шаг 4 — Зоопарк
# Создай класс Zoo с:
# - список животных
# - метод add_animal(animal) — добавить животное
# - метод feed_all() — покормить всех
# - метод show_all() — показать статус всех животных
#
# Пример результата:
# === Зоопарк ===
# Симба (Лев) — энергия: 50
# Кеша (Попугай) — энергия: 80
# Тортилла (Черепаха) — энергия: 70
#
# Кормим всех...
# Симба (Лев) — энергия: 70
# Кеша (Попугай) — энергия: 100
# Тортилла (Черепаха) — энергия: 90
#
# Симба охотится!
# Симба (Лев) — энергия: 30
#
# Кеша говорит: я красавчик!
#
# Подсказки:
# - __energy — приватное свойство
# - Lion, Parrot, Turtle наследуют Animal
# - play() работает по-разному у каждого класса
# - Zoo.feed_all() вызывает eat() у всех животных и не зависит от их типа


# Шаг 1 — Базовый класс
# Создай класс Animal с:
# - свойства: name, species, __energy (приватное, от 0 до 100)
# - метод eat() — увеличивает энергию на 20, но не больше 100
# - метод play() — уменьшает энергию на 30, но не меньше 0
# - метод status() — выводит имя и текущую энергию

class Animal:
    def __init__(self, name, species, energy):
        self.name = name
        self.species = species
        self.__energy = energy

    def eat(self):
        self.__energy += 20
        if self.__energy > 100:
            self.__energy = 100
        return self.__energy

    def play(self):
        self.__energy += -30
        if self.__energy < 0:
            self.__energy = 0
        return self.__energy

    def status(self):
        return print(f"Имя:{self.name} Энергия:{self.__energy}")
    
parrot = Animal("Rici", "parrot", 10)
print(parrot.eat())
print(parrot.play())
parrot.status()
#
# Шаг 2 — Наследование
# Создай 3 дочерних класса:
# - Lion(Animal) — добавь метод roar() -> "Симба рычит!"
# - Parrot(Animal) — добавь метод talk(phrase) -> "Кеша говорит: привет!"
# - Turtle(Animal) — добавь метод hide() -> "Тортилла прячется в панцирь"


class Lion(Animal):
    def __init__(self, name, species, energy):
        super().__init__(name, species, energy)

    def roar():
        return Print("Симба рычит!")


class Parrot(Animal):
    def __init__(self, name, species, energy):
        super().__init__(name, species, energy)

    def talk(phrase):
        return print("Кеша говорит: привет!")

class Turtle(Animal):
    def __init__(self, name, species, energy):
        super().__init__(name, species, energy)
    
    def hide():
        return print("Тортилла прячется в панцирь")


class Zoo:
    pass


if __name__ == '__main__':
    print('Реализуй проект по комментариям в этом файле.')
