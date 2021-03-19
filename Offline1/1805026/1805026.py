from math import sqrt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Constants
k = 0.5
pt = 3
previousRoot = np.NaN
delta = 0.000000000001


#Dictionary for the table
table = {
    "Iteration": [],
    "Low" : [],
    "High" : [],
    "Mid" : [],
    "Error" : [],
}

def f(x):
    if (x == 1):
        return np.NaN
    return (x / (1 - x))  * sqrt((2 * pt) / (2 + x)) - k

def clearTable():
    for key in table.keys():
        table[key] = []

def plotFunction():
    x_cord = np.linspace(-1.9999,1, 100)
    y = np.array([f(i) for i in x_cord] )
    fig = plt.figure()
    ax = plt.gca() 
    ax.spines['top'].set_color('none')  
    ax.spines['left'].set_position('zero') 
    ax.spines['right'].set_color('none') 
    ax.spines['bottom'].set_position('zero') 
    
    plt.xlim(-2, 2) 
    plt.ylim(-2, 2)
    plt.plot(x_cord, y) 
    plt.grid(True) 
    plt.show() 
    
def plotError():
    err = table["Error"]
    x_cord = list(range(1, len(err) + 1))
    plt.plot(x_cord, err)
    plt.grid(True)
    plt.show()
    
def bisection(low, high, error, max_iteration = 30):
    global previousRoot
    
    mid = (low + high) / 2
    
    current_error = np.NaN
    if (mid == 0):
        mid += delta
    if (previousRoot != np.NaN):
        current_error = abs(previousRoot - mid) / mid
    table["Iteration"].append(20 - max_iteration + 1)
    table["Low"].append(low)
    table["High"].append(high)
    table["Mid"].append(mid)
    table["Error"].append(current_error)
    
    if (max_iteration == 0 or current_error < error):
        return mid
    
    previousRoot = mid

    if (f(mid) * f(low) < 0):
        return bisection(low, mid, error, max_iteration - 1)
    else:
        return bisection(mid, high, error, max_iteration - 1)
    
# Calls Bisection Without error 
def bisectionWOError(low, high, max_iteration):
    return bisection(low, high, 0, max_iteration)
    
    
plotFunction()

# From the plot we observe the root lies in between 0 and 1
clearTable()
print(bisectionWOError(0, 1, 20))
plotError()
df = pd.DataFrame(table)
print(df)