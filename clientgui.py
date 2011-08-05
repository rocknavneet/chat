# Client GUI
import socket, sys, time, logging, thread
from Tkinter import *
import tkMessageBox
import client, server

def clntmsgs():
    msg = clntsendmsg.get(1.0, END)
    client.senddata(msg)
    clntsendmsg.delete(1.0, END)
    clntrecvmsg.insert(END, "Client: "+msg)




chatclient = Tk()

chatclient["padx"] = 60
chatclient["pady"] = 60

chatclient.title("Client")

f1 = Frame(chatclient,width = 20, height = 5)
f1.pack(side = TOP)

f2 = Frame(chatclient,width = 20, height = 5)
f2.pack(side = BOTTOM)


clntrecvmsg = Text(f1, width = 20, height = 5)
clntrecvmsg.pack(padx = 10, pady =10)

clntsendmsg = Text(f2, width = 20, height = 5)
clntsendmsg.pack(padx = 10, pady =10)


sendbutton = Button(f2, width = 5, height = 2, text = "Send", command = clntmsgs)
sendbutton.pack(side = BOTTOM, padx = 20, pady = 20)

while True:
    recvmsg = client.acceptdata()
    if recvmsg == '':break
    clntrecvmsg.insert(END, "Server:"+recvmsg)


chatclient.mainloop()
