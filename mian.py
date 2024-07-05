import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt


class DataExplorer:
    def __init__(self, rt):
        self.root = rt
        self.root.title("Data Explorer")
        self.df = None

        # screen size
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        # a frame for main title and upload
        self.menu_frame = tk.Frame(self.root, bg="light blue")
        self.menu_frame.place(x=0, y=0, height=60, width=screen_width)

        # label for upload button
        self.main_title = tk.Label(self.menu_frame, text="Upload a CSV file to explore",
                                   fg="black", bg='light blue', font=("Arial", 20, "bold"))
        self.main_title.grid(row=0, column=0, padx=50, pady=10)

        # File uploader button
        self.upload_button = tk.Button(self.menu_frame, text="Upload File",
                                       command=self.upload_file,
                                       bg="black", fg="white",
                                       font=("Arial", 12, "bold"))
        self.upload_button.grid(row=0, column=10)

        # label for summary
        self.summary_label = tk.Label(self.root, text="Summary of data", font=("Arial", 15, "bold"))
        self.summary_label.place(y=60)

        # a frame for summary of data
        self.summary_frame = tk.Frame(self.root, bg="light gray", bd=5, relief="groove")
        self.summary_frame.place(y=90, width=screen_width)

        # Summary statistics
        self.summary_text = tk.Text(self.summary_frame)
        self.summary_text.pack(fill="x")

        # A frame for options
        self.options_frame = tk.Frame(self.root, bg="light blue")
        self.options_frame.place(y=500, width=screen_width, height=50)

        # label for options
        self.chose_plot = tk.Label(self.options_frame, text="Chose:",
                                   font=("Arial", 11, "bold"))
        self.chose_plot.grid(row=0, column=0, padx=20, pady=13)

        # Plot options
        self.plot_var = tk.StringVar()
        self.plot_var.set("Histogram")
        self.plot_menu = tk.OptionMenu(self.options_frame, self.plot_var, "Histogram",
                                       "Scatter Plot", "Bar Chart")
        self.plot_menu.grid(row=0, column=1, padx=20)

        self.column_var = tk.StringVar()
        self.column_var.set("")
        self.column_menu = tk.OptionMenu(self.options_frame, self.column_var, "")
        self.column_menu.grid(row=0, column=2, padx=20)

        self.column_var2 = tk.StringVar()
        self.column_var2.set("")
        self.column_menu2 = tk.OptionMenu(self.options_frame, self.column_var2, "")
        self.column_menu2.grid(row=0, column=3, padx=20)

        # plot button
        self.plot_button = tk.Button(self.options_frame, text="Plot Data", command=self.plot_data)
        self.plot_button.grid(row=0, column=4, padx=20)

    def upload_file(self):
        file_path = filedialog.askopenfilename()
        self.df = pd.read_csv(file_path)
        self.summary_text.insert(tk.INSERT, str(self.df.describe()))
        self.update_plot_options()

    def update_plot_options(self):
        columns = list(self.df.columns)
        self.column_var.set(columns[0])
        self.column_menu['menu'].delete(0, 'end')
        for column in columns:
            self.column_menu['menu'].add_command(label=column,
                                                 command=tk._setit(self.column_var, column))

        self.column_var2.set(columns[0])
        self.column_menu2['menu'].delete(0, 'end')
        for column in columns:
            self.column_menu2['menu'].add_command(label=column, command= tk._setit(
                self.column_var2, column))

    def plot_data(self):
        plot_type = self.plot_var.get()
        if plot_type == "Histogram":
            plt.hist(self.df[self.column_var.get()])
        elif plot_type == "Scatter Plot":
            plt.scatter(self.df[self.column_var.get()], self.df[self.column_var2.get()])
        elif plot_type == "Bar Chart":
            plt.bar(self.df[self.column_var.get()], self.df[self.column_var2.get()])
        plt.show()


root_window = tk.Tk()
data_explorer = DataExplorer(root_window)
root_window.mainloop()
