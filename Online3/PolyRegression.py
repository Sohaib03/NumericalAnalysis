import numpy as np
import matplotlib.pyplot as plt

order = int(input())

#n = int(input())

xs = []
ys = []

# for i in range(n):
#     inp = input().split()
#     x, y =  [float(i) for i in inp]

#     xs.append(x)
#     ys.append(y)

with open("data.txt", 'r') as datafile:
    lines = datafile.readlines()

    for xy in lines:
        #print(xy)
        x, y = [float(j) for j in xy.strip().split()]
        xs.append(x)
        ys.append(y)

n = len(xs)
print(n)
matrix = []

for i in range(0, order+1):
    
    row = []


    for j in range(0, order+1):
        sum = 0

        for x in xs:
            sum += x ** (i+j)

        row.append(sum)
    
    y_sum = 0

    for j in range(n):
        y_sum += (xs[j]**i) * ys[j]

    row.append(y_sum)

    matrix.append(row)

def guassian_elimination(matrix):
    
    n = len(matrix)
    matrix = np.array(matrix)
    
    for i in range(n):
        for j in range(i+1, n):
            matrix[j] -= matrix[i] * (matrix[j][i] / matrix[i][i])


    solution = [0 for  i in range(n)]
    for i in range(n-1, -1, -1):
        value = matrix[i][n]
        for j in range(i+1, n):
            value -= matrix[i][j] * solution[j]
        value /= matrix[i][i]
        solution[i] = value
    return solution

solution = guassian_elimination(matrix)

plt.scatter(xs, ys, 1)

def f(coeffs, x):
    value = 0
    xp = 1
    for c in coeffs:
        value += c * xp
        xp *= x

    return value


x_points = np.arange(min(xs), max(xs), 0.01)
y_points = [f(solution, k) for k in x_points]


plt.plot(x_points, y_points, color='orange')
plt.show()

print(solution)

"""
3
7
80 0.00000647
40 0.00000624
-40 0.00000572
-120 0.00000509
-200 0.00000430
-280 0.00000333
-340 0.00000245

3
7
80 647
40 624
-40 572
-120 509
-200 430
-280 333
-340 245

"""