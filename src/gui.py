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
def runLocking():
    tup = dialog.getPaths()
    password = passField.getFieldValue()

    # Удаляем сообщения если есть
    lb.clearMessages()
    lb.destroyLables()

    # Проверяем выбран ли файлы
    if len(tup) == 0:
        return messagebox.showerror("Ошибка", "Необходимо выбрать файлы")
    # Проверяем введен ли пароль
    if len(password) == 0 or password == passField.placeholder:
        return messagebox.showerror("Ошибка", "Необходимо ввести пароль")
    if len(password) > 15:
        return messagebox.showerror("Ошибка", "Пароль должен состоять из максимум 15 символов")

    i = 0
    for path in tup:
        ps.setPassword(path, password)

        # Добавляем сообщение об успешном выполнении
        lb.addMessageToList(f"Пароль должен был быть установлен для {dialog.fileNames[i]}", 6)
        lb.destroyLables()
        lb.createLables(background='#2e8b57')

        # Обновляем окно
        window.update()

        i += 1

    # Удаляем сообщения об успешном выполнении и выводим сообщение об успешном завершении процесса
    lb.destroyLables()
    lb.addMessageToList("ВСЕ ФАЙЛЫ БЫЛИ ОБРАБОТАНЫ, НАДЕЮСЬ УСПЕШНО...", 6)
    lb.createLables(background='#2e8b57')
        

# Инициализация кнопки выбора файлов
chooseFileBtn = Button(window, text="Выбрать файлы", command=dialog.callDialog, width=25, height=1)
chooseFileBtn.pack(side=TOP, padx=5, pady=5)

# Инициализация поля ввода пароля
passField.configure(width=30, justify=CENTER)
passField.pack(side=TOP, padx=5, pady=5)

# Инициализация кнопки запуска
showFileBtn = Button(window, text="Запустить обработку файлов", command=runLocking, width=25, height=1)
showFileBtn.pack(padx=5, pady=5)

window.mainloop()
