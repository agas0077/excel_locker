from tkinter import Label as L

class Lables(L):
    def __init__(self):
        super().__init__()
        self.done = []
        self.lables = []
    
    def addMessageToList(self, message):
        return self.done.append(message)

    def createLables(self):
        self.lables = [L(text=message) for message in self.done]
        for lable in self.lables:
            lable.pack()
            
    def destroyLables(self):
        if len(self.lables) != 0:
            for lable in self.lables:
                lable.destroy()

    def clearMessages(self):
        self.done = []