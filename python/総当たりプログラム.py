import time
import tkinter as tk
import string
import random
import webbrowser
import pyautogui

password= 0

#文字列の用意
chars = string.ascii_letters + string.digits
chars += '/*-+.,!#$%&()~|_'


start = time.perf_counter()

root = tk.Tk()
root.geometry("350x500")

#スタートの時間設定
start = time.perf_counter()

#ここにループ文
def aiu():
    i = 1    
    while i == 1:
        size = 4
        chars = str(1234567890)
        password = ''.join(random.choices(chars,k=size))
        if password == "1986":
            i = i - 1
    webbrowser.open("https://www.google.com/")
    time.sleep(0.5)
    pyautogui.click(x=990, y=400, clicks=1, button="left")
    pyautogui.typewrite(password)
    pyautogui.press("enter")
#終わりの時間計測
    end = time.perf_counter() - start
    end = str(end)
    statusbar = tk.Label(root, text =  "パスワードは↓")
    statusbar.place(x = 10, y = 180)
    statusbar = tk.Label(root, text =  password)
    statusbar.place(x = 50, y = 215)
    statusbar = tk.Label(root, text =  end + "秒かかりました！")
    statusbar.place(x = 10, y = 300)

#スタートボタン
run_button = tk.Button(root, text = "    R u n    ", command = aiu)
run_button.place(x = 130, y = 40)


root.mainloop()
