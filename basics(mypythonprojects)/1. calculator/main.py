from tkinter import *
root = Tk()
root.title("calc")
#root.iconbitmap(r"C:\Users\vpkam\Desktop\yes.ico")
e = Entry(root, width=40,borderwidth=2)
e.grid(row=0, column=0, columnspan=3)
nums = []
add = False
sub = False
def clicked(n):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(n))
    nums.append(n)

def equals():
    s = "".join(nums)
    e.delete(0, END)
    add = True
    for i in s:
        if i == "+":
            add = True
        if i == "-":
            add = False
    if add == True:
        sum = 0
        numbers = s.split("+")
        print("adding")
        print(numbers)
        for i in numbers:
            sum += int(i)
        e.insert(0, sum)
    else:
        numbers = s.split("-")
        print("subtracting")
        print(numbers)
        diff = int(numbers[0])
        for i in range(1, len(numbers)):
            diff = diff - int(numbers[i])
        e.insert(0, diff)
    nums.clear()
    ans = e.get()
    nums.append(ans)


def clear():
    nums.clear()
    e.delete(0, END)

def delete():
    string = e.get()
    e.delete(0, END)
    lists = []
    for i in range(0,len(string)-1):
        lists.append(string[i])
    x = "".join(lists)
    e.insert(0, x)

B1 = Button(root, text="1", padx=32, pady=20, command=lambda: clicked("1"))
B2 = Button(root, text="2", padx=32, pady=20, command=lambda: clicked("2"))
B3 = Button(root, text="3", padx=32, pady=20, command=lambda: clicked("3"))
B4 = Button(root, text="4", padx=32, pady=20, command=lambda: clicked("4"))
B5 = Button(root, text="5", padx=32, pady=20, command=lambda: clicked("5"))
B6 = Button(root, text="6", padx=32, pady=20, command=lambda: clicked("6"))
B7 = Button(root, text="7", padx=32, pady=20, command=lambda: clicked("7"))
B8 = Button(root, text="8", padx=32, pady=20, command=lambda: clicked("8"))
B9 = Button(root, text="9", padx=32, pady=20, command=lambda: clicked("9"))
B0 = Button(root, text="0", padx=32, pady=20, command=lambda: clicked("0"))
Beaquals = Button(root, text="=", padx=32, pady=20, command=lambda: equals())
Badd = Button(root, text="+", padx=32, pady=20, command=lambda: clicked("+"))
Bsub = Button(root, text="-", padx=32, pady=20, command=lambda: clicked("-"))
Bclear = Button(root, text="clear", padx=24, pady=20, command=lambda: clear())
Bdelete = Button(root, text="Bspace", padx=17, pady=20,command=lambda: delete())

B1.grid(row=1, column=0)
B2.grid(row=1, column=1)
B3.grid(row=1, column=2)

B4.grid(row=2, column=0)
B5.grid(row=2, column=1)
B6.grid(row=2, column=2)

B7.grid(row=3, column=0)
B8.grid(row=3, column=1)
B9.grid(row=3, column=2)

B0.grid(row=4, column=0)
Beaquals.grid(row=5, column=2,)

Badd.grid(row=4, column=1)
Bclear.grid(row=5, column=0,)
Bdelete.grid(row=5,column=1)
Bsub.grid(row=4, column=2)
root.mainloop()
