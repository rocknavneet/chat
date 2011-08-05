#Server GUI

import socket, sys, time, logging, thread
from Tkinter import *
import tkMessageBox
import server


def srvrmsgs():
    msg = srvrsendmsg.get(1.0, END)
    server.servercall.senddata(msg)
    srvrsendmsg.delete(1.0, END)
    srvrrecvmsg.insert(END, "Server: "+msg)





chatserver = Tk()

chatserver["padx"] = 60
chatserver["pady"] = 60

chatserver.title("Server")

f1 = Frame(chatserver,width = 20, height = 5)
f1.pack(side = TOP)

f2 = Frame(chatserver,width = 20, height = 5)
f2.pack(side = BOTTOM)


srvrrecvmsg = Text(f1, width = 20, height = 5)
srvrrecvmsg.pack(padx = 10, pady =10)

srvrsendmsg = Text(f2, width = 20, height = 5)
srvrsendmsg.pack(padx = 10, pady =10)


sendbutton = Button(f2, width = 5, height = 2, text = "Send", command = srvrmsgs)
sendbutton.pack(side = BOTTOM, padx = 20, pady = 20)

while True:
    recvmsg = server.servercall.acceptdata()
    if recvmsg == '':break
    srvrrecvmsg.insert(END, "Client:"+recvmsg)



chatclient.mainloop()
