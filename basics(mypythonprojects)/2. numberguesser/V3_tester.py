split = 100
overhead = 0
guessed = False
guess = 0
def user_compares(i, guess):
    return i<guess

avsum = 0
for num in range (1, 100):
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
        less = num<test
        guess += 1
        if not(less):
            overhead += split
    for i in range(overhead, overhead + split + 3):
        guessed = num==i
        guess += 1
        if guessed:
            print(f"guessed number {i} on guess number {guess}")
            break
    if num==i:
        print("GUESSED")
    else:
        print("NOT GUESSED")
    avsum += guess
print(f"average: {avsum/ 99}")