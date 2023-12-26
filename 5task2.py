import tkinter
from tkinter import messagebox
from tkinter.filedialog import askopenfile
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from PIL import Image, ImageTk


class Task2Window(tkinter.Frame):
    """Класс MainWindow, наследующий Frame"""

    def __init__(self, parent):
        """Настройка графического интерфейса"""
        super().__init__(parent)
        self.pack(fill=tkinter.BOTH, expand=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

        self.img = ImageTk.PhotoImage(file='image.png')
        self.lb_image = tkinter.Label(self, image=self.img)
        self.lb1 = tkinter.Label(self, text="N = ")
        self.N_entr = tkinter.Entry(self)

        self.but1 = tkinter.Button(self, text="Create file", command=self.create_file)
        self.but2 = tkinter.Button(self, text="Open file", command=self.open_file)
        self.but3 = tkinter.Button(self, text="Show content", command=self.show_msg)
        self.but4 = tkinter.Button(self, text="Show plot", command=self.show_plot)

        self.lb_image.grid(row=0, column=0, columnspan=2, sticky=tkinter.NSEW)
        self.lb1.grid(row=0, column=2, sticky=tkinter.NSEW)
        self.N_entr.grid(row=0, column=3, sticky=tkinter.NSEW)
        self.but1.grid(row=1, column=0, sticky=tkinter.NSEW)
        self.but2.grid(row=1, column=1, sticky=tkinter.NSEW)
        self.but3.grid(row=1, column=2, sticky=tkinter.NSEW)
        self.but4.grid(row=1, column=3, sticky=tkinter.NSEW)
        self.text1 = ""  # содержимое файла

    def create_file(self):
        """Расчет значений функции и сохранение результатов в файл"""
        try:
            N = int(self.N_entr.get())
            if N < 20:
                raise ValueError
        except ValueError:
            messagebox.showerror("Data ERROR", "N must be an integer that is >= 20!")
        else:
            K = 1.5
            T = 1
            T0 = 2 * T / N
            U = 0.1
            eps = 0.1
            x = [0]
            y = [0]

            for k in range(1, N):
                x.append(k * T0)
                tmp_value = (2 - ((2 * eps * T0) / T)) * y[k - 1] + \
                            (((2 * eps * T0) / T) - 1 - ((T0 * T0) / (T * T))) * y[k - 2] + \
                            ((K * T0 ** 2) / T ** 2) * U
                y.append(tmp_value)

            with open("graph_data.txt", 'w') as f:
                for i, x_val in enumerate(x):
                    f.write("{}#{}\n".format(x_val, y[i]))

            messagebox.showinfo("File creation", "File with data was created!")

    def open_file(self):
        """Чтение содержимого файла и сохранение в text1"""
        fopen = askopenfile(mode='r', defaultextension=".txt",
                            filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if fopen is None:
            return
        self.text1 = fopen.readlines()
        messagebox.showinfo("File opening", "File with data was opened!")

    def show_msg(self):
        """Отобразить text1 в окне messagebox"""
        messagebox.showinfo("File content", self.text1)

    def show_plot(self):
        """Построение графика функции"""
        x = []
        y = []
        try:
            for line in self.text1:
                words = line.split('#')
                x.append(float(words[0]))
                y.append(float(words[1]))
        except ValueError:
            messagebox.showerror("Data ERROR", "Wrong file format!")
        else:
            fig = Figure(figsize=(5, 4))
            a = fig.add_subplot(111)
            a.plot(x, y, 'c--')
            a.set_xlabel('X')
            a.set_ylabel('Y')
            a.set_title('Graph')
            drawing = FigureCanvasTkAgg(fig, master=self)
            drawing.get_tk_widget().grid(row=2, column=0, columnspan=4, sticky=tkinter.NSEW)
            drawing.draw()

            min_x = min(x)
            min_y = min(y)
            max_x = max(x)
            max_y = max(y)
            messagebox.showinfo("Basic information", "X min = {}, X max = {}\n"
                                                     "Y min = {}, Y max = {}".format(min_x, max_x, min_y, max_y))



