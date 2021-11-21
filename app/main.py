from tkinter.font import Font
import info, engine
import interface

main_window = None
credits_window = None


def open_credits():
    global credits_window
    credits_window = interface.Credits()
    credits_window.create_elements()
    credits_window.mainloop()

def create_file(root):
    new_file = interface.ask_new_file_name()
    execution = lambda: engine.new_file(new_file['filename'].get())
    new_file['button'].configure(command=execution)
    new_file['window'].mainloop()


def apply_functions():
    global main_window
    main_window.credits.configure(command=open_credits)
    main_window.save.configure(command=lambda: engine.save_file(main_window))
    main_window.open.configure(command=lambda: engine.open_file(main_window))
    font = Font(font=main_window.code['font'])
    tab_count = font.measure(info.gui_text_editor_tab_count)
    main_window.code.configure(tabs=tab_count)
    engine.highlight_syntax(main_window)


def start_main_window():
    global main_window
    main_window = interface.Main(info.gui_min_size, info.gui_title)
    main_window.create_top_bar()
    main_window.create_text_editor()


def main():
    global main_window, credits_window
    start_main_window()
    apply_functions()
    main_window.mainloop()


if __name__ == "__main__":
    main()
