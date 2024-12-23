import numpy as np
import time
import matplotlib.pyplot as plt
import concurrent.futures
# to compare the performance of synchronous and asynchronous matrix multiplication

def timemults(func1, func2, func3):
    size = 30
    avs = 3
    list1, list2, list3 = [], [], []
    average1, average2, average3 = np.zeros((avs)), np.zeros((avs)), np.zeros((avs))

    for i in range(size):
        for j in range(avs):
            m1 = np.random.rand(i, i) * 10
            m2 = np.random.rand(i, i) * 10

            a = time.perf_counter()
            _ = func1(m1, m2)
            b = time.perf_counter()
            average1[j] = b-a

            a = time.perf_counter()
            _ = func2(m1, m2)
            b = time.perf_counter()
            average2[j] = b-a
            
            a = time.perf_counter()
            _ = func3(m1, m2)
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
    plt.plot(r, list1, color="blue", label="np.matmul")
    plt.plot(r, list2, color="red", label="synchronous")
    plt.plot(r, list3, color="green", label="concurrent")
    plt.legend(loc="upper left")
    plt.show()

def syncmult(m1, m2):
    #print("entered")
    prod = np.zeros((m1.shape[0], m2.shape[1]))
    for i in range(m1.shape[0]):
        for j in range(m2.shape[1]):
            vec1 = m1[i]
            vec2 = m2[:, j]
            #print(f"iter {i}, {j}")
            #print(vec1)
            #print(vec2)
            sum = 0
            for k, l in zip(vec1, vec2):
                sum += k * l
            prod[i][j] = sum
    return prod



def asyncmult(m1, m2):
    threads = []
    prod = np.zeros((m1.shape[0], m2.shape[1]))
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for i in range(m1.shape[0]):
            for j in range(m2.shape[1]):
                f = executor.submit(multvecs, (m1[i], m2[:, j], (i, j)))
                threads.append(f)
        for f in concurrent.futures.as_completed(threads):
            vprod, index = f.result()
            i, j = index
            prod[i][j] = vprod
    return prod

def multvecs(inp):
    v1, v2, index = inp
    sum = 0
    for i in range(v1.shape[0]):
        sum += v1[i] * v2[i]
    return sum, index


m1 = np.random.rand(5, 4) * 10
m2 = np.random.rand(4, 3) * 10

true = np.matmul(m1, m2)
custom = asyncmult(m1 ,m2)
print("result:")
print(true)
print(custom)

timemults(asyncmult, syncmult, np.matmul)