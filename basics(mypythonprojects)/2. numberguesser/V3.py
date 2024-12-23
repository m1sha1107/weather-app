#Guesses the number user is thinking of from 0-100 within 10 guesses. 2023 design
split = 100
overhead = 0
guessed = False
guess = 0
while True:
    split = int(split / 2)
    if split < 1:
        break
    #print("overhead= " + str(overhead) + " split= " + str(split))
    test = overhead + split
    ans = input("is your number less than " + str(test) + " ?")
    less = ans in "YESyesYes1"
    guess += 1
    if not(less):
        overhead += split
for i in range(overhead, overhead + split + 3):
    ans = input("is your number " + str(i) + " ?")
    guessed = ans in "YESyesYes1"
    guess += 1
    if guessed:
        print(f"guessed number {i} on guess number {guess}")
        break
