from tkinter import *

root = Tk()
root.title("Alumni Registration")
root.geometry("400x300")

Label(root, text="Name").pack()
Entry(root).pack()

Label(root, text="Email").pack()
Entry(root).pack()

Label(root, text="Password").pack()
Entry(root, show="*").pack()

Button(root, text="Register").pack(pady=10)

root.mainloop()
