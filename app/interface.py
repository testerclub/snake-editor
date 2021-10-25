from tkinter import *
from tkinter.messagebox import *
from info import min_size, gui_title

class Main(Tk):

    def __init__(self, min_size, win_title) -> None:
        super().__init__()
        self.minsize(*min_size)
        self.configure(bg="#444444")
        self.title(win_title)
        self.open = None
        self.save = None
        self.settings = None
        self.code = None
        self.run = None

    def make_shortcuts(self):
        self.bind("<Control> <q>", self.destroy)
    
    def create_top_bar(self):
        self.open = Button(self, text="I", font=("Aquawax Pro Pictograms", 30),
                            bg='#222222', fg='white')
        self.open.bind("<Enter>", lambda x: self.open.configure(bg='gray'))
        self.open.bind("<Leave>", lambda x: self.open.configure(bg='#222222'))
        self.open.place(relx=0, relwidth=.1, relheight=.1)

        self.save = Button(self, text="H", font=("Aquawax Pro Pictograms", 30),
                            bg='#222222', fg='white')
        self.save.bind("<Enter>", lambda x: self.save.configure(bg='gray'))
        self.save.bind("<Leave>", lambda x: self.save.configure(bg='#222222'))
        self.save.place(relx=.1, relwidth=.1, relheight=.1)

        self.run = Button(self, text="H", font=("Aquawax Pro Pictograms", 30),
                            bg='#222222', fg='white')
        self.run.bind("<Enter>", lambda x: self.run.configure(bg='gray'))
        self.run.bind("<Leave>", lambda x: self.run.configure(bg='#222222'))
        self.run.place(relx=.8, relwidth=.1, relheight=.1)

        self.settings = Button(self, text="r", font=("Aquawax Pro Pictograms", 30),
                            bg='#222222', fg='white')
        self.settings.bind("<Enter>", lambda x: self.settings.configure(bg='gray'))
        self.settings.bind("<Leave>", lambda x: self.settings.configure(bg='#222222'))
        self.settings.place(relx=.9, relwidth=.1, relheight=.1)

    def create_text_editor(self):
        self.code = Text(self, bg="#111111", fg='white')
        self.code.place(rely=.1, relwidth=1, relheight=1)
