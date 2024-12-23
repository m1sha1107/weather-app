#Guesses the number user is thinking of from 0-100 within 10 guesses. 2023 design
narrow = [n for n in range(100)]
def factor_reduction(narrow, fac):
    #when factors:
    does_factor = narrow.copy()
    for j in narrow:
        if not(j%fac==0):
            does_factor.remove(j)
    #when doesn't factor:
    doesnt_factor = narrow.copy()
    for j in narrow:
        if j%fac==0:
            doesnt_factor.remove(j)
    
    factor_prob = len(does_factor) / len(narrow)
    return factor_prob * len(does_factor) + (1 - factor_prob) * len(doesnt_factor)

split = 100
overhead = 0
guessed = False
guess = 0
fac = 2
while True:
    #print(narrow)
    #print(len(narrow))
    if split < 1 or len(narrow) < 3:
        break
    #print("overhead= " + str(overhead) + " split= " + str(split))

    fac_test = factor_reduction(narrow, fac)
    binary_test = int(len(narrow) / 2)
    #print(f"factor reduction: {fac_test} binary reduction {binary_test}")
    if fac_test < binary_test:
        #factor query
        ans = input(f"is your number divisible by {fac} ?")
        factors = ans in "YESyesYes1"
        guess += 1
        if factors:
            scale = narrow.copy()
            for j in scale:
                if not(j%fac==0):
                    narrow.remove(j)
        else:
            scale = narrow.copy()
            for j in narrow:
                if j%fac==0:
                    narrow.remove(j)
        fac += 1
    else:
        #binary query
        split = int(split / 2)
        test = overhead + split
        ans = input("is your number less than " + str(test) + " ?")
        less = ans in "YESyesYes1"
        guess += 1
        scale = narrow.copy()
        if not(less):
            overhead += split
            for i in scale:
                if i < test:
                    narrow.remove(i)
        else:
            for i in scale:
                if i >= test:
                    narrow.remove(i)

for i in narrow:
    ans = input(f"is your number {i}?")
    guessed = ans in "YESyesYes1"
    guess += 1
    if guessed:
        print(f"guessed number {i} on guess number {guess}")
        break

    