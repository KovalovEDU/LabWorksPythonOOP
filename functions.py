import math


def if24():
    """Необхідно додавати опис завдання у строку документації"""
    # Введення трьох чисел
    try:
        x = float(input("Введіть перше число: "))
    except ValueError:
        print("Wrong input!")
    else:
        if x > 0:
            f_x = 2 * math.sin(x)
        else:
            f_x = 6 - x
        print(f"f(x) при x {x} = {f_x}")


def task2():
    it = 0
    try:
        a = int(input("Введіть a: "))
        b = int(input("Введіть b: "))
        r = int(input("Введіть r: "))
        n = int(input("Введіть кількість точок: "))
    except ValueError:
        print("Wrong input!")
    else:
        for i in range(n):
            print(f"Введіть координати точки {i + 1}:")
            try:
                x = float(input("x: "))  # Введення координати x
                y = float(input("y: "))  # Введення координати y
            except ValueError:
                print("X, Y must be float")
            else:
                if (x - (b / 2)) ** 2 + (y - r) ** 2 < r * r and x > (b / 2):
                    it = it + 1
                elif (x - (b / 2)) ** 2 + (y - r) ** 2 > r * r and y < a and x > 0 and y > 0:
                    it = it + 1

        print(f"Точок потрапляє у фігуру:{it}")


def task16():
    E = 1e-5  # Мала величина для збіжності
    G = 1e5  # Велика величина для розбіжності
    current_sum = 0
    n = 1  # Починаємо з n = 1
    u = 1  # Ініціалізуємо `u` значенням 1 перед використанням

    while abs(u) >= E and abs(u) <= G:
        u = (n ** 3 * math.exp(2 * n + 1)) / math.factorial(n)
        current_sum += u
        print(u)
        n += 1

    if abs(u) < E:
        print("Сума сходиться до заданої точності.")
    elif abs(u) > G:
        print("Ряд розходиться.")