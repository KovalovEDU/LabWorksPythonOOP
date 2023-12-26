import random
def AddLeftDigit(D, K):
    return D * 10 + K

def process_input_data(input_data):
    results = []
    for data in input_data:
        D, K = data
        result = AddLeftDigit(D, K)
        results.append(result)
        print(f"Після додавання цифри {D} зліва до числа {K} отримуємо: {result}")
    return results

def proc9():
    input_data = []

    # Введення даних з консолі
    n = int(input("Введіть кількість чисел: "))
    for i in range(n):
        D = int(input(f"Введіть цифру D для числа {i + 1} (1-9): "))
        K = int(input(f"Введіть число K для числа {i + 1} (0 < K < 1000): "))
        input_data.append((D, K))

    results = process_input_data(input_data)

    print("\nРезультати:")
    for result in results:
        print(result)
def process_matrix(filename):
    with open(filename, 'r') as file:
        # Читаємо матрицю з файлу
        matrix = [list(map(int, line.split())) for line in file]

    # Знаходимо мінімальний серед максимальних елементів стовпців
    max_column_values = [max(column) for column in zip(*matrix)]
    min_among_max = min(max_column_values)

    # Відсортовуємо матрицю по рядках по спадаючій
    sorted_matrix = sorted(matrix, key=lambda row: max(row), reverse=True)

    return min_among_max, sorted_matrix
def matrix12():
    filename = 'matrix.txt'

    # Виклик внутрішньої функції
    min_among_max, sorted_matrix = process_matrix(filename)

    # Виведення результатів
    print(f"Мінімальний серед максимальних елементів стовпців: {min_among_max}")
    print("Відсортована матриця по рядках по спадаючій:")
    for row in sorted_matrix:
        print(row)
if __name__ == "__main__":
    while True:
        print("\nОберіть опцію:")
        print("1. Proc 17")
        print("2. Matrix 14")
        print("0. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            proc9()
        elif choice == "2":
            matrix12()
        elif choice == "0":
            break
        else:
            print("Невірний вибір. Виберіть 1, 2, 3 або 0.")
