import math
def task1():
    """
    Функція для перестановки місцями цифр у двозначному числі
    """
    try:
        number = int(input("Введіть двозначне число: "))
        if 10 <= number <= 99:
            digit1 = number // 10
            digit2 = number % 10
            reversed_number = digit2 * 10 + digit1
            print("Результат перестановки цифр:", reversed_number)
        else:
            print("Введене число не є двозначним.")
    except ValueError:
        print("Помилка: Введіть дійсне ціле число.")

def task2():
    """
    Функція для розрахунку прикладу.
    """
    try:
        x = float(input("Введіть x: "))
        num = math.exp(x+1)*math.sqrt(math.fabs(2*x-math.cos(x+(33*(math.pi/180)))-25))
        denum =math.cbrt(math.sin(x*x))*math.log(math.fabs(x**2),5)

        if denum == 0:
            print("Ділення на нуль неможливе.")
        else:
            y = num / denum
            print(f"Значення y при x={x}: {y}")
    except ValueError:
        print("Помилка: Введіть коректне числове значення для x.")
    except ZeroDivisionError:
        print("Помилка: Ділення на нуль неможливе.")


def task3():
    """
    Функція для перевірки істинності висловлювання «Існує
трикутник зі сторонами a, b, c»..
    """
    try:
        a = int(input("Введіть число a: "))
        b = int(input("Введіть число b: "))
        c = int(input("Введіть число c: "))

        is_positive = a + b > c and a + c > b and b + c > a

        print(is_positive)
    except ValueError:
        print("Помилка:Введіть ціле число для a, b та c.")


if __name__ == "__main__":
    while True:
        print("\nОберіть опцію:")
        print("1. Вивести число з переставленими числами")
        print("2. Обрахувати приклад")
        print("3. Перевірити істинність висловлювання")
        print("0. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            task1()
        elif choice == "2":
            task2()
        elif choice == "3":
            task3()
        elif choice == "0":
            break
        else:
            print("Невірний вибір. Виберіть 1, 2, 3 або 0.")