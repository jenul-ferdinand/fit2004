import time
import sys

sys.setrecursionlimit(10_000)

def fib(n: int) -> int:
    """
    Gives the n-th fibonacci number (without memoisation)
    """    
    if n == 0 or n == 1:
        return n
    
    return fib(n - 1) + fib(n - 2)

def fib_entry(n: int) -> int:
    """
    Entry point for the memoised fib function
    
    Creates the memo array with n+1 elements. memo[0]=0, memo[1]=1, the rest
    are -1 to indicate that we haven't saved anything.
    """
    memo = [-1] * (n+1)
    memo[0] = 0
    memo[1] = 1
    
    def fib_memo(n: int) -> int:
        """
        The memoised fib function
        """
        if memo[n] != -1:
            return memo[n]
        
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
        return memo[n]
    
    return fib_memo(n)
    


if __name__ == '__main__':
    start_time = time.time()
    result = fib(30)
    end_time = time.time()
    basic_total_time = end_time - start_time
    print(f'basic fib took {basic_total_time:.6f}, with result: {result}')
    
    start_time = time.time()
    result = fib_entry(1005)
    end_time = time.time()
    memo_total_time = end_time - start_time
    print(f'memo fib took {memo_total_time:.6f}, with result {result}')

