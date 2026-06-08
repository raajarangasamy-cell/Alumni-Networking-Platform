from tkinter import *

root = Tk()
root.title("Alumni Networking Platform")
root.geometry("500x400")

Label(root, text="Welcome to Alumni Networking Platform",
      font=("Arial", 14)).pack(pady=20)

Button(root, text="Search Alumni", width=20).pack(pady=10)

Button(root, text="View Jobs", width=20).pack(pady=10)

Button(root, text="Manage Profile", width=20).pack(pady=10)

Button(root, text="Logout", width=20).pack(pady=10)

root.mainloop()
