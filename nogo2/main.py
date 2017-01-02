
from kivy.app import App
from kivy import platform

import sys
from os.path import abspath, join, dirname
nogo_path = dirname(abspath(__file__))
sys.path = [join(nogo_path, 'ext')] + sys.path
sys.path.append(dirname(__file__))

# if platform == 'android':
#     from .gui import board
# else:
#     from nogo2.gui import board

from gui import board

from gui import misc

print('cb', misc.ColouredButton)

print('board', board.__file__)

class NogoApp(App):
    def build(self):
        return board.GuiBoard()


NogoApp().run()
