import heapq

def find_kth_largest(nums: list[int], k: int) -> int:
    # Create max heap
    max_heap = [-elem for elem in nums]
    heapq.heapify(max_heap)
    
    # Pop out elements until, leaving the last
    while k >= 2:
        heapq.heappop(max_heap)
        print(max_heap)
        k -= 1
    
    # Return the last one
    return -heapq.heappop(max_heap)

if __name__ == '__main__':
    nums = [3,2,1,5,6,4]
    print(find_kth_largest(nums, 2))
    
    nums = [3,2,3,1,2,4,5,5,6]
    print(find_kth_largest(nums, 4))
    