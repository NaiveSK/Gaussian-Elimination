# Copyright (c) Su Kai 2019
# All rights reserved.
# Welcome to tell me you solution.
import pprint

mat = [[0, 2, 3, 4, 5, 90], # My instance for testing.
       [0, 0, 2, 8, 0, 0],
       [8, 0, 0, 0, 3, 6],
       [0, 4, 3, 3, 7, 88],
       [3, 4, 2, 9, 2, 2],
       [2, 2, 0, 2, 2, 9]]

def Read_matrix(matrix):
    global i, j
    i = len(matrix)
    j = len(matrix[0])
    print("The matrix is a ", i, " * ", j)

def Gaus_Eli(matrix):
    n = 0
    while n < i:
        for s in range(i - 1 - n):
            a = 1
            while matrix[n][n] == 0:
                try:
                    matrix[n], matrix[n + a] = matrix[n + a], matrix[n]
                    exc = matrix[n][n]
                except:
                    exc = 0
                    break
                if matrix[n][n] != 0:
                    break
                else:
                    a += 1
            try:
                if exc == 0: # This place still has a bug to be solved.
                    break
            except:
                pass
            time = matrix[n + s + 1][n] / matrix[n][n]
            for m in range(j):
                matrix[n + s + 1][m] = matrix[n + s + 1][m] - matrix[n][m] * time

        n += 1
    return matrix

def Simplify_matrix(mat): # To simplify the matrix, which cause a bug that can not be solved.
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] <= 10e-5:
                mat[i][j] = 0
    return mat

if __name__ == "__main__":
    pprint.pprint(mat)
    Read_matrix(mat)
    Gaus_Eli(mat)
    Simplify_matrix(mat) # I found that there are some numbers that too small, so I simplified them to zero.
    Gaus_Eli(mat)
    pprint.pprint(mat)

