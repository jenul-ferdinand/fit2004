from colorama import Fore, init

init(autoreset=True)

INFINITY = float('inf')

def coins_change_top_down(coins: list, target: int):
    """
    Finds the minimum number of coins needed that add up to the target value
    given a set of coins.
    
    Recurrence:
        1. mc[0] = 0
        2. mc[T] = INFINITY if T > 0 and v < C[i] for all i
        Otherwise,
        3. mc[T] = min(1 + mc[T - C[i]]) 
    """
    memo = [-1] * (target+1)
    
    def solve(coins: list, target: int):
        # Reccurence case 1
        if target == 0: return 0
        
        if memo[target] == -1:
            # Recurrence case 2
            min_coins = INFINITY
            
            for i in range(len(coins)):
                if coins[i] <= target:
                    # Recurrence step 3
                    min_coins = min(min_coins,  1 + solve(coins, target - coins[i]))
                    
            memo[target] = min_coins
        
        return memo[target]
    
    return solve(coins, target)

if __name__ == '__main__':
    print('Bottom-up tests')
    print()
    print('Top-down tests')
    # Test 1
    coins = [1]
    target = 3
    result = coins_change_top_down(coins, target)
    print(f'{Fore.WHITE}Coins available: {coins}')
    print(f'Target value: ${target}')
    print(f'No. coins needed: {result} coins')
    assert result == 3, f'\n{Fore.RED}Failed!'
    print(f'{Fore.GREEN}Passed!')
    print()
    # Test 2
    coins = [2,3,9]
    target = 12
    result = coins_change_top_down(coins, target)
    print(f'{Fore.WHITE}Coins available: {coins}')
    print(f'Target value: ${target}')
    print(f'No. coins needed: {result} coins')
    assert result == 2, f'\n{Fore.RED}Failed!'
    print(f'{Fore.GREEN}Passed!')
    
    