from tkinter import *
from PIL.ImageTk import PhotoImage, Image
root = Tk()
im1 = PhotoImage(Image.open(r"images\1.png"))
im2 = PhotoImage(Image.open(r"images\2.png"))
im3 = PhotoImage(Image.open(r"images\3.png"))
im_list = [im1, im2, im3]
num = 0

def next(num):
    global im_list
    global image
    image.grid_forget()
    num += 1
    image = Label(root, image=im_list[num])
    update = Label(root, text="image " + str(num + 1) + " out of " + str(len(im_list)), anchor=E)
    if num == (len(im_list)-1):
        nextB = Button(root, text=">>", padx=10, command=lambda: next(num), state=DISABLED)
    else:
        nextB = Button(root, text=">>", padx=10, command=lambda: next(num))
    if num == 0:
        prevB = Button(root, text="<<", padx=10, command=lambda: prev(num), state=DISABLED)
    else:
        prevB = Button(root, text="<<", padx=10, command=lambda: prev(num))

    image.grid(row=0, column=0, columnspan=3)
    update.grid(row=2, column=2, sticky=E + W)
    prevB.grid(row=1, column=0)
    nextB.grid(row=1, column=2)


def prev(num):
    global im_list
    global image
    image.grid_forget()
    num -= 1
    image = Label(root, image=im_list[num])
    update = Label(root, text="image " + str(num + 1) + " out of " + str(len(im_list)), anchor=E)
    if num == (len(im_list) - 1):
        nextB = Button(root, text=">>", padx=10, command=lambda: next(num), state=DISABLED)
    else:
        nextB = Button(root, text=">>", padx=10, command=lambda: next(num))
    if num == 0:
        prevB = Button(root, text="<<", padx=10, command=lambda: prev(num), state=DISABLED)
    else:
        prevB = Button(root, text="<<", padx=10, command=lambda: prev(num))

    image.grid(row=0, column=0, columnspan=3)
    update.grid(row=2, column=2, sticky=E + W)
    prevB.grid(row=1, column=0)
    nextB.grid(row=1, column=2)

update = Label(root, text="image 1 out of " + str(len(im_list)), anchor=E)
image = Label(root, image=im1)
nextB = Button(root, text=">>", padx=10, command=lambda: next(num))
prevB = Button(root, text="<<", padx=10, command=lambda: prev(num), state=DISABLED)
exitB = Button(root, text="exit", padx=10, command=root.quit)

update.grid(row=2, column=2, sticky=E+W)
image.grid(row=0, column=0, columnspan=3)
prevB.grid(row=1, column=0)
nextB.grid(row=1, column=2)
exitB.grid(row=1, column=1)
root.mainloop()