perps = [i for i in range(100)]
for i in range(2, 8):
    ans = input(f"is your number divisible by {i} ?")
    factors = ans in "YESyesYes1"
    if factors:
        scale = perps.copy()
        for j in scale:
            if not(j%i==0):
                perps.remove(j)
    else:
        scale = perps.copy()
        for j in scale:
            if j%i==0:
                perps.remove(j)
    print(perps)