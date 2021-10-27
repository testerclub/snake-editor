import re

def autoindent(event):
    widget = event.widget
    line = widget.get("insert linestart", "insert lineend")
    match = re.match(r'^(\s+)', line)
    current_indent = len(match.group(0)) if match else 0
    new_indent = current_indent + 4
    widget.insert("insert", event.char + "\n" + " "*new_indent)
    return "break"