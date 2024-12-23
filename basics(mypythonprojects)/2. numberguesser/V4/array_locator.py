narrow = [n for n in range(100)]
target = 22


split = 100
overhead = 0
guessed = False
guess = 0
while True:
    print(narrow)
    print(len(narrow))
    split = int(split / 2)
    if split < 1 or len(narrow) < 4:
        break
    #print("overhead= " + str(overhead) + " split= " + str(split))
    test = overhead + split
    ans = input("is your number less than " + str(test) + " ?")
    less = ans in "YESyesYes1"
    guess += 1
    narrowed = []
    if not(less):
        overhead += split
        for i in narrow:
            if i > test:
                narrowed.append(i)
        narrowed.insert(0, split)
    else:
        old = narrow.copy()
        for i in narrow:
            if i < test:
                narrowed.append(i)
    narrow = narrowed
for i in narrow:
    ans = input(f"is your number {i}?")
    guessed = ans in "YESyesYes1"
    guess += 1
    if guessed:
        print(f"guessed number {i} on guess number {guess}")
        break