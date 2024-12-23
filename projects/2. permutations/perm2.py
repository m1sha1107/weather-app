def permute(x):
    if len(x) == 1:
        print(str(x[0]), end="\n")
    else:
        for i in x:
            y = [j for j in x if j != i]
            print(str(i), end="")
            permute(y)

n = int(input("input n \n"))
permute([i for i in range(1, n+1)])

