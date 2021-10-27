from tkinter import *
from tkinter import messagebox
from info import *

def show_font_message():
    from tkinter.messagebox import showinfo
    showinfo(title="Font Warning", message=
    "This app requires the installation of a font to improve viewing. Please download and install it by following the link below:\n\nhttps://github.com/marc-dantas/snake-editor/blob/main/app/resources/font/Aquawax-Pro-Pictograms-Regular.ttf?raw=true")

class Main(Tk):

    def __init__(self, min_size, win_title) -> None:
        super().__init__()
        self.minsize(*min_size)
        self.iconbitmap("./resources/winicon.ico")
        self.configure(bg=gui_bg_color)
        self.title(win_title)
        self.open = None
        self.save = None
        self.settings = None
        self.code = None
        self.run = None
        self.mainmenu = None
        self.filemenu = None
        self.aboutmenu = None

    def create_top_bar(self):
        self.open = Button(self, text="I", font=("Aquawax Pro Pictograms", 30),
                            bg='#222222', fg='white')
        self.open.bind("<Enter>", lambda event: self.open.configure(bg='gray'))
        self.open.bind("<Leave>", lambda event: self.open.configure(bg='#222222'))
        self.open.place(relx=0, relwidth=.1, relheight=.1)

        self.save = Button(self, text="H", font=("Aquawax Pro Pictograms", 30),
                            bg='#222222', fg='white')
        self.save.bind("<Enter>", lambda event: self.save.configure(bg='gray'))
        self.save.bind("<Leave>", lambda event: self.save.configure(bg='#222222'))
        self.save.place(relx=.1, relwidth=.1, relheight=.1)

        self.run = Button(self, text="X", font=("Aquawax Pro Pictograms", 30),
                            bg='#222222', fg='white', command=self.destroy)
        self.run.bind("<Enter>", lambda event: self.run.configure(bg='gray'))
        self.run.bind("<Leave>", lambda event: self.run.configure(bg='#222222'))
        self.run.place(relx=.9, relwidth=.1, relheight=.1)

    def create_text_editor(self):
        self.code = Text(self, bg=gui_text_editor_bg_color, fg='white', insertbackground='white',
                            undo=True, font=gui_text_editor_font)
        self.code.insert(INSERT, start_msg)
        self.code.place(rely=.1, relwidth=1, relheight=1)


class Credits(Tk):

    def __init__(self) -> None:
        super().__init__()
        self.iconbitmap("./resources/winicon.ico")
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
