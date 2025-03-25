from random import randrange

def quick_select(array: list, lo: int, hi: int, k: int) -> float | int | str:
    """
    * QuickSelect finds the k-th smallest element in an unordered list.
    
    Similar to QuickSort, it selects a pivot and partitions the array, but only
    recurses into one partition instead of both, giving average O(n) time complexity.
    
    Parameters:
    -----------
    array : list
        The input array to search in
    lo : int
        The lower index of the current subarray
    hi : int
        The upper index of the current subarray
    k : int
        The index of the element to find (0 indexed)
    
    Returns:
    --------
    element : float | int | str
        The k-th smallest element in the array
        
    Time Complexity:
    ----------------
    - Average Case: O(n)

    Space Complexity:
    -----------------
    O(log n) for the recursion stack in the average case.
    
    Example:
    --------
    >>> arr = [3,1,4,5,2]
    >>> quick_select(arr, 0, len(arr)-1, 2) # Find the 3rd smallest element (index 2)
    3
    """
    if hi > lo:
        pivot_index = randrange(lo, hi)
        mid = naive_partition(array, lo, hi, pivot_index)
        if k < mid:
            return quick_select(array, lo, mid-1, k)
        elif k > mid:
            return quick_select(array, mid+1, hi, k)
        elif k == mid:  
            return array[k]
    else:
        return array[k]
        
        

def naive_partition(array: list, lo: int, hi: int, pivot_index: int = None) -> int:
    """
    * Naive partitioning shceme (Lumoto)
    
    Returns the final position of the pivot
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if pivot_index is None:
        pivot_index = randrange(lo, hi)
        
    # Move the pivot to the end 
    if pivot_index != hi:
        array[pivot_index], array[hi] = array[hi], array[pivot_index]
        
    pivot = array[hi]
    j = lo
    
    for i in range(lo, hi):
        if array[i] <= pivot:
            array[i], array[j] = array[j], array[i]
            j = j + 1
        
    array[hi], array[j] = array[j], array[hi]
    
    return j



if __name__ == '__main__':
    nums = [1,2,3,4,5]
    print(quick_select(nums, 0, len(nums)-1, 0))
    
    # Test 1: Simple sorted array
    nums1 = [1, 2, 3, 4, 5]
    for i in range(len(nums1)):
        result = quick_select(nums1, 0, len(nums1)-1, i)
        assert result == nums1[i], f"Expected {nums1[i]}, got {result}"
    
    # Test 2: Unsorted array
    nums2 = [3, 1, 4, 5, 2]
    # Expected sorted order: [1, 2, 3, 4, 5]
    expected = sorted(nums2)
    for i in range(len(nums2)):
        result = quick_select(nums2, 0, len(nums2)-1, i)
        assert result == expected[i], f"Expected {expected[i]}, got {result}"
    
    # Test 3: Array with duplicates
    nums3 = [3, 3, 1, 2, 2, 5]
    # Expected sorted order: [1, 2, 2, 3, 3, 5]
    expected = sorted(nums3)
    for i in range(len(nums3)):
        result = quick_select(nums3, 0, len(nums3)-1, i)
        assert result == expected[i], f"Expected {expected[i]}, got {result}"
    
    # Test 4: Single element array
    nums4 = [42]
    assert quick_select(nums4, 0, 0, 0) == 42
    
    print("All tests passed! QuickSelect is working correctly.")