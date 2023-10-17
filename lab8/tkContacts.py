# TSU-CHENG, LU
# ITM 513 (02)     07/20/2023
# Lab8 
# Description: This program is to modify a GUI program, which allows you to add, update, delete and load contacts in to the database.

from tkinter import *
from tkinter import messagebox
import os
import myDatabase as db
from contacts import contactlist

#create a selection 
def selection () :
    print("At %s of %d" % (select.curselection(), len(contactlist)))
    return int(select.curselection()[0])

#create an add function 
def addContact () :
    if messagebox.askokcancel(title = "Add", message="Do you want to add this contact?"):
        name = nameVar.get()
        phone = phoneVar.get()
        try:
            db.insert_table(name, phone)
            contactlist.append([name, phone])
            select.insert(END, name)
            messagebox.showinfo("Add", "Contacts Added successfully")
            print(f"{name} has been added to the database")
        except Exception as e:
            messagebox.showerror("Error", message=str(e))

#create an update function 
def updateContact() :
    selection_tuple = select.curselection()
    if not selection_tuple:  # Check if no item is selected
        messagebox.showerror(title="Error", message="No contact selected.")
        return

    index = int(selection_tuple[0])
    new_name = nameVar.get()
    new_phone = phoneVar.get()
    old_phone = contactlist[index][1]  # Get the old phone number
    contact_id = contactlist[index][0]  # Get the ID of the selected contact
    db.update_table(new_name, new_phone, contact_id)
    contactlist[index] = [new_name, new_phone]
    select.delete(index)
    select.insert(index, new_name)

    # Show success message after updating the contact
    messagebox.showinfo(title="Success", message="Contact updated successfully.")

    print(f"Contact {new_name} had a contact number changed from {old_phone} to {new_phone}.")

#create a delete function 
def deleteContact() :
    global contactlist, select, index
    
    index = int(selection())
    if 0 <= index < len(contactlist):
        if messagebox.askokcancel("Exit", "Are you sure you want to delete this contact?"):
            del contactlist[index]
            contact_id = contactlist[index][0] 
            db.delete_table(contact_id)
            select.delete(index)
            # Show success message after deleting the contact
            messagebox.showinfo(title="Success", message="Contact deleted successfully.")

            deleted_contact_name = contactlist[index][0]
            print(f"Contact deleted: {deleted_contact_name}")

#create a loading function 
def loadContact  () :
    global contactlist, select  
    
    db.insert_contacts_from_list(contactlist)
    select.delete(0, END)
    contactlist = db.read_Contacts()
    
    for record in contactlist:
        name, phone = record
        select.insert(END, name)

#displaying the information from the contactlist
def printContacts():
    for record in contactlist:
        name, phone = record
        print(f"Name: {name}, Phone: {phone}")
#print the values
printContacts()

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
    btn1.pack(side=LEFT); btn2.pack(side=LEFT)
    btn3.pack(side=LEFT); btn4.pack(side=LEFT)

    frame1 = Frame(root)   
    frame1.pack()
    scroll = Scrollbar(frame1, orient=VERTICAL)
    select = Listbox(frame1, yscrollcommand=scroll.set, height=7)
    scroll.config (command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT,  fill=BOTH)

    exit_button = Button(root, text="Exit", command=exitApp)
    exit_button.pack(side=BOTTOM, pady=10)

    loadContact()
 
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)

    root.mainloop()

buildFrame()


