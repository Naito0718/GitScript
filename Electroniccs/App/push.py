import tkinter as tk
import random

def dispLabel():
    kuji=["大吉","中吉","小吉","こんにち凶"]
    lbl.configure(text=random.choice(kuji))


root=tk.Tk()
root.geometry("1200x1100")

lbl=tk.Label(text="くじ")
btn=tk.Button(text="PUSH",command=dispLabel)



lbl.pack()
btn.pack()
tk.mainloop()