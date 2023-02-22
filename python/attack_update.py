## 実行のためファイル名変わってます by 前田
## 変更日 2023-02-20(月)
## URL変更 'google.com' から 'localhost:3000'(私のローカルサーバーURLです
# もし動かしたい時は前田に連絡お願いします。
# メルアド f22aa021@chuo.ac.jp
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
    webbrowser.open("http://localhost:3000") ##URL 変更済
    time.sleep(0.5)

    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.typewrite(password)
    pyautogui.press("tab")
    pyautogui.press("enter")