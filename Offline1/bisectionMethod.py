from math import sqrt
import pandas as pd

k = 0.5
pt = 3


table = {
    "Iteration": [],
    "Low" : [],
    "High" : [],
    "Mid" : [],
    "Error" : [],
}

def f(x):
    return (x / (1 - x))  * sqrt((2 * pt) / (2 + x)) - k


def bisection(low, high, error, max_iteration = 20):
    mid = (low + high) / 2
    
    current_error = (high - low) / (high + low);
    table["Iteration"].append(20 - max_iteration + 1)
    table["Low"].append(low)
    table["High"].append(high)
    table["Mid"].append(mid)
    table["Error"].append(current_error)
    
    if (max_iteration == 0 or current_error < error):
        return mid

    mid_val = f(mid)
    #print(low, high, mid, mid_val)
    if (mid_val > 0):
        return bisection(low, mid, error, max_iteration - 1)
    else:
        return bisection(mid, high, error, max_iteration - 1)
    

print(bisection(0, 1, 0.005))
#print(table)

df = pd.DataFrame(table)
print(df)