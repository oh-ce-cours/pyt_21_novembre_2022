import tkinter as tk
from tkinter import ttk
import time


def on_click_button():
    print("clicked")
    time.sleep(10)


# root window
root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("Button Demo")

# exit button
exit_button = ttk.Button(root, text="Click me :)", command=on_click_button)

exit_button.pack(ipadx=5, ipady=5, expand=True)

root.mainloop()
