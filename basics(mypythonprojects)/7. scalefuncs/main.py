import numpy as np
import time
import matplotlib.pyplot as plt

def timemults(func1, func2, func3):
        size = 300
        avs = 1
        list1, list2, list3 = [], [], []
        average1, average2, average3 = np.zeros((avs)), np.zeros((avs)), np.zeros((avs))

        for i in range(size):
            for j in range(avs):
                # m1 = np.random.rand(i, i) * 10
                # m2 = np.random.rand(i, i) * 10

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
        #plt.title("time taken by matrix multiplications with increase in input matrix size")
        plt.plot(r, list1, color="blue", label="mefs")
        plt.plot(r, list2, color="red", label="norm")
        plt.plot(r, list3, color="green", label="ident")
        plt.legend(loc="upper left")
        plt.show()


def identity(n):
    # sum = 0
    # while n > 0:
    #     sum += n
    #     n -= 1
    # return sum
    # # return np.sum(np.arange(n+1))
    pass

def mefs(n):
    # return n * (n+1) / 2
    pass

def norm(n):
    # sum = 0
    # for i in range(1, n+1):
    #     sum += i
    # return sum
    pass

print(identity(12))
print(mefs(12))
print(norm(12))
time.sleep(1)

timemults(mefs, norm, identity)