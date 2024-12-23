def predict_guesses(narrow):
    for target in narrow:
        avg_over = 1
        for j in range(avg_over): #averaging over:
            
            #binary locator:
            split = 100
            overhead = 0
            guessed = False
            guessn = 0
            while True:
                split = int(split / 2)
                if split < 1 or len(narrow) < 5:
                    break
                #print("overhead= " + str(overhead) + " split= " + str(split))
                test = overhead + split
                less = target<test
                guessn += 1
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
                guessed = i==target
                guessn += 1
                if guessed:
                    break
            sum_single += guessn
    avg = sum_single/ (avg_over *len(narrow))
    return avg