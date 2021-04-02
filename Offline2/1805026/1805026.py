import numpy as np
import sys


d = 0

def guassian_elimination(matrix):
    global d
    
    n = len(matrix)
    matrix = np.array(matrix)
    
    if (d==1):
        print(matrix)

    for i in range(n):
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

    matrix = []
    for i in range(n):
        values = list(map(float, input().split()))
        matrix.append(values)

    for i in range(n):
        value = float(input())
        matrix[i].append(value)

    solution = guassian_elimination(matrix)


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
"""