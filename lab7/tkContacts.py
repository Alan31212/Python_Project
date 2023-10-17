# TSU-CHENG, LU
# ITM 513 (02)     07/012/2023
# Lab7 
# Description: This program is to modify a GUI program, which allows you to add, update, delete and load contacts from a list defined in another pytyhon file.

from tkinter import *
from contacts import *
from tkinter import messagebox
import pickle
import os

#create a selection 
def selection () :
    print ("At %s of %d" % (select.curselection(), len(contactlist)))
    return int(select.curselection()[0])

#create an add function 
def addContact () :
    contactlist.append ([nameVar.get(), phoneVar.get()])
    messagebox.showinfo("Add", "Contacts Added successfully")
    setList ()

#create an update function 
def updateContact() :
    contactlist[selection()]=[nameVar.get(), phoneVar.get()]
    messagebox.showinfo("Update", "Contacts Updated successfully")
    with open("contacts.py", "w") as file:
        file.write("contactlist = \n" + repr(contactlist))
    setList ()

#create a delete function 
def deleteContact() :
    del contactlist[selection()]
    if (messagebox.askokcancel("Exit", "Are you sure you want to delete this contact?") == 1):
        os.close(1)
    setList ()

#create a loading function 
def loadContact  () :
    name, phone = contactlist[selection()]
    nameVar.set(name)
    phoneVar.set(phone)

#create a saving function 
def saveContacts () :
    with open("contacts.pkl", "wb") as file:
        pickle.dump(contactlist, file)
    messagebox.showinfo("Save", "Contacts saved successfully")

#create an exiting function 
def exitApp () :
    if (messagebox.askokcancel(title = "Exit", message = "Are you want to exit, OK or Cancel") == 1):
        os._exit(1)


#build a frame page 
def buildFrame () :
    global nameVar, phoneVar, select
    root = Tk()
    root.title("My Contact List")
    root.geometry("300x280")

    frame1 = Frame(root)
    frame1.pack()

    Label(frame1, text="Name:").grid(row=0, column=0, sticky=W)
    nameVar = StringVar()
    name = Entry(frame1, textvariable=nameVar)
    name.grid(row=0, column=1, sticky=W)

    Label(frame1, text="Phone:").grid(row=1, column=0, sticky=W)
    phoneVar= StringVar()
    phone= Entry(frame1, textvariable=phoneVar)
    phone.grid(row=1, column=1, sticky=W)

    frame1 = Frame(root)       # add a row of buttons
    frame1.pack()
    btn1 = Button(frame1,text=" Add  ",command=addContact)
    btn2 = Button(frame1,text="Update",command=updateContact)
    btn3 = Button(frame1,text="Delete",command=deleteContact)
    btn4 = Button(frame1,text=" Load ",command=loadContact)
    btn5 = Button(frame1,text=" save ",command=saveContacts)
    btn1.pack(side=LEFT); btn2.pack(side=LEFT)
    btn3.pack(side=LEFT); btn4.pack(side=LEFT)
    btn5.pack(side=LEFT)

    frame1 = Frame(root)       # allow for selection of names
    frame1.pack()
    scroll = Scrollbar(frame1, orient=VERTICAL)
    select = Listbox(frame1, yscrollcommand=scroll.set, height=7)
    scroll.config (command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT,  fill=BOTH)

    exit_button = Button(root, text="Exit", command=exitApp)
    exit_button.pack(side=BOTTOM, pady=10)

    return root

def setList () :
    contactlist.sort()
    select.delete(0,END)
    for name,phone in contactlist :
        select.insert (END, name)
    select.config(height=10)

root = buildFrame()
setList ()

root.mainloop()

