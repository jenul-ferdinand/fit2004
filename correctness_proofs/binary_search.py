import math

def binary_search(arr, target):
    """
    
    """
    n = len(arr) + 1
    
    lo = 1
    hi = n + 1
    
    while (lo < hi - 1):
        mid = math.floor((lo + hi) / 2)
        if target >= arr[mid]:
            lo = mid
        if target < arr[mid]:
            hi = mid
        if arr[lo] == target:
            return lo
    
    return math.inf