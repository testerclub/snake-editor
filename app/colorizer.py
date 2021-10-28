from idlelib.colorizer import ColorDelegator
from idlelib.percolator import Percolator
from info import syntax_colors

color_filter = ColorDelegator()

def highlight_syntax(root):
    color_filter.tagdefs['COMMENT'] = syntax_colors['COMMENT']
    color_filter.tagdefs['KEYWORD'] = syntax_colors['KEYWORD']
    color_filter.tagdefs['BUILTIN'] = syntax_colors['BUILTIN']
    color_filter.tagdefs['STRING'] = syntax_colors['STRING']
    color_filter.tagdefs['DEFINITION'] = syntax_colors['DEFINITION']
    Percolator(root.code).insertfilter(color_filter)

