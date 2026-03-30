# Неделя 4, День 1 — Практика: классы и объекты

# %%

# Задание 1
# Создай класс Book с __init__(title, author).
# Сохрани значения в self.title и self.author.
# Затем создай объект и выведи оба атрибута.

class Book:
     def __init__(self, title, author):
            self.title = title
            self.author = author

book_1 = Book("Чебурнет", "Л.Н. Толстой")
print(book_1.title, book_1.author)




# Задание 2
# Создай класс BugReport с полями summary и severity.
# Создай два объекта с разными значениями.
# Выведи severity второго объекта.

class BugReport:
      def __init__(self, summary, severity):
            self.summary = summary
            self.severity = severity

bug_front_01 = BugReport("Все не работает!", "front")
bug_back_01 = BugReport("Все работает!", "back")

print(bug_back_01.severity)



# Задание 3
# Создай класс UserAccount с полями username и is_active.
# После создания объекта измени is_active на False и выведи значение.

class UserAccount:
      def __init__(self, username, is_active):
            self.username = username
            self.is_active = is_active

useraccount_01 = UserAccount("Anna", True)
useraccount_01.is_active = False
print(useraccount_01.is_active)

# Задание 4
# Создай класс Product с полями name и price.
# Создай список из двух объектов Product и выведи name каждого объекта в цикле.

class Product:
      def __init__(self, name, price):
            self.name = name
            self.price = price

products = [Product("Сало", 100), Product("Хлеб", 50)]

for product in products:
      print(product.name)


# Дополнительный проект недели
# В конце Week 4 есть отдельный сквозной проект `Зоопарк`.
# Он лежит в ../bonus_project_zoo/ и рассчитан на несколько дней темы ООП.


# %%
