from itertools import permutations
import numpy as np

n = input("input n \n")
perms = set(permutations(np.arange(int(n))))
print(len(perms))