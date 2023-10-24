import math
def if24():
    # Введення трьох чисел
    x = float(input("Введіть перше число: "))
    if x>0:
        f_x=2*math.sin(x)
    else:
        f_x=6-x
    print(f"f(x) при x {x} = {f_x}")

def task2():
    it=0
    a=int(input("Введіть a: "))
    b = int(input("Введіть b: "))
    r=int(input("Введіть r: "))
    n =int(input("Введіть кількість точок: "))
    for i in range(n):
        print(f"Введіть координати точки {i + 1}:")
        x = float(input("x: "))  # Введення координати x
        y = float(input("y: "))  # Введення координати y
        if (x-(b/2))**2+(y-r)**2<r*r and x>(b/2):
            it=it+1
        elif (x-(b/2))**2+(y-r)**2>r*r and y<a and x>0 and y>0:
            it = it + 1

    print(f"Точок потрапляє у фігуру:{it}")

def task16():
    E = 1e-5  # Мала величина для збіжності
    G = 1e5  # Велика величина для розбіжності
    current_sum = 0
    n = 1  # Починаємо з n = 1
    u = 1  # Ініціалізуємо `u` значенням 1 перед використанням

    while abs(u) >= E and abs(u) <= G:
        u = (n**3 * math.exp(2 * n + 1)) / math.factorial(n)
        current_sum += u
        print(u)
        n += 1

    if abs(u) < E:
        print("Сума сходиться до заданої точності.")
    elif abs(u) > G:
        print("Ряд розходиться.")

if __name__ == "__main__":
    while True:
        print("\nОберіть опцію:")
        print("1. Визначити корінь рівняння")
        print("2. Попадання в фігуру")
        print("3. Дослідження ряду на збіжність ")
        print("0. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            if24()
        elif choice == "2":
            task2()
        elif choice == "3":
            task16()
        elif choice == "0":
            break
        else:
            print("Невірний вибір. Виберіть 1, 2, 3 або 0.")