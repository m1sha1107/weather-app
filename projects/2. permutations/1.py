#numbers placed properly

import numpy as np
fact = np.math.factorial


# def sum(n):
#     if n == 0:
#         return 0
#     else:
#         return n + sum(n-1)

def perm(n):
    grid = np.array([[1 for i in range(n)] for j in range(fact(n))])
    #row_ext = 0
    #col_ext = 0

    def rec(n, grid):
        if False: #len(n) == 2:
            return None
        else:
            prev = 0
            for i in range(1, n+1):
                grid[prev:prev + fact(n-1), 0] = i
                prev = prev + fact(n-1)
                #rec(n-1, grid)
                #here try grid[each sub perm] = rec(perm[each sub perm])
            print(grid)
    
    grid = rec(n, grid)

perm(3)