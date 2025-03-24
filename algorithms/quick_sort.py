from typing import List

def naive(arr: List, low: int, high: int):
    '''
    Naive partitioning scheme (with QuickSort)
    
    https://youtu.be/f_9itSjoMVo
    
    Time Complexity:
    - Best Case: O(nlogn)
    - Average Case: O(nlogn)
    - Worst Case: O(n^2)
    
    Space Complexity: O(logn)
    '''
    # Base Case
    if low >= high:
        return
    
    # Partitioning
    pivot = arr[high]
    j = low
    
    for i in range(low, high):
        if arr[i] <= pivot:
            # Swap element at i and j
            arr[i], arr[j] = arr[j], arr[i]
            
            j = j + 1
            
    # Swap element at j with pivot
    arr[high], arr[j] = arr[high], arr[j]
    
    # Recursive Step
    naive(arr, low, j-1)
    naive(arr, j+1, high)
    
    return arr



def hoares(arr: List, low: int, high: int):
    '''
    Hoare's partitioning scheme (with QuickSort)
    
    https://youtu.be/qwzWH36FX60

    This scheme is in-place but not stable
    
    Time Complexity:
    - Best Case: O(nlogn)
    - Average Case: O(nlogn)
    - Worst Case: O(n^2)
    
    Space Complexity: O(logn)
    '''
    # Base Case
    if low >= high:
        return
    
    # Partitioning
    pivot = arr[high]
    i = low
    j = high
    
    while i < j:
        while arr[i] < pivot:
            i = i + 1
        
        while arr[j] > pivot:
            j = j - 1 
            
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    
    # Recursive Step        
    hoares(arr, low, i-1)
    hoares(arr, i, high)
    
    return arr


if __name__ == '__main__':
    unsorted_arr = [5,4,3,6,3,2,1,7,6,5,3,5,55,32]
    sorted_arr = hoares(unsorted_arr, 0, len(unsorted_arr)-1)
    print(sorted_arr)
    
    sorted_arr = naive(unsorted_arr, 0, len(unsorted_arr)-1)
    print(sorted_arr)