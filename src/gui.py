from tkinter import *
from pathlib import Path
from Dialog import *
from PasswordSetter import *
from EntryField import *
from Lables import *

with open("config.txt", "r") as f:
    if f.readline() == "RU":
        from RU import *
    else:
        from ENG import *

# Создаем окно
window = Tk()

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

# Создаём функции для переключения языков
def set_lang_ru():
    with open('config.txt', 'w') as f:
        f.write('RU')
    restart_program()

def set_lang_eng():
    with open('config.txt', 'w') as f:
        f.write('ENG')
    restart_program()

# Создаём кнопки переключения языков
lang_ru_btn = Button(window, text="Русский", command=set_lang_ru)
lang_eng_btn = Button(window, text="English", command=set_lang_eng)

lang_ru_btn.grid(column = 0, row = 0, padx = 5, pady = 5, sticky = W)
lang_eng_btn.grid(column = 0, row = 1, padx = 5, pady = 5, sticky = W)

# Конфигурируем окно
window.title(TITLE)
window.geometry("500x300")
window.resizable(width=False, height=False)
window.configure(background='#2e8b57')

# Создаем экемпляр класса диалогового окна
dialog = Dialog()
# Создаем экземпляр класса поля ввода
passField = EntryField(window, ENTRY_TEXT)
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
        return messagebox.showerror(ERROR, ERROR1)
    # Проверяем введен ли пароль
    if button: 
        if len(password) == 0 or password == passField.placeholder:
            return messagebox.showerror(ERROR, ERROR2)
        if len(password) > 15:
            return messagebox.showerror(ERROR, ERROR3)

    i = 0
    errors = 0
    for index, path in enumerate(tup):
        
        name = names[index]

        lb.addMessageToList(f"{Path(path)}", 6)
        lb.destroyLables()
        lb.createLables(background='#2e8b57')

        # Обновляем окно
        window.update()
        res = ps.setPassword(path, name, password)
        if res["err"]:
            message = f"{ERROR}: {res['err']}"
            errors += 1
        else:
            message = f"{PASSWORD_INSTALLED_MSG} {dialog.fileNames[i]}"
        # Добавляем сообщение об успешном выполнении
        lb.addMessageToList(f"{message}", 6)
        lb.destroyLables()
        lb.createLables(background='#2e8b57')

        # Обновляем окно
        window.update()

        i += 1

    # Удаляем сообщения об успешном выполнении и выводим сообщение об успешном завершении процесса
    lb.destroyLables()
    lb.addMessageToList(f"{SUCCESS}{errors}", 6)
    lb.createLables(background='#2e8b57')
        

# Инициализация кнопки выбора файлов
chooseFileBtn = Button(window, text=CHOOSE_FILES_BTN, command=dialog.callDialog, width=25, height=1)
chooseFileBtn.grid(column = 1, row = 0, padx = 5, pady = 5)

# Инициализация поля ввода пароля
passField.configure(width=30, justify=CENTER)
passField.grid(column = 1, row = 1, padx = 5, pady = 5)

# Инициализация кнопки запуска
showFileBtn = Button(window, text=START_PROCESSING_BTN, command=runLocking, width=25, height=1)
showFileBtn.grid(column = 1 , row = 2, padx = 5, pady = 5)

# Инициализация кнопки запуска со стандартным паролем
presetBtn = Button(window, text="iWantToModify", command=lambda: runLocking('iWantToModify', 'preset'), width=25, height=1)
presetBtn.grid(column = 1, row = 3, padx = 5, pady = 5)

filler_txt = Label(text = " ", bg = '#2e8b57') # filler text to create 3rd column
filler_txt.grid(column = 2, row = 0)

window.columnconfigure(0, minsize = 166)
window.columnconfigure(2, minsize = 166)

window.mainloop()
