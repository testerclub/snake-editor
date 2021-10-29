from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory, test
from info import *


def ask_new_file_name():
    window = Tk()
    window.configure(bg=gui_bg_color)
    window.title("New...")
    window.geometry("250x100")
    window.resizable(False, False)
    name = Entry(window, bg=gui_text_editor_bg_color, fg='white')
    name.place(relx=.1, rely=.1, relwidth=.8)
    ok = Button(window, text="OK", bg='#222222', fg='white')
    ok.bind("<Enter>", lambda event: ok.configure(bg='gray'))
    ok.bind("<Leave>", lambda event: ok.configure(bg='#222222'))
    ok.place(relx=.1, rely=.5, relwidth=.8)
    return {'filename': name, 'button': ok, 'window': window}


class Main(Tk):

    def __init__(self, min_size, win_title) -> None:
        super().__init__()
        self.minsize(*min_size)
        self.configure(bg=gui_bg_color)
        self.title(win_title)
        self.open = None
        self.save = None
        self.new = None
        self.code = None
        self.exit = None
        self.credits = None

    def create_top_bar(self):
        self.open = Button(self, text="I", font=("Aquawax Pro Pictograms", 30),
                            bg='#222222', fg='white')
        self.open.bind("<Enter>", lambda event: self.open.configure(bg='gray'))
        self.open.bind("<Leave>", lambda event: self.open.configure(bg='#222222'))
        self.open.place(relx=0, relwidth=.07, relheight=.07)

        self.save = Button(self, text="H", font=("Aquawax Pro Pictograms", 30),
                            bg='#222222', fg='white')
        self.save.bind("<Enter>", lambda event: self.save.configure(bg='gray'))
        self.save.bind("<Leave>", lambda event: self.save.configure(bg='#222222'))
        self.save.place(relx=.07, relwidth=.07, relheight=.07)

        self.new = Button(self, text="New File", font=("Consolas", 15),
                            bg='#222222', fg='white')
        self.new.bind("<Enter>", lambda event: self.new.configure(bg='gray'))
        self.new.bind("<Leave>", lambda event: self.new.configure(bg='#222222'))
        self.new.place(relx=.14, relwidth=.21, relheight=.07)

        self.credits = Button(self, text="y", font=("Aquawax Pro Pictograms", 30),
                            bg='#222222', fg='white')
        self.credits.bind("<Enter>", lambda event: self.credits.configure(bg='gray'))
        self.credits.bind("<Leave>", lambda event: self.credits.configure(bg='#222222'))
        self.credits.place(relx=.86, relwidth=.07, relheight=.07)

        self.exit = Button(self, text="X", font=("Aquawax Pro Pictograms", 30),
                            bg='#222222', fg='white', command=self.destroy)
        self.exit.bind("<Enter>", lambda event: self.exit.configure(bg='gray'))
        self.exit.bind("<Leave>", lambda event: self.exit.configure(bg='#222222'))
        self.exit.place(relx=.93, relwidth=.07, relheight=.07)

    def create_text_editor(self):
        self.code = Text(self, bg=gui_text_editor_bg_color, fg='white', insertbackground='white',
                            undo=True, font=gui_text_editor_font)
        self.code.insert(INSERT, start_msg)
        self.code.place(rely=.07, relwidth=1, relheight=.9)


class Credits(Tk):

    def __init__(self) -> None:
        super().__init__()
        self.configure(bg=gui_bg_color)
        self.geometry("500x300")
        self.resizable(False, False)
        self.title("Snake Editor - Credits")
        self.exit = None

    def create_elements(self):
        text = Text(self, bg="#111111", fg='white', insertbackground='white',
                        undo=True)
        text.place(relheight=1, relwidth=1)
        text.insert(INSERT, credits_msg)
        self.exit = Button(self, text="X", font=("Aquawax Pro Pictograms", 30),
                            bg='#222222', fg='white', command=self.destroy)
        self.exit.bind("<Enter>", lambda event: self.exit.configure(bg='gray'))
        self.exit.bind("<Leave>", lambda event: self.exit.configure(bg='#222222'))
        self.exit.place(relx=.85, rely=.85, relwidth=.15, relheight=.15)
