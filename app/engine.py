from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
import re

local_path = r""


def open_file(root):
    global local_path
    filename = askopenfilename()
    with open(f'{filename}', 'r', encoding='utf-8') as file:
        file.seek(0, 0)
        content = file.read()
    root.code.delete(0.0, 'end')
    root.code.insert('insert', content)
    local_path = filename
    showinfo("Information", "File opened successfully!")
    return content


def save_file(root):
    global local_path
    file_changes = root.code.get(0.0, 'end')
    with open(f'{local_path}', 'w') as file:
        file.write(file_changes)
    showinfo("Information", "File saved successfully!")


def auto_indent(event):
    widget = event.widget
    line = widget.get("insert linestart", "insert lineend")
    match = re.match(r'^(\s+)', line)
    current_indent = len(match.group(0)) if match else 0
    new_indent = current_indent + 4
    widget.insert("insert", event.char + "\n " * new_indent)
