from tkinter import * #imports all functions from tkinter
root = Tk() #creates root window 
root.title("calc")
#root.iconbitmap(r"C:\Users\vpkam\Desktop\yes.ico")
e = Entry(root, width=40,borderwidth=5) #input box 
e.grid(row=0, column=0, columnspan=4)
nums = [] #list to store all teh numbers 

#initial initialization of flags for each operation
add = False
sub = False
mul = False
div = False

#function to handle button clicks
def clicked(n):
    current = e.get() #adds to entry box
    e.delete(0, END) #clears the entry box
    e.insert(0, current + str(n)) #updates the entry box
    nums.append(n)


#function triggers calculation and displays the result
def equals():
    s = "".join(nums) #concatonates into a single string
    e.delete(0, END)
    global add, sub, mul, div
    add = sub = mul = div = mod = False  #reset all operation flags

    #identify which operator is present in the string
    if "+" in s:
        add = True
    elif "-" in s:
        sub = True
    elif "*" in s:
        mul = True
    elif "/" in s:
        div = True
    elif "%" in s:  
        mod = True
    else:
        mod = False

   #performs respective calculation
    if add: #handles addition operation
        numbers = s.split("+")
        result = sum(int(i) for i in numbers)  #runs a for loop to calculate sum 
        e.insert(0, result) #updates the entry box

    elif sub: #handles subtraction operation
        numbers = s.split("-")
        result = int(numbers[0])  #start with the first number
        for i in range(1, len(numbers)):
            result -= int(numbers[i])  #subtract subsequent numbers
        e.insert(0, result)

    elif mul: #handles multiplication operation
        numbers = s.split("*")
        result = 1  
        for i in numbers:
            result *= int(i)  # run a for loop to multiply all numbers
        e.insert(0, result)

    elif div: #handles division operation
        numbers = s.split("/")
        result = int(numbers[0]) 
        for i in range(1, len(numbers)):
            if int(numbers[i]) != 0:
                result /= int(numbers[i])  #divide by subsequent numbers
            else:
                e.insert(0, "Error")  # error handling
                return
        e.insert(0, result)

    elif mod:  # Handle modulus operation
        numbers = s.split("%")
        result = int(numbers[0]) % int(numbers[1])  # Perform modulus
        e.insert(0, result)

    nums.clear()  #clears the list after calculation
    nums.append(e.get())  #stores the results for further operations

#function to clear the entry box 
def clear():
    nums.clear()
    e.delete(0, END)

#function that runs blank space button 
def delete():
    string = e.get()
    e.delete(0, END)
    lists = []
    for i in range(0,len(string)-1):
        lists.append(string[i])
    x = "".join(lists)
    e.insert(0, x)


#initializes buttons
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
Bmul = Button(root, text="x", padx=32, pady=20, command=lambda: clicked("x"))
Bdiv = Button(root, text="/", padx=32, pady=20, command=lambda: clicked("/"))
Bmod = Button(root, text="%", padx=32, pady=20, command=lambda: clicked("%"))

Bclear = Button(root, text="clear", padx=24, pady=20, command=lambda: clear())
Bdelete = Button(root, text="space", padx=17, pady=20,command=lambda: delete())

#sets the grid for display
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
Beaquals.grid(row=6, column=2,)

Bclear.grid(row=6, column=0,)
Bdelete.grid(row=6,column=1)

Badd.grid(row=4, column=1)
Bsub.grid(row=4, column=2)
Bmul.grid(row=5, column=0)
Bdiv.grid(row=5, column=1)
Bmod.grid(row=5, column=2)

root.mainloop()