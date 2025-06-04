def calc_arr(arr):
    """
    
    """
    n = len(arr) + 1
    total = 0
    
    for i in range(1, n):
        total += arr[i]
    
    return total