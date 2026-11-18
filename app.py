import os
from tkinter import *

task_count = 0

# Обработка нажатия на кнопку добавления задачи
def add_task():
    global task_count
    task_name = entry_name.get()
    task_days = entry_days.get()

    task_count += 1

    # Ошибка: сначала пытался поменять текст через несуществующий параметр caption
    # label_status["caption"] = f"Задач добавлено: {task_count}"
    label_status["text"] = f"Задач добавлено: {task_count}\nПоследняя: {task_name} ({task_days} дн.)"

# Очистка обоих полей ввода
def clear_fields():
    entry_name.delete(0, END)
    entry_days.delete(0, END)

# Подсветка кнопки при наведении курсора
def on_enter(event):
    btn_add["bg"] = "#d0f0c0"

def on_leave(event):
    btn_add["bg"] = "SystemButtonFace"

# Главное окно приложения (создаётся строго до PhotoImage)
root = Tk()
root.title("Планировщик задач")
root.geometry("460x520")

# Загрузка и вывод баннера сверху окна
base_dir = os.path.dirname(__file__)
logo_img = PhotoImage(file=os.path.join(base_dir, "baner.png"))
# logo_img = logo_img.subsample(2, 2)
label_img = Label(image=logo_img)
label_img.pack(pady=10)

# Поле ввода названия задачи с подписью
label_name = Label(text="Название задачи")
label_name.pack(pady=(5, 2))

entry_name = Entry(width=30)
entry_name.pack(pady=(0, 10))

# Поле ввода длительности задачи с подписью
label_days = Label(text="Длительность (дней)")
label_days.pack(pady=(5, 2))

entry_days = Entry(width=30)
entry_days.pack(pady=(0, 15))

# Ошибка: передавал функцию со скобками add_task(), из-за чего она срабатывала при запуске
# btn_add = Button(text="Добавить задачу", width=20, command=add_task())
btn_add = Button(text="Добавить задачу", width=20, command=add_task)
btn_add.pack(pady=5)

btn_add.bind("<Enter>", on_enter)
btn_add.bind("<Leave>", on_leave)

# Кнопка очистки полей
btn_clear = Button(text="Очистить поля", width=20, command=clear_fields)
btn_clear.pack(pady=5)

# Метка-счётчик добавленных задач в рамке
label_status = Label(
    text="Задач добавлено: 0",
    borderwidth=2,
    relief="ridge",
    padx=15,
    pady=8
)
label_status.pack(pady=15)

root.mainloop()