from tkinter import *

class Interface:
    def __init__(self, title, min_size_x, min_size_y, logo_path, background_color):
        self.title = title
        self.window = Tk()
        self.window.title(self.title)
        self.window.minsize(min_size_x, min_size_y)
        self.window.iconbitmap(logo_path)
        self.window.configure(bg=background_color)
        self.frame = Frame(self.window, bg=background_color)
        self.frame.pack(expand=True)

    def run(self):
        self.window.mainloop()

    def add_title(self, text, text_color):
        title_label = Label(self.frame, text=text, bg=self.frame.cget("bg"), fg=text_color, font=("Comfortaa", 40))
        title_label.pack()

    def add_subtitle(self, text, text_color):
        subtitle_label = Label(self.frame, text=text, bg=self.frame.cget("bg"), fg=text_color, font=("Comfortaa", 20))
        subtitle_label.pack()

    def add_button(self, text, command, text_color, bg_color):
        button = Button(self.frame, text=text, command=command, fg=text_color, bg=bg_color, font=("Comfortaa", 15))
        button.pack(pady=25, fill=X, ipadx=10, ipady=10)
