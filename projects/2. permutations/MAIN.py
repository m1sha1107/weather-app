import numpy as np

n = int(input("input n \n"))

def fact(n):
    prod = 1
    for i in range(1, n+1):
        prod = prod * i
    return prod

# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
def perm(n):
    grid = np.array([[1 for i in range(n)] for j in range(fact(n))])
    x = n + 1
    
    def rec(n, grid, history):
        prev = 0
        run = True
        for i in range(1, x):
            for j in history:
                if j == i:
                    run = False
            if run:
                looplist = history.copy()
                looplist.append(i)
                grid[prev:prev + fact(n-1), 0] = i
                grid[prev:prev + fact(n-1), 1:] = rec(n-1, grid[prev:prev + fact(n-1), 1:], looplist)
                prev = prev + fact(n-1)
            run = True
        return grid
    
    grid = rec(n, grid, [])
    
    for i in grid:
        print(i)

perm(n)
