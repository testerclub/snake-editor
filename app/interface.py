from tkinter import *
from tkinter import ttk


class GUI(Tk):

    def __init__(self, size, win_title, res_state) -> None:
        super().__init__()
        self.geometry(size)
        self.title(win_title)
        self.resisable(res_state)
    
    def create_elements(self):
        pass
