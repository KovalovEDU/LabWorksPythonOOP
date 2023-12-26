import tkinter
from tkinter import messagebox

class CalculatorWithPrimeCounter(tkinter.Frame):
    """Graphical user interface and logic for counting prime numbers in a set"""

    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tkinter.BOTH, expand=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Labels and Entry widgets for prime counting
        self.lb5 = tkinter.Label(self, text="Enter 10 numbers (space-separated):")
        self.numbers_entry = tkinter.Entry(self)
        self.btn_count_primes = tkinter.Button(self, text="Count Primes", command=self.count_primes)
        self.result_label = tkinter.Label(self, text="Prime Count:")
        self.result_str = tkinter.StringVar()
        self.result_label_prime_count = tkinter.Label(self, textvariable=self.result_str)

        self.lb5.grid(row=4, column=0, sticky=tkinter.NSEW)
        self.numbers_entry.grid(row=4, column=1, sticky=tkinter.NSEW)
        self.btn_count_primes.grid(row=5, column=0, columnspan=2, sticky=tkinter.NSEW)
        self.result_label.grid(row=6, column=0, columnspan=2, sticky=tkinter.NSEW)
        self.result_label_prime_count.grid(row=7, column=0, columnspan=2, sticky=tkinter.NSEW)

    def count_primes(self):
        try:
            numbers = [int(x.strip()) for x in self.numbers_entry.get().split()]
            if len(numbers) == 10:
                prime_count = sum(self.is_prime(num) for num in numbers)
                self.result_str.set(prime_count)
            else:
                messagebox.showerror("Input Error", "Please enter exactly 10 integers separated by spaces")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter 10 valid integers separated by spaces")

    def is_prime(self, n):
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

