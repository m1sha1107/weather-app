#guesses a number user is thinking of from 0-100 within 20 guesses. 2021 design
guess = 1
print("is your number even? (question "  + str(guess) + ")")
oddeve = input()
sub = 0
if oddeve in "YESyesYes":
    sub = 2
elif oddeve in "NOnoNo":
    sub = 1
else:
    print("invalid answer")

check = False
lessThan = 10
while check == False:
    guess += 1
    print("is your number less than " + str(lessThan) + "(question "+ str(guess) + ")")
    ans = input()
    if ans in "YESyesYes":
        check = True
    else:
        lessThan += 10

guessed = False
num = lessThan - sub
while num > 0 and guessed == False and guess <= 20:
    guess += 1
    print("is your number " + str(num) + "?" + "(guess "+ str(guess) + ")")
    ans = input()
    if ans in "YESyesYes":
        guessed = True
    else:
        num = num - 2
if num < 1 :
    print("negative numbers are not accepted")
elif guessed:
    print(f"guessed number {num} on guess {guess}")
x = input()
