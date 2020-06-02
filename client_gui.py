import socket
import threading
import time
from tkinter import *

def set_ip():
    ip = edit_text_ip.get()
    port = edit_text_port.get()

    # Define Client and connect to server:
    global client
    client = socket.socket()
    client.connect((ip, int(port)))

    # distryo input root
    input_root.destroy()
    # end of input root:
    input_root.quit()


def send():
    if str(edit_text.get()).strip() != "":
        message = edit_text.get()
        client.send(str.encode(message))

        # scrollbar:
        listbox.insert(END, message)
        edit_text.delete(0, END)

        # raw labels:
        # label = Label(canvas, text=message, bg="#00802b", fg="white")
        # label.pack(fill=X, side=TOP)


def recv():
    while True:
        response_message = client.recv(1024).decode()

        # scrollbar:
        listbox.insert(END, "Server: " + response_message)
        edit_text.delete(0, END)

        # raw labels:
        # label = Label(root, text = "Server : " + response_message, bg="#2929a3", fg="white")
        # label.pack(fill=X, side=TOP)


# Client GUI
# 1: Input Root GUI
input_root = Tk()

edit_text_ip = Entry()
edit_text_port = Entry()
ip_label = Label(input_root, text="Enter Server IP")
port_label = Label(input_root, text="Enter Server Port")
watermark = Label(input_root, text="Developed by: M-Taghizadeh", fg="#66000f")
connect_btn = Button(input_root, text="Connect To Server", command=set_ip, bg='#668cff', fg="white")

# show elements:
ip_label.pack(fill=X, side=TOP)
edit_text_ip.pack(fill=X, side=TOP)
port_label.pack(fill=X, side=TOP)
edit_text_port.pack(fill=X, side=TOP)
watermark.pack(fill=X, side=BOTTOM)
connect_btn.pack(fill=X, side=BOTTOM)

input_root.title("Client")
input_root.geometry("300x300")
input_root.resizable(width=False, height=False)

input_root.mainloop()

# 2: Main Root GUI
root = Tk()

# Scrollbar:
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
listbox = Listbox(root, yscrollcommand=scrollbar.set)
listbox.pack(fill=BOTH, side=TOP)
scrollbar.config(command=listbox.yview)

button = Button(root, text="Send Message", command=send, bg='#4040bf', fg="white")
button.pack(fill=X, side=BOTTOM)
edit_text = Entry(root)
edit_text.pack(fill=X, side=BOTTOM)

root.title("PyChat [Client]")
root.geometry("310x260")
root.resizable(width=False, height=False)

threading.Thread(target=recv).start()

root.mainloop()