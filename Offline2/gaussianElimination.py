import numpy as np


def guassian_elimination(matrix):
    n = len(matrix)
    matrix = np.array(matrix);

    for i in range(n):
        matrix[i] /= matrix[i][i]
        for j in range(i+1, n):
            matrix[j] -= matrix[i] * matrix[j][i]

    for i in range(n-1, -1, -1):
        for j in range(i-1, -1, -1):
            matrix[j] -= matrix[i] * matrix[j][i];

    solution = []
    for i in matrix:
        solution.append(i[n])
    return solution


if __name__ == '__main__':
    n = int(input())

    matrix = []
    for i in range(n):
        values = list(map(float, input().split()))
        matrix.append(values)

    for i in range(n):
        value = float(input())
        matrix[i].append(value)

    print(matrix)
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