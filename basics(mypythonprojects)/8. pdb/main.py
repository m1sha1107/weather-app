from tkinter import *
import dbs
dbs.setup()
root = Tk()
root.geometry("600x500")
result = None

#entry setup
def entrysub():
    global namee, agee, heighte, ethne
    dbs.insert(namee.get(), agee.get(), heighte.get(), ethne.get())
    namee.delete(0, END)
    agee.delete(0, END)
    heighte.delete(0, END)
    ethne.delete(0,END)

#query setup
def searchsub():
    global bar, opt, result, resf
    y = opt.get()
    y.strip()
    if y == "full name":
        x = "name"
    if y == "age":
        x = "age"
    if y == "height":
        x = "height"
    if y == "ethnicity":
        x = "ethn"
    result = dbs.query(x, bar.get())
    resf.grid(row=2, column=0, pady=5, columnspan=5)
    res = []
    v = 1
    for i in result:
        t = str(i[0])+"\t\t\t"+str(i[1])+"\t\t\t"+str(i[2])+"\t\t\t"+str(i[3])
        l = Label(resf, text=t, padx=3, pady=3)
        l.grid(row=v, column=0)
        v += 1

#entry tab setup
entryf = LabelFrame(root, padx=10, pady=10)
namel = Label(entryf, text="full name", pady=7)
agel = Label(entryf, text="age", pady=7)
heightl = Label(entryf, text="height", pady=7)
ethnl = Label(entryf, text="ethnicity", pady=7)
namee = Entry(entryf, width=65, borderwidth=1)
agee = Entry(entryf, width=65, borderwidth=1)
heighte = Entry(entryf, width=65, borderwidth=1)
ethne = Entry(entryf, width=65, borderwidth=1)
submite = Button(entryf, text="submit",padx=20, pady=5, relief=RAISED, command=entrysub)
namel.grid(row=0, column=0, sticky=W, padx=2)
namee.grid(row=1, column=0, columnspan=2)
agee.grid(row=3, column=0, columnspan=2)
agel.grid(row=2, column=0, sticky=W, padx=3)
heightl.grid(row=4, column=0, sticky=W, padx=3)
heighte.grid(row=5, column=0, columnspan=2)
ethnl.grid(row=6, column=0, sticky=W, padx=3)
ethne.grid(row=7, column=0, columnspan=2)
submite.grid(row=8, column=1, pady=7, sticky=E)

#search tab setup
opt = StringVar()
opt.set("full name")
searchf = LabelFrame(root, padx=10, pady=10)
resf = LabelFrame(searchf, padx=10, pady=10)
bar = Entry(searchf, width=40, borderwidth=3)
searchl = Label(searchf, text="search by:")
x = OptionMenu(searchf, opt, "full name", "age", "height", "ethnicity")
submit = Button(searchf, text="search", padx=10, pady=5, relief=RAISED, command=searchsub)
context = Label(resf, text="Name \t\t\t age \t\t\t height \t\t\t ethnicity", padx=3, pady=3)
bar.grid(row=0, column=0, columnspan=2, sticky=W)
submit.grid(row=0, column=2, padx=7, sticky=W)
searchl.grid(row=0, column=3, padx=25, sticky=W)
x.grid(row=0, column=4, sticky=W)
context.grid(row=0, column=0)

#tab buttons setup
def epress():
    global entryf, searchf
    global searchb, entryb
    searchb.grid_forget()
    entryb.grid_forget()
    entryb = Button(root, text="entry", padx=90, pady=10, relief=SUNKEN, command=epress)
    searchb = Button(root, text="search", padx=90, pady=10, relief=RAISED, command=spress)
    entryb.grid(row=0, column=0, padx=5, pady=5, sticky=W)
    searchb.grid(row=0, column=1, padx=5, pady=5, sticky=W)
    searchf.grid_forget()
    entryf.grid(row=1, column=0, padx=5, pady=5, columnspan=2, sticky=W)

def spress():
    global entryf, searchf
    global searchb, entryb
    searchb.grid_forget()
    entryb.grid_forget()
    entryb = Button(root, text="entry", padx=90, pady=10, relief=RAISED, command=epress)
    searchb = Button(root, text="search", padx=90, pady=10, relief=SUNKEN, command=spress)
    entryb.grid(row=0, column=0, padx=5, pady=5, sticky=W)
    searchb.grid(row=0, column=1, padx=5, pady=5, sticky=W)
    entryf.grid_forget()
    searchf.grid(row=1, column=0, sticky=W, columnspan=2)

entryb = Button(root, text="entry", padx=90, pady=10, relief=SUNKEN, command=epress)
searchb = Button(root, text="search", padx=90, pady=10, relief=RAISED, command=spress)
entryb.grid(row=0, column=0, padx=5, pady=5, sticky=W)
searchb.grid(row=0, column=1, padx=5, pady=5, sticky=W)
entryf.grid(row=1, column=0, padx=5, pady=5, columnspan=2, sticky=W)
root.mainloop()
