def bisection(low, high, error, max_iteration = 30):
    global previousRoot
    
    mid = (low + high) / 2
    
    current_error = np.NaN;
    if (mid == 0):
        mid += delta
    if (previousRoot != np.NaN):
        curre