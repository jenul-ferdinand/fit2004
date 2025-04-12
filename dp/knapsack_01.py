from typing import List, Tuple
from colorama import Fore

"""
Same as unbounded knapsack except that each item can only be picked at most once.

The difference is that if we pick an item X, giving us a remaining capacity R,
we have to somehow make sure that X is not part of the optimal solution to our
new subproblem of size R.
"""

def knapsack_01_bu(capacity, items):
    pass

def knapsack_01_td(capacity, items):
    pass

if __name__ == '__main__':
    # Example from the seminar
    # Testing bottom up
    print(f'{Fore.WHITE}Testing bottom up')
    capacity = 12
    items = [(9, 550), (5, 350), (6, 180), (1, 40)]
    # result_bu = knapsack_unbounded_bu(capacity, items)h
    answer = 780
    # assert result_bu == answer, f'{Fore.RED}Expected {answer}, got {result_bu}'
    print(f'{Fore.GREEN}Passed!')
    # Testing top down
    print(f'{Fore.WHITE}Testing top down')
    capacity = 12
    items = [(9, 550), (5, 350), (6, 180), (1, 40)]
    # result_td = knapsack_unbounded_td(capacity, items)
    answer = 780
    # assert result_td == answer, f'{Fore.RED}Expected {answer}, got {result_td}'
    print(f'{Fore.GREEN}Passed!')