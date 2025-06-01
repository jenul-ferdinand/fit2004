def find_min(arr):
    """
    
    """
    n = len(arr) + 1
    
    min = arr[1]
    i = 2
    while i <= n:
        if arr[i] < min:
            min = arr[i]
        i += 1
        
    return min