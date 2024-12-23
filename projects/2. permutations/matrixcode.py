import numpy as np
from itertools import permutations
import time
import matplotlib.pyplot as plt
# to compare the performance of synchronous and asynchronous matrix multiplication

def timemults(func1, func2, func3):
    size = 9
    avs =5
    list1, list2, list3 = [], [], []
    average1, average2, average3 = np.zeros((avs)), np.zeros((avs)), np.zeros((avs))

    for i in range(size):
        for j in range(avs):
            m1 = np.random.rand(i, i) * 10
            m2 = np.random.rand(i, i) * 10

            a = time.perf_counter()
            _ = func1(i)
            b = time.perf_counter()
            average1[j] = b-a

            a = time.perf_counter()
            _ = func2(i)
            b = time.perf_counter()
            average2[j] = b-a
            
            a = time.perf_counter()
            _ = func3(m1,m2)
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
    #plt.title("time taken by matrix multiplications with increase in input matrix size")
    plt.plot(r, list1, color="blue", label="custom")
    plt.plot(r, list2, color="red", label="lib")
    #plt.plot(r, list3, color="green", label="np.matmul")
    plt.legend(loc="upper left")
    plt.show()

def fact(n):
    prod = 1
    for i in range(1, n+1):
        prod = prod * i
    return prod

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
    return grid

def ident(n):
    return set(permutations(np.arange(int(n))))

timemults(perm, ident, np.matmul)
