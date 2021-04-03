import numpy as np
import sys


d = 0

def guassian_elimination(A, B, d):
    
    n = len(A)
    for i in range(n):
        A[i].append(B[i])
    matrix = np.array(A)
    
    if (d==1):
        print(matrix)

    for i in range(n):
        if (matrix[i][i] == 0):
            for j in range(i+1, n):
                if (matrix[j][i] != 0):
                    matrix[[i, j]] = matrix[[j, i]]
                    break

        for j in range(i+1, n):
            matrix[j] -= matrix[i] * (matrix[j][i] / matrix[i][i])

    if (d==1):
        print(matrix)

    solution = [0 for  i in range(n)]
    for i in range(n-1, -1, -1):
        value = matrix[i][n]
        for j in range(i+1, n):
            value -= matrix[i][j] * solution[j]
        value /= matrix[i][i]
        solution[i] = value
    return solution


if __name__ == '__main__':
    if (len(sys.argv) > 1):
        if (sys.argv[1] == 'debug=true'):
            d = 1
    n = int(input())

    A = []
    for i in range(n):
        values = list(map(float, input().split()))
        A.append(values)
    B = []
    for i in range(n):
        value = float(input())
        B.append(value)

    solution = guassian_elimination(A, B, d)


    solution = [round(i, 4) for i in solution]
    for i in solution:
        print(i)


"""
3
25  5  1
64  8  1
144  12  1
106.8
177.2
279.2

3
2 4 8
2 4 6 
1 3 2
14
12
6

"""