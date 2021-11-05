from tkinter import Widget, font
from tkinter.filedialog import askdirectory, askopenfilename
from tkinter.messagebox import showerror, showinfo
from idlelib.colorizer import ColorDelegator
from idlelib.percolator import Percolator
from info import syntax_colors
from tkinter.font import Font
import re

local_path = ''
insert_indent = lambda x: x.widget.insert('insert', '    ')

def open_file(root):
    global local_path
    filename = askopenfilename()
    if filename != '':
        with open(f'{filename}', 'r', encoding='utf-8') as file:
            file.seek(0, 0)
            content = file.read()
        root.code.delete(0.0, 'end')
        root.code.insert('insert', content)
        local_path = filename
        showinfo("Information", "File opened successfully!")
        return content
    else:
        showerror("Error", "You have not selected any files. Please try again.")
        open_file(root)


def save_file(root):
    global local_path
    if local_path != '':
        file_changes = root.code.get(0.0, 'end')
        with open(f'{local_path}', 'w') as file:
            file.write(file_changes)
        showinfo("Information", "File saved successfully!")
    else:
        showerror("Error", "To be able to save a file, you must first open one.")


def highlight_syntax(root):
    color_filter = ColorDelegator()
    color_filter.tagdefs['COMMENT'] = syntax_colors['COMMENT']
    color_filter.tagdefs['KEYWORD'] = syntax_colors['KEYWORD']
    color_filter.tagdefs['BUILTIN'] = syntax_colors['BUILTIN']
    color_filter.tagdefs['STRING'] = syntax_colors['STRING']
    color_filter.tagdefs['DEFINITION'] = syntax_colors['DEFINITION']
    Percolator(root.code).insertfilter(color_filter)
    return color_filter
