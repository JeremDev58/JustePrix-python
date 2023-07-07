from tkinter import Frame, Label, Entry, Button, StringVar, LabelFrame
from tkinter.font import Font
import random


class FrameGame(Frame):
    def __init__(self, master, mode, coups):
        Frame.__init__(self, master=master, bg="#4c70e4")
        self.num = random.randint(0, int(mode))
        self.font = Font(size=20)
        self.count = int(coups)
        self.poop = 0
        self.txt = "nombre de coup restant: "
        self.nb_chances = Label(self, text=self.txt+str(self.count), bg="#4c70e4")
        self.container = Frame(self, bg="#4c70e4")
        self.lb = Label(self.container, text="Choisis un nombre entre 0 et "+str(mode)+": ", font=self.font, bg="#4c70e4")
        self.choice = StringVar()
        self.input = Entry(self.container,textvariable=self.choice, font=self.font)
        self.btn = Button(self, text="Valider", command=self.on_click)
        self.btn.bind("<Return>", self.on_click)
        self.container_reponse = LabelFrame(self, text="Réponse", bg="#4c70e4")
        self.reponse = Label(self.container_reponse, font=self.font, height=1, bg="#4c70e4")
        self.container_history = LabelFrame(self, text="Historique", height=1, bg="#4c70e4")

        self.nb_chances.pack(anchor='e', padx=5, pady=5)
        self.container.pack(fill="x", padx=5, pady=5)
        self.lb.pack(side="left")
        self.input.pack(side="right", padx=5, pady=5)
        self.btn.pack(anchor="e", padx=5, pady=5)
        self.container_reponse.pack(fill="x", padx=5, pady=5)
        self.reponse.pack(fill="x", padx=5, pady=5)
        self.container_history.pack(fill="x", padx=5, pady=5)

    def on_click(self):
        try:
            int(self.choice.get())
        except:
            self.input["background"] = "#d16667"
        else:
            self.input["background"] = "white"
            self.poop += 1
            self.count -= 1
            self.nb_chances["text"] = self.txt+str(self.count)
            if self.count == 0:
                self.master.switch_view([1, False, self.num])
            if int(self.choice.get()) == self.num:
                self.master.switch_view([1, True, self.num])
            elif int(self.choice.get()) > self.num:
                self.reponse["text"] = "C'est plus petit."
                Label(self.container_history, text=str(self.poop)+") C'est plus petit que "+str(self.choice.get()), fg="#ea87f0", bg="#4c70e4").pack(anchor="w")
            else:
                self.reponse["text"] = "C'est plus grand."
                Label(self.container_history, text=str(self.poop) + ") C'est plus grand que "+str(self.choice.get()), fg="#ea87f0", bg="#4c70e4").pack(anchor="w")