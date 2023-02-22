## 実行のためファイル名変わってます by 前田
## 変更日 2023-02-21(火)
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
fonts = ("", 20)
fon = ("",20)
aiu=[]
f = int(0)

#文字列の用意
chars = string.ascii_letters + string.digits
chars += '/*-+.,!#$%&()~|_'


start = time.perf_counter()

root = tk.Tk()
root.geometry("485x500")
root.configure(bg="black")

#スタートの時間設定
start = time.perf_counter()

#ここにループ文
def aiu():
    print("-1")
    i = 1    
    print("-2")
    while i == 1:
        size = 4
        chars = str(1234567890)
        password = ''.join(random.choices(chars,k=size))
        if password == "1986":
            i = i - 1
    webbrowser.open("https://cid-works.vercel.app/") ##URL 変更済
    print("-3")
    time.sleep(0.5)
    autopresstab = "tab"
    autopressalt = "alt"

    ## ウィンドウフォーカス切り替え(Alt + Tab)
    pyautogui.press(autopresstab + autopressalt)
    print("1")
    pyautogui.press("tab")
    print("2")
    pyautogui.typewrite(password)
    print("3")
    print("4")
    pyautogui.press("tab")
    pyautogui.press("enter")
    print("5")
#終わりの時間計測
    end = time.perf_counter() - start
    end = round(end, 3)
    end = str(end)
    password = "  ".join(password)
    print('1')
#ラベルやボタンの表示
    statusbar = tk.Label(root, text =  "パスワードは↓" ,font = fonts,bg ="black", fg="Lime")
    statusbar.place(x = 10, y = 180)
    statusbar = tk.Label(root, text = password ,font = fonts ,bg ="black",fg="Lime")
    statusbar.place(x = 150, y = 230)
    statusbar = tk.Label(root, text =  end + "秒かかりました！" , font = fonts,bg ="black" ,fg="Lime")
    statusbar.place(x = 10, y = 340)

#スタートボタン
run_button = tk.Button(root, text = "    R u n    " , borderwidth="15", font = fon , bg="black", fg = "Lime", command = aiu)
run_button.place(x = 130, y = 40)


root.mainloop()
