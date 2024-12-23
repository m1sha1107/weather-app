import numpy as np
from time import perf_counter
from time import sleep
import os
for i in range(100):
    print("\n")
os.system("color 2")
sleep(3.75)
n = 37 #max 37
wait = 0.7 #0.7
x = np.random.randint(10, size=(n))
prev = perf_counter()
count = 0
while True:
    now = perf_counter()
    diff = now - prev
    if diff > wait:
        count += 1
        #print(count)
        prev = perf_counter()
    if count == n:
        break
    y = np.random.randint(5, size=(n))
    y[0:count] = x[0:count]
    print(y)
sleep(2)
