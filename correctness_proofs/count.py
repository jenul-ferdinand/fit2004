def count(arr, target):
    """
    ? LI:
    At the start of iteration i, count = no. of occurrences of target in
    arr[0..i-1]
    
    ? Init:
    i = 0
    count = 0
    LI: count = no. of occurrences of target in arr[0 .. 0-1] = Nothing yet.
    
    ? Maintenance:
    Assume true for i=k and arr[k] = target,
    Then we will increment count.
    But if arr[k] != target,
    Then we don't increment count.
    LI: count = no. of occurrences of target in arr[0 .. k-1].
    
    Because this is true at the start of iteration k, it holds for k + 1.
    
    ? Termination:
    i = n + 1
    LI: count = no. of occurrences of target in arr[1 .. n]
    
    Therefore this algorithm is correct.
    """
    n = len(arr)
    
    count = 0
    i = 0
    while i <= n:
        if arr[i] == target:
            count += 1
        i += 1
    
    return count