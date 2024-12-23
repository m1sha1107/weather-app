import numpy as np
import time
import matplotlib.pyplot as plt
import itertools
import math
# to compare the performance of synchronous and asynchronous matrix multiplication

def timemults(func1, name1, func2, name2, func3, name3, size, avs):
    list1, list2, list3 = [], [], []
    average1, average2, average3 = np.zeros((avs)), np.zeros((avs)), np.zeros((avs))

    for i in range(size):
        for j in range(avs):

            a = time.perf_counter()
            _ = func1(i)
            b = time.perf_counter()
            average1[j] = b-a

            a = time.perf_counter()
            _ = func2(i)
            b = time.perf_counter()
            average2[j] = b-a
            
            a = time.perf_counter()
            _ = func3(i)
            b = time.perf_counter()
            average3[j] = b-a
        list1.append(np.average(average1))
        list2.append(np.average(average2))
        list3.append(np.average(average3))
        average1, average2, average3 = np.zeros((avs)), np.zeros((avs)), np.zeros((avs))
        print(i)
    
    #plt.rcParams["figure.figsize"] = [7.50, 3.50]
    #plt.rcParams["figure.autolayout"] = True
    r = np.arange(size)
    plt.title("time taken by matrix multiplications with increase in input matrix size")
    plt.plot(r, list1, color="blue", label=name1)
    plt.plot(r, list2, color="red", label=name2)
    plt.plot(r, list3, color="green", label=name3)
    plt.legend(loc="upper left")
    plt.show()

def fact(n):
    prod = 1
    for i in range(1, n+1):
        prod = prod * i
    return prod

def perm_custfact(n):
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
    return grid

def perm_mathfact(n):
    grid = np.array([[1 for i in range(n)] for j in range(math.factorial(n))])
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
                grid[prev:prev + math.factorial(n-1), 0] = i
                grid[prev:prev + math.factorial(n-1), 1:] = rec(n-1, grid[prev:prev + math.factorial(n-1), 1:], looplist)
                prev = prev + math.factorial(n-1)
            run = True
        return grid
    
    grid = rec(n, grid, [])
    return grid

def with_nump(n):
    perm_list = list(itertools.permutations(range(1, n + 1)))
    matrix = np.array(perm_list)
    return matrix

def with_itertools(n):
    permutations = list(itertools.permutations(range(1, n + 1)))
    matrix = []
    for perm in permutations:
        matrix.append(list(perm))
    return matrix

n = 4
#perm_out = perm(n)
#nump_out = with_nump(n)
#iter_out = with_itertools(n)
#print("custom:")
#print(perm_out)
#print("numpy:")
#print(nump_out)
#print("itertool:")
#print(iter_out)

timemults(perm_custfact, "custom factorial", perm_mathfact, "library factorial", with_itertools, "with itertools", 11, 3)