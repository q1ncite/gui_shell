
import tkinter.messagebox
from tkinter import *


window = Tk()
window.title("Shell EnCryPt3d 172.18.211.91")
window.resizable(width=False, height=False)
window.geometry("665x530")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


def open_warning():
    tkinter.messagebox.showwarning(title="Предупреждение",
                                   message="Что бы продолжить, купите полный доступ tg: @dunnojava")


def send():
    send = "russian_agent#server:~$ " + e.get()
    txt.insert(END, "\n" + send)

    user = e.get().lower()

    if user == "help":
        txt.insert(END, "\n" + "ls, ifconfig, whoami, pwd, hack pentagon")

    elif user == "ifconfig" or user == "ip a" or user == "ip addr":
        txt.insert(END, "\n" + "172.18.211.91/24")

    elif user == "whoami":
        txt.insert(END, "\n" + "you're secret Russian agent")

    elif user == "ls":
        txt.insert(END, "\n" + "secret.txt\thashes.md5\tcompiled.bin")

    elif user == "pwd" or user == "where am i":
        txt.insert(END, "\n" + "/home/russian_agent")

    elif user == "hack pentagon":
        open_warning()

    else:
        txt.insert(END, "\n" + "Sorry! I didn't understand that")

    e.delete(0, END)


txt = Text(bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.place(x=1, y=503)

send = Button(text="Send", font=FONT_BOLD, bg=BG_GRAY, command=send)
send.place(x=590, y=502)

window.mainloop()
