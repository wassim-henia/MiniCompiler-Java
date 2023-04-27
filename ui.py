import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor:
    def __init__(self, master):
        self.master = master
        master.title("Text Editor")

        # Create a frame to hold the line numbers and text widget
        self.frame = tk.Frame(master)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Create a canvas to hold the line numbers
        self.line_number_canvas = tk.Canvas(self.frame, width=50, highlightthickness=0)
        self.line_number_canvas.pack(side=tk.LEFT, fill=tk.Y)

        # Create a text widget for the editor
        self.text_widget = tk.Text(self.frame, wrap=tk.NONE)
        self.text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.text_widget.bind("<Key>", self.on_key_press)
        self.text_widget.bind("<Button-1>", self.on_click)
        self.text_widget.bind("<MouseWheel>", self.on_mousewheel)

        # Create a scrollbar for the text widget
        self.scrollbar = tk.Scrollbar(self.frame, command=self.text_widget.yview)
        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        self.text_widget.config(yscrollcommand=self.scrollbar.set)

        # Create a frame to hold the output text widget and separator
        self.bottom_frame = tk.Frame(master, height=100)
        self.bottom_frame.pack(fill=tk.BOTH, expand=True)

        # Create a label for the output text widget
        self.output_label = tk.Label(self.bottom_frame, text="Output")
        self.output_label.pack(side=tk.TOP)

        # Create a separator between the editor and the output widget
        self.separator = tk.Frame(self.bottom_frame, height=2, bd=1, relief=tk.SUNKEN)
        self.separator.pack(side=tk.TOP, fill=tk.X)

        # Create a text widget for the output
        self.output_text_widget = tk.Text(self.bottom_frame, wrap=tk.NONE, height=15)
        self.output_text_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.output_text_widget.config(state=tk.DISABLED)

        # Create a menu bar
        self.menu_bar = tk.Menu(master)
        master.config(menu=self.menu_bar)

        # Create a "File" menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.master.quit)

        # Create a "Run" menu
        self.run_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Run", menu=self.run_menu)
        self.run_menu.add_command(label="Compile", command=self.compile_file)

        # Initialize the line numbers
        self.line_number_widget = tk.Text(self.line_number_canvas, width=3, padx=3, pady=3, highlightthickness=0)
        self.line_number_widget.pack(side=tk.LEFT, fill=tk.Y)
        self.line_number_widget.config(state=tk.DISABLED)

        # Set the font and line spacing for
        self.line_number_widget = tk.Text(self.line_number_canvas, width=3, padx=3, pady=3, highlightthickness=0)
        self.line_number_widget.pack(side=tk.LEFT, fill=tk.Y)
        self.line_number_widget.config(state=tk.DISABLED)

        # Set the font and line spacing for the editor and line numbers
        self.font = ("Consolas", 12)
        self.text_widget.config(font=self.font)
        self.line_number_widget.config(font=self.font)
        self.text_widget.config(spacing1=3)
        self.line_number_widget.config(spacing1=3)

        # Keep track of the current file path
        self.file_path = None

        # Set up the initial line numbers
        self.update_line_numbers()
    
    def on_click(self, event):
        self.update_line_numbers()

    def on_mousewheel(self, event):
        self.text_widget.yview_scroll(int(-1 * (event.delta / 120)), "units")


    def new_file(self):
        self.text_widget.delete("1.0", tk.END)
        self.file_path = None
        self.update_line_numbers()

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_widget.delete("1.0", tk.END)
                self.text_widget.insert("1.0", content)
                self.file_path = file_path
                self.update_line_numbers()

    def save_file(self):
        if self.file_path:
            content = self.text_widget.get("1.0", tk.END)
            with open(self.file_path, "w") as file:
                file.write(content)
        else:
            self.save_file_as()

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            content = self.text_widget.get("1.0", tk.END)
            with open(file_path, "w") as file:
                file.write(content)
            self.file_path = file_path
            self.update_line_numbers()

    def compile_file(self):
        content = self.text_widget.get("1.0", tk.END)
        if self.file_path:
            file_name = self.file_path.split("/")[-1]
        else:
            file_name = "temp.java"
        with open(file_name, "w") as file:
            file.write(content)
        result = subprocess.getoutput(f"cd MiniCompiler && ./miniJava < {file_name}")
        print(result)
        self.output_text_widget.config(state=tk.NORMAL)
        self.output_text_widget.delete("1.0", tk.END)
        self.output_text_widget.insert(tk.END, result)
        self.output_text_widget.config(state=tk.DISABLED)

    def update_line_numbers(self):
        lines = str(self.text_widget.get("1.0", tk.END)).count("\n")
        self.line_number_widget.config(state=tk.NORMAL)
        self.line_number_widget.delete("1.0", tk.END)
        for i in range(1, lines + 1):
            self.line_number_widget.insert(tk.END, str(i) + "\n")
        self.line_number_widget.config(state=tk.DISABLED)

    def on_key_press(self, event):
        if event.keysym == "BackSpace" or event.keysym == "Delete":
            self.update_line_numbers()
        elif event.keysym == "Return":
            self.update_line_numbers()
            self.text_widget.see(tk.END)
    
root = tk.Tk()
editor = TextEditor(root)
root.mainloop()
