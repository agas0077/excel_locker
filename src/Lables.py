from tkinter import Label as L


class Lables(L):
    def __init__(self):
        super().__init__()
        self.done = []
        self.lables = []

    def addMessageToList(self, message, maxNum):
        self.done.append(message)
        if len(self.done) > maxNum:
            self.done.pop(0)

    def createLables(self, background=None):
        self.lables = [L(text=message, wraplength=500, background=background) for message in self.done]
        for lable in self.lables:
            lable.pack()

    def destroyLables(self):
        if len(self.lables) != 0:
            for lable in self.lables:
                lable.destroy()

    def clearMessages(self):
        self.done = []
