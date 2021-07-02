
n = int(input())

xs = []
ys = []

sum_x = 0
sum_y = 0
sum_xy = 0
sum_x_squared = 0

for i in range(n):
    inp = input().split()
    x, y =  [float(i) for i in inp]

    xs.append(x)
    ys.append(y)

    sum_x_squared += x * x
    sum_xy += x * y
    sum_x += x
    sum_y += y

a1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x * sum_x)
a0 = (sum_y/n - a1 * sum_x/n)


print(a0, a1)


## y = a0 + a1 * x

"""
5
0.698132 0.188224
0.959931 0.209138
1.134464 0.230052
1.570796 0.250965
1.919862 0.313707
"""
