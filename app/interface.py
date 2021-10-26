from tkinter import *
from tkinter import messagebox
from pygments import *
from tkinter.messagebox import *
from info import min_size, gui_title, __msg__


class Main(Tk):

    def __init__(self, min_size, win_title) -> None:
        super().__init__()
        self.minsize(*min_size)
        self.iconbitmap("./app/resources/winicon.ico")
        self.configure(bg="#444444")
        self.title(win_title)
        self.open = None
        self.save = None
        self.settings = None
        self.code = None
        self.run = None
        self.mainmenu = None
        self.filemenu = None
        self.editmenu = None
        self.aboutmenu = None
    
    def create_menu_bar(self):
        self.mainmenu = Menu(self)
        self.filemenu = Menu(self.mainmenu, tearoff=0)
        self.filemenu.add_command(label="Open")
        self.filemenu.add_command(label="Save")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=exit)
        self.mainmenu.add_cascade(label="File", menu=self.filemenu)

        self.editmenu = Menu(self.mainmenu, tearoff=0)
        self.editmenu.add_command(label="Font...")
        self.editmenu.add_command(label="")
        self.mainmenu.add_cascade(label="Edit", menu=self.editmenu)
        
        self.aboutmenu = Menu(self.mainmenu, tearoff=0)
        self.aboutmenu.add_command(label="Credits")
        self.aboutmenu.add_command(label="About Snake Editor")
        self.mainmenu.add_cascade(label="About", menu=self.aboutmenu)
        
        self.config(menu=self.mainmenu)

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
                            bg='#222222', fg='white', command=exit)
        self.run.bind("<Enter>", lambda event: self.run.configure(bg='gray'))
        self.run.bind("<Leave>", lambda event: self.run.configure(bg='#222222'))
        self.run.place(relx=.8, relwidth=.1, relheight=.1)

        self.settings = Button(self, text="a", font=("Aquawax Pro Pictograms", 30),
                            bg='#222222', fg='white')
        self.settings.bind("<Enter>", lambda event: self.settings.configure(bg='gray'))
        self.settings.bind("<Leave>", lambda event: self.settings.configure(bg='#222222'))
        self.settings.place(relx=.9, relwidth=.1, relheight=.1)

    def create_text_editor(self):
        self.code = Text(self, bg="#111111", fg='white', insertbackground='white',
                            undo=True)
        self.code.insert(INSERT, __msg__)
        self.code.place(rely=.1, relwidth=1, relheight=1)


class Settings(Tk):

    def __init__(self) -> None:
        super().__init__()
        self.iconbitmap("./app/resources/winicon.ico")
        self.configure(bg="#444444")
        self.geometry("500x500")
        self.resizable(False, False)
        self.title("Snake Editor - Settings")
    
    def create_elements(self):
        pass
