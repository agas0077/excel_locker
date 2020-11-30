from tkinter import *
from pathlib import Path
from Dialog import *
from PasswordSetter import *
from EntryField import *
from Lables import *

# Создаем окно с необходимыми параметрами
window = Tk()
window.title('Установка паролей на редактирование файлов Excel')
window.geometry("500x300")
window.resizable(width=False, height=False)
window.configure(background='#2e8b57')

# Создаем экемпляр класса диалогового окна
dialog = Dialog()
# Создаем экземпляр класса поля ввода
passField = EntryField(window, "Пароль")
# Создаем экземпляр класса установщика паролей
ps = PasswordSetter()
# Создаем экземпляр лейбла
lb = Lables()


# Функция, определяющая адреса файлов, пароль и запускающая процесс блокировки файлов
def runLocking(mypassword=None, button=None):
    tup = dialog.getPaths()
    names = dialog.getNames()
    password = mypassword or passField.getFieldValue()

    # Удаляем сообщения если есть
    lb.clearMessages()
    lb.destroyLables()

    # Проверяем выбран ли файлы
    if len(tup) == 0:
        return messagebox.showerror("Ошибка", "Необходимо выбрать файлы")
    # Проверяем введен ли пароль
    if not button: 
        if len(password) == 0 or password == passField.placeholder:
            return messagebox.showerror("Ошибка", "Необходимо ввести пароль")
        if len(password) > 15:
            return messagebox.showerror("Ошибка", "Пароль должен состоять из максимум 15 символов")

    i = 0
    errors = 0
    for index, path in enumerate(tup):
        
        name = names[index]

        lb.addMessageToList(f"Обработка {name}", 6)
        lb.destroyLables()
        lb.createLables(background='#2e8b57')

        # Обновляем окно
        window.update()
        res = ps.setPassword(path, name, password)
        if res["err"]:
            message = f"Ошибка: {res['err']}"
            errors += 1
        else:
            message = f"Пароль установлен для {name}"
        # Добавляем сообщение об успешном выполнении
        lb.addMessageToList(f"{message}", 6)
        lb.destroyLables()
        lb.createLables(background='#2e8b57')

        # Обновляем окно
        window.update()

        i += 1

    # Выводим сообщение об успешном завершении процесса
    return messagebox.showinfo("Завершение работы", f"Все файлы были обработаны! Ошибок: {errors}")        

        

# Инициализация кнопки выбора файлов
chooseFileBtn = Button(window, text="Выбрать файлы", command=dialog.callDialog, width=25, height=1)
chooseFileBtn.pack(side=TOP, padx=5, pady=5)

# Инициализация поля ввода пароля
passField.configure(width=30, justify=CENTER)
passField.pack(side=TOP, padx=5, pady=5)

# Инициализация кнопки запуска
showFileBtn = Button(window, text="Запустить обработку файлов", command=runLocking, width=25, height=1)
showFileBtn.pack(padx=5, pady=5)

# Инициализация кнопки запуска со стандартным паролем
presetBtn = Button(window, text="iWantToModify", command=lambda: runLocking('iWantToModify', 'preset'), width=25, height=1)
presetBtn.pack(padx=5, pady=5)

window.mainloop()
