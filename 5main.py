# Підключення створенних вікон
import tkinter
from task1 import CalculatorWithPrimeCounter
from task2 import Task2Window

# словник для швидкого доступу до відповідної функції виконання
task_window_dict = {
    "1": (CalculatorWithPrimeCounter, "Lab5_1-312st-v13-Kovalyov-Oleg", "300x150"),
    "2": (Task2Window, "Lab5_2-312st-v11-Kovalyov-Oleg", "900x300")
}


# Основна функція
def main():
    choice = input("Please, choose the task 1-2 (0-EXIT): ")
    while choice != "0":
        # якщо даний ключ є у словнику
        if choice in task_window_dict.keys():
            # Створення відповідного вікна
            application = tkinter.Tk()
            window_class, window_name, window_size = task_window_dict.get(choice)
            window = window_class(application)
            application.geometry(window_size)
            application.title(window_name)
            application.mainloop()
        else:
            print("Wrong task number!")
        choice = input("Please, choose the task again (0-EXIT): ")


if __name__ == '__main__':
    main()