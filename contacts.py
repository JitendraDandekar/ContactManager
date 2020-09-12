from tkinter import *
import tkinter.messagebox as tkmsgbox
from db_conn import Database
import validation

db = Database('contacts.db')

root = Tk()
root.title("Contacts")
root.geometry("430x250")

#=-=-=-=-=-=Frames=-=-=-=-=-=-=
tops = Frame(root)
tops.pack(side=TOP)

bot = Frame(root)
bot.pack(side=BOTTOM)

#=-=-=-=-=-=-Variables=-=-=-=-=-=-=
fname = StringVar()
lname = StringVar()
mob = StringVar()
email = StringVar()

#=-=-=-=--=-=-=-=Functions=-=-=-=-=-=-=-=
def content():
    lst.delete(0, END)
    for row in db.fetch():
        lst.insert(END, row)

def select(row):
    global selected
    index = lst.curselection()
    selected = lst.get(index)

    fname.delete(0, END)
    fname.insert(END, selected[0])
    
    lname.delete(0, END)
    lname.insert(END, selected[1])

    mobnum.delete(0, END)
    mobnum.insert(END, selected[2])
    
    mail.delete(0, END)
    mail.insert(END, selected[3])

    for row in db.match():
        if selected[0]==row[1] and selected[1]==row[2] and selected[2]==row[3] and selected[3]==row[4]:
            global id
            id = row[0]

def add():
    if fname.get() == '' or lname.get() == '' or mob.get() == '':
        tkmsgbox.showwarning('Attention!','Please fill up required fields')
    if validation.mobchk(mob.get()) and validation.mailchk(email.get()):
        entity = (fname.get(), lname.get(), mob.get(), email.get())
        db.insert(entity)
        clear()
    content()

def update():
    if validation.mobchk(mob.get()) and validation.mailchk(email.get()):
        db.update(fname.get(), lname.get(), mob.get(), email.get(), id)
        content()
        clear()

def delete():
    db.delete(id)
    content()
    clear()

def clear():
    fname.delete(0, END)
    lname.delete(0, END)
    mobnum.delete(0, END)
    mail.delete(0, END)

#=-=-=-=-=-=-=Field Info=-=-=-=-=-=-=-=
fnameleb = Label(tops, text='First Name *')
fnameleb.grid(row=0,column=0)
fname = Entry(tops, textvariable=fname)
fname.grid(row=0, column=1)

lnameleb = Label(tops, text='Last Name *')
lnameleb.grid(row=0,column=2)
lname = Entry(tops, textvariable=lname)
lname.grid(row=0, column=3)

mobnumleb = Label(tops, text='Contact No. *')
mobnumleb.grid(row=1,column=0)
mobnum = Entry(tops, textvariable=mob)
mobnum.grid(row=1, column=1)

mailleb = Label(tops, text='Email')
mailleb.grid(row=1,column=2)
mail = Entry(tops, textvariable=email)
mail.grid(row=1, column=3)
#=-=-=-=-=-=-=Buttuns=-=-=-=-=-=-=-=-=
addbtn = Button(tops, text='ADD', command=add, padx=15)
addbtn.grid(row=2,column=0,pady=5)

upbtn = Button(tops, text='UPDATE', command=update, padx=10)
upbtn.grid(row=2,column=1,padx=10)

delbtn = Button(tops, text='DELETE', command=delete, padx=10)
delbtn.grid(row=2,column=2,padx=10)

clrbtn = Button(tops, text='CLEAR', command=clear, padx=10)
clrbtn.grid(row=2,column=3,padx=10)

#=-=-=--=-=-=-= Detail Info=-=-=-=-=-=-=-=-=
scrollbar = Scrollbar(bot)
scrollbar.pack(side=RIGHT, fill=Y, pady=10)

lst = Listbox(bot, yscrollcommand = scrollbar.set)
lst.pack(side=LEFT, fill=BOTH, ipadx=100, pady=10)

lst.bind('<<ListboxSelect>>', select)

content()

scrollbar.config(command=lst.yview)
root.mainloop()
