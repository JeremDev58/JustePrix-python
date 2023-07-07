from tkinter import Tk
from frame_game import FrameGame
from frame_finish import FrameFinish
from frame_selector import FrameSelector


class JustePrix(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Juste Prix")
        self.resizable(False, False)
        self.view = FrameSelector(self)
        self.view.pack(fill="both")
        self.mode = ""
        self.coups = 0

    def switch_view(self, view):
        self.view.destroy()
        if view[0] == 0:
            if view[1]:
                self.mode = int(view[1])
                self.coups = int(view[2])
            self.view = FrameGame(self, self.mode, self.coups)
        else:
            self.view = FrameFinish(self, view[1], view[2])
        self.view.pack(fill="both")

