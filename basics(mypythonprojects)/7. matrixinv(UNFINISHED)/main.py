#invert a matrix. first project since july 2022
import numpy as np


inp = np.zeros((3, 3), dtype=np.float64)
inpstr = input("input matrix as __ __ __ __... \n")
#to parse input
num = ""
row = 0 
column = 0 
for i in inpstr:
    if i.isnumeric():
        num += i
    elif i.isspace():
        inp[row, column] = int(num)
        num = ""
        column += 1
        if column >=3:
            column = 0
            row += 1

class Matrixops:
    def twosdet(input):
        
