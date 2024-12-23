import numpy as np
import time

def custom(arr):
    large = 0
    slarge = 0
    for i in range(len(arr)):

        if arr[i] > large:
            slarge=large
            large = arr[i]
        else:
            if arr[i] > slarge:
                slarge = arr[i]
    return slarge

def custom2(arr):
    large = 0
    slarge = 0
    for i in range(len(arr)):
        if arr[i] > large:
            slarge=large
            large = arr[i]
        else:
            if arr[i] > slarge:
                slarge = arr[i]
    return slarge

def standard(arr):
    arr = np.sort(arr, kind='quicksort')
    return arr[-2]

#testing
n = 30
length = 100
avs, avc = 0, 0
s, c = [], []
for j in range(5, length + 5):
    for i in range(n):
        arr = np.arange(j)
        arr = np.random.permutation(arr)
        x = time.perf_counter()
        a = standard(arr)
        y = time.perf_counter()
        avs += (y - x)

        x = time.perf_counter()
        a = custom(arr)
        y = time.perf_counter()
        avc += (y - x)
    s.append(avs / n)
    c.append(avc / n)

import matplotlib.pyplot as plt

#plt.rcParams["figure.figsize"] = [7.50, 3.50]
#plt.rcParams["figure.autolayout"] = True
plt.title("time taken plotted against length")
r = np.arange(length + 5)[5:]
plt.plot(r, s, color="blue")
plt.plot(r, c, color="red")
plt.show()

print("sort time:")
print(np.average(avs))
print("custom time:")
print(np.average(avc))
