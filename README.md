![header](https://user-images.githubusercontent.com/90472141/138929686-ace3d03b-72dc-43cf-a708-d2daf735d647.png)

> ### 🚧WARNING🚧: Beta version... There may be malfunctions and bugs!

# Welcome to Snake Editor!
## Hi! This is our repository, we are here to present our new project.

- Inspired by GNU Emacs, we created our new software. Which has the purpose of being an editor for Python code, we named it *Snake Editor*.

## Technologies used:

- Tkinter (Python Lib)
- Python 3.10
- GitHub Desktop (Git Version Control)

## Authors:
- [Kmsz](https://github.com/Kamaasoo)
- [Marcio Dantas](https://github.com/marc-dantas)

## Prerequisites for use:
- If you're on a linux distribution, make sure IDLE is installed, if you are unsure run the command `sudo apt install idle-python3.9` in your terminal to get syntax highlighting to work. Same for MAC OS users.
- This program uses a specific font to be able to show the icons on the screen, if you don't have it installed on your system, the icons won't appear correctly, to download, click [here](https://github.com/marc-dantas/snake-editor/blob/main/app/resources/font/Aquawax-Pro-Pictograms-Regular.ttf?raw=true) to download it.
- If you're on Microsoft Windows, make sure your python installation includes the IDLE installation, to avoid syntax highlighting not working.

## How to customize the app?
- Text editor font - Variable `gui_text_editor_font`
  + Font family - First tuple value (`gui_text_editor_font[0]`);
  + Font size - Second tuple value (`gui_text_editor_font[1]`).<br><br>
- Syntax colors - HEX Colors or CSS Colors
  + COMMENT - From `syntax_colors`: background, foreground;
  + KEYWORD - From `syntax_colors`: background, foreground;
  + BUILTIN - From `syntax_colors`: background, foreground;
  + STRING - From `syntax_colors`: background, foreground;
  + DEFINITION - From `syntax_colors`: background, foreground.<br><br>
- General customization
  + Window title - Variable `gui_title`
  + Window background color - Variable `gui_bg_color`
  + Text editor background color - Variable `gui_text_editor_bg_color`
  + Window size - Variable `gui_min_size`
  + Welcome messsage - Variable `start_msg`
  + And more...

<p>Customizing this application is not recommended, as if you do something wrong the program may not work properly...<br>
  Everything that is customizable is in the <code>info.py</code> file, so everything mentioned here will refer to it.</p>
