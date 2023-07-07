from tkinter import Frame, Label, StringVar, Button
from tkinter.ttk import Combobox


class FrameSelector(Frame):
    def __init__(self, master):
        Frame.__init__(self, master=master, bg="#4c70e4")
        self.container_mode = Frame(self, bg="#4c70e4")
        self.lb_mode = Label(self.container_mode, text="Selectionnez un mode : ", bg="#4c70e4")
        self.mode_values = ["10",
                            "100",
                            "1000"]
        self.mode = StringVar(value=self.mode_values[0])
        self.box_mode = Combobox(self.container_mode, textvariable=self.mode, values=self.mode_values, state="readonly")

        self.container_coups = Frame(self, bg="#4c70e4")
        self.lb_coups = Label(self.container_coups, text="Selectionnez le nombre de coups : ", bg="#4c70e4")
        self.coups_values = ["5",
                            "10",
                            "15"]
        self.coups = StringVar(value=self.coups_values[0])
        self.box_coups = Combobox(self.container_coups, textvariable=self.coups, values=self.coups_values, state="readonly")
        self.btn = Button(self, text="Valider", command=lambda: self.master.switch_view([0, self.mode.get(), self.coups.get()]))

        self.container_mode.pack(fill="x", padx=5, pady=5)
        self.lb_mode.pack(side="left")
        self.box_mode.pack(side="right")
        self.container_coups.pack(fill="x", padx=5, pady=5)
        self.lb_coups.pack(side="left")
        self.box_coups.pack(side="right")
        self.btn.pack(anchor="e")