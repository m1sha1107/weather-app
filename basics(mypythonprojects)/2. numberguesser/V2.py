primePre50 = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47) #discluding 2
primePost50 =(53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
compPre50 =(4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49)
compPost50 =(50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72, 74, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100)
eve = False
pre50 = False
prime = False
guessed = False
guess = 1
print("is your number even? (guess " + str(guess) + ")")
oddevecheck = input()
if oddevecheck in "YESyesYes":
    eve = True
elif oddevecheck in "NOnoNo":
    eve = False
lessthan = input("is your number less than 50? (guess " + str(guess) + ")")
guess += 1
if lessthan in "YESyesYes":
    pre50 = True
elif lessthan in "NOnoNo":
    pre50 = False
primecheck = input("is your number prime? (guess " + str(guess) + ")")
guess += 1
if primecheck in "YESyesYes":
    prime = True
elif primecheck in "NOnoNo":
    prime = False

if prime and pre50 and eve:
    two = input("is your number two? (guess " + str(guess) + ")")

    if two in "YESyesYes":
        guessed = True
else:
    if prime and pre50:
        for i in primePre50:
            print("is your number " + str(i) + "?" + "(guess " + str(guess) + ")")
            ans = input()
            if ans in "YESyesYes":
                guessed = True
                break
    if prime == False and pre50:
        for i in compPre50:
            print("is your number " + str(i) + "?" + "(guess " + str(guess) + ")")
            ans = input()
            if ans in "YESyesYes":
                guessed = True
                break
    if prime and pre50 == False:
        for i in primePost50:
            print("is your number " + str(i) + "?" + "(guess " + str(guess) + ")")
            ans = input()
            if ans in "YESyesYes":
                guessed = True
                break
    if prime == False and pre50 == False:
        for i in compPost50:
            print("is your number " + str(i) + "?" + "(guess " + str(guess) + ")")
            ans = input()
            if ans in "YESyesYes":
                guessed = True
                break
if guessed and guess <= 20:
    print("you lose")
else:
    print("you win")

