from math import log

#constants

m_o = 140000    # initial mass
q = 2100        # consumption rate of fuel
u = 2000        # velocity of expelled fuel
g = 9.8         # acceleration due to gravity

def func(t):
    return u * log(m_o / (m_o - q * t)) - g * t


def integrate(low, high, n, func):
    del_x = (high - low) / n
    area = 0
    for i in range(n):
        trapezium = 0.5 * (func(low) + func(low + del_x)) * del_x
        low += del_x
        area += trapezium
    return area

def simpsons_integral(low, high, n, func):
    del_x = (high - low)/(2*n)
    area = 0

    for i in range(n):
        dA  = (del_x / 3) * (func(low) + 4*func(low + del_x) + func(low + 2*del_x))
        low += 2*del_x
        area += dA
    
    return area

n = int(input("Enter no of intervals : "))

print("The required integral using trapezoid rule is ", integrate(8, 30, n, func))

last = integrate(8, 30, 1, func)
print("n =", 1, "value = ",round(last, 5), "error = ", None)
for i in range(2, 6):
    cur =  integrate(8, 30, i, func)
    print("n =", i, "value = ",round(cur,5) , "error = ", round(abs(cur - last) * 100 / cur, 5) )
    last = cur
    

print("\n\nThe required integral using simpsons rule is ", simpsons_integral(8, 30, n, func))

last = simpsons_integral(8, 30, 1, func)
print("n =", 1, "value = ",round(last, 5), "error = ", None)
for i in range(2, 6):
    cur =  simpsons_integral(8, 30, i, func)
    print("n =", i, "value = ",round(cur,5) , "error = ", round(abs(cur - last) * 100 / cur, 5) )
    last = cur
