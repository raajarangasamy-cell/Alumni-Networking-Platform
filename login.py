from tkinter import *

root = Tk()
root.title("Alumni Login")
root.geometry("400x250")

Label(root, text="Email").pack()
Entry(root).pack()

Label(root, text="Password").pack()
Entry(root, show="*").pack()

Button(root, text="Login").pack(pady=10)

root.mainloop()def login():
    print("Login Module")
