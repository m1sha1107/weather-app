import statistics
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
    return  factor_prob * len(does_factor) + (1 - factor_prob) * len(doesnt_factor)

guesses = []
facentry = 0
for num in range(1, 100):
    narrow = [n for n in range(100)]
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
            facentry += 1
            factors = num%fac==0
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
            less = num<test
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
        guessed = i==num
        guess += 1
        if guessed:
            print(f"guessed number {i} on guess number {guess}")
            break
    if num==i:
        print("GUESSED")
    else:
        print("NOT GUESSED")
    guesses.append(guess)

res = []
mean_val = statistics.mean(guesses)
for ele in guesses:
   res.append(abs(ele - mean_val))

print(f"average: {statistics.mean(guesses)}")
print(f"variance: {statistics.mean(res)}")
print(f"max: {max(guesses)}")
print(f"average factor queries per num: {facentry / 99}")