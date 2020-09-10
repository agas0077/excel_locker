from tkinter import *
from Dialog import *
from PasswordSetter import *
from EntryField import *
from Lables import *

# Создаем окно с необходимыми параметрами
window = Tk()
window.title('Установка паролей на редактирование файлов Excel v0.1.0')
window.geometry("500x300")
window.resizable(width=False, height=False)

# Создаем экемпляр класса диалогового окна
dialog = Dialog()
# Создаем экземпляр класса поля ввода
passField = EntryField(window, "Пароль")
# Создаем экземпляр класса установщика паролей
ps = PasswordSetter()
# Создаем экземпляр лейбла
lb = Lables()

# Функция, определяющая адреса файлов, пароль и запускающая процесс блокировки файлов
def runLocking():
    tup = dialog.getPaths()
    password = passField.getFieldValue()
    # Проверяем выбран ли файлы
    if len(tup) == 0:
        return messagebox.showerror("Ошибка", "Необходимо выбрать файлы")
    # Проверяем введен ли пароль
    if len(password) == 0 or password == passField.placeholder:
        return messagebox.showerror("Ошибка", "Необходимо ввести пароль")
    

    for path in tup:
        ps.setPassword(path, password)
        lb.addMessageToList(f"the password has been set for {path}")
        lb.destroyLables()
        lb.createLables()
    lb.destroyLables()
    lb.clearMessages()
    lb.addMessageToList("Все файлы были обработаны")
    lb.createLables()
        



# Инициализация кнопки выбора файлов
chooseFileBtn = Button(window, text="Выбрать файлы", command=dialog.callDialog, width=25, height=2)
chooseFileBtn.pack(side=TOP, padx=5, pady=5)

# Инициализация поля ввода пароля
passField.pack(side=TOP, padx=5, pady=5)

# Инициализация кнопки запуска
showFileBtn = Button(window, text="Запустить обработку файлов", command=runLocking, width=25, height=2)
showFileBtn.pack(padx=5, pady=5)

window.mainloop()