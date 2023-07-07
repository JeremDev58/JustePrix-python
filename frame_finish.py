from tkinter import Frame, Label, Button
from tkinter.font import Font


class FrameFinish(Frame):
    def __init__(self, master, result, num):
        Frame.__init__(self, master=master)
        self.lb = Label(self, font=Font(size=20))
        if result:
            self.lb["text"] = "Tu as gagné !\nTu as trouvée le juste prix qui était de : "+str(num)
            self.lb["bg"] = "#03ae01"
            self.background = "#03ae01"
        else:
            self.lb["text"] = "Tu as Perdu !\nLe juste prix était : "+str(num)
            self.lb["bg"] = "#d16667"
            self.background = "#d16667"
        self.lb.pack(fill="both")
        self.btn = Button(self, text="Recommencer", command=lambda: self.master.switch_view([0, self.master.mode, self.master.coups]))
        self.btn.pack(fill="x", anchor='e')