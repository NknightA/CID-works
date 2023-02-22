import webbrowser
import time
import tkinter as tk
import random

fonts = ("", 50)
ss =["gold","blue","green"]

window_size= "1370x700"
def gamen():
	fon = ("", 50)
	root = tk.Tk()
	root.attributes('-fullscreen', True)
	root.title("画面固定です")
	root.overrideredirect(True)
	root.configure(bg="red")
	statusbar = tk.Label(root, text =  "あなたのパソコンはハッキングされました。" ,font = fonts,bg 	="red", fg="gold")
	statusbar.place(x = 60, y = 350)
	root.protocol("WM_DELETE_WINDOW", (lambda: 'pass')())

#ページを増殖する文
def click_close():
    root = tk.Tk()
    root.geometry(window_size)
    root.title("これはワーム")
    b = random.randint(0,2)
    root.configure(bg="black")
    run_button = tk.Button(root, text = "解除するにはこのボタンを押してください", font=fonts, bg=ss[b], fg='red', command = gamen)
    run_button.place(x = 68, y = 100)
    root.resizable(0, 0)
    root.protocol("WM_DELETE_WINDOW", click_close)

#最初のウィンドウの表示
root = tk.Tk()
root.geometry(window_size)
root.title("これはワーム")
b = random.randint(0,2)
root.configure(bg="black")
run_button = tk.Button(root, text = "解除するにはこのボタンを押してください", font=fonts, bg=ss[b], fg='red', command = gamen)
run_button.place(x = 68, y = 100)
root.resizable(0, 0)  
root.protocol("WM_DELETE_WINDOW", click_close)

root.mainloop()