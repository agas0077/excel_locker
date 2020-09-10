from tkinter import filedialog, messagebox, Entry

class Dialog():
    def __init__(self):
        self.pathTuple = ()

    def callDialog(self):
        """Calls open file dialog, possible to choose only '.xlsx .xls .xlsm .xlsb'"""
        self.pathTuple = filedialog.askopenfilenames(filetypes=[("Excel files", ".xlsx .xls .xlsm .xlsb")])

    def getPaths(self):
        """Returns tuple of paths stored at class instance"""
        return self.pathTuple

    


    

