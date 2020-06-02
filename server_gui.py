import socket
import threading
import time
from tkinter import *

def set_ip():
    ip = edit_text_ip.get()
    port = edit_text_port.get()
    
    # Define Server:
    server = socket.socket()
    server.bind((ip, int(port)))
    server.listen()

    global conn
    conn, addr = server.accept()

    # distryo input root
    input_root.destroy()
    # end of input root
    input_root.quit()


def send():
    if str(edit_text.get()).strip() != "":
        message = str.encode(edit_text.get())
        conn.send(message)

        # scrollbar:
        listbox.insert(END, message)
        edit_text.delete(0, END)

        # raw labels:
        # label = Label(root, text=message, bg="#00802b", fg="white")
        # label.pack(fill=X, side=TOP)

    # after sent message
    edit_text.delete(0, END)


def recv():
    while True:
        recv_message = conn.recv(1024).decode()

        # scrollbar:
        listbox.insert(END, "Client: " + recv_message)
        edit_text.delete(0, END)

        # raw labels:
        # label = Label(root, text = "Client : " + recv_message, bg="#2929a3", fg="white")
        # label.pack(fill=X, side=TOP)


# Server GUI:

# 1: Input Root GUI
input_root = Tk()

edit_text_ip = Entry()
edit_text_port = Entry()
ip_label = Label(input_root, text="Enter IP:")
port_label = Label(input_root, text="Enter Port:")
watermark = Label(input_root, text="Developed by: M-Taghizadeh", fg="#66000f")
connect_btn = Button(input_root, text="Connect To Server", command=set_ip, bg='#668cff', fg="white")

# show elements:
ip_label.pack(fill=X, side=TOP)
edit_text_ip.pack(fill=X, side=TOP)
port_label.pack(fill=X, side=TOP)
edit_text_port.pack(fill=X, side=TOP)
watermark.pack(fill=X, side=BOTTOM)
connect_btn.pack(fill=X, side=BOTTOM)

input_root.title("Server")
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

button = Button(root, text="Send Message", command=send, bg='#29a329', fg="white")
edit_text = Entry(root)

button.pack(fill=X, side=BOTTOM)
edit_text.pack(fill=X, side=BOTTOM)

root.title("PyChat [Server]")
root.geometry("310x260")
root.resizable(width=False, height=False)

threading.Thread(target=recv).start()

root.mainloop()