from idlelib.colorizer import ColorDelegator
from idlelib.percolator import Percolator
import interface as gui

color_filter = ColorDelegator()

def apply(theme, root):
    choice = {
        'draculla': lambda: change_draculla(),
        'monokai': lambda: change_monokai(),
        'darker': lambda: change_darker(),
        'white': lambda: change_white()
    }
    choice[theme]()
    Percolator(root).insertfilter(color_filter)

def change_draculla():
    color_filter.tagdefs['COMMENT'] = {'foreground': '#FF0000', 'background': '#FFFFFF'}
    color_filter.tagdefs['KEYWORD'] = {'foreground': '#007F00', 'background': '#FFFFFF'}
    color_filter.tagdefs['BUILTIN'] = {'foreground': '#7F7F00', 'background': '#FFFFFF'}
    color_filter.tagdefs['STRING'] = {'foreground': '#7F3F00', 'background': '#FFFFFF'}
    color_filter.tagdefs['DEFINITION'] = {'foreground': '#007F7F', 'background': '#FFFFFF'}

def change_monokai():
    color_filter.tagdefs['COMMENT'] = {'foreground': '#FF0000', 'background': '#FFFFFF'}
    color_filter.tagdefs['KEYWORD'] = {'foreground': '#007F00', 'background': '#FFFFFF'}
    color_filter.tagdefs['BUILTIN'] = {'foreground': '#7F7F00', 'background': '#FFFFFF'}
    color_filter.tagdefs['STRING'] = {'foreground': '#7F3F00', 'background': '#FFFFFF'}
    color_filter.tagdefs['DEFINITION'] = {'foreground': '#007F7F', 'background': '#FFFFFF'}

def change_darker():
    color_filter.tagdefs['COMMENT'] = {'foreground': '#FF0000', 'background': '#FFFFFF'}
    color_filter.tagdefs['KEYWORD'] = {'foreground': '#007F00', 'background': '#FFFFFF'}
    color_filter.tagdefs['BUILTIN'] = {'foreground': '#7F7F00', 'background': '#FFFFFF'}
    color_filter.tagdefs['STRING'] = {'foreground': '#7F3F00', 'background': '#FFFFFF'}
    color_filter.tagdefs['DEFINITION'] = {'foreground': '#007F7F', 'background': '#FFFFFF'}

def change_white():
    color_filter.tagdefs['COMMENT'] = {'foreground': '#FF0000', 'background': '#FFFFFF'}
    color_filter.tagdefs['KEYWORD'] = {'foreground': '#007F00', 'background': '#FFFFFF'}
    color_filter.tagdefs['BUILTIN'] = {'foreground': '#7F7F00', 'background': '#FFFFFF'}
    color_filter.tagdefs['STRING'] = {'foreground': '#7F3F00', 'background': '#FFFFFF'}
    color_filter.tagdefs['DEFINITION'] = {'foreground': '#007F7F', 'background': '#FFFFFF'}
