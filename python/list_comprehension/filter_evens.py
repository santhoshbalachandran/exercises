from typing import List

def filter_even_numbers(nums):
    if not nums:
        return []
    
    even_nums = []
    for n in nums:
        if n % 2 == 0:
            even_nums.append(n)
    
    even_nums.sort()
    return even_nums

def filter_even_numbers_list_comp(nums: List[int]) -> List[int]:
    return sorted([num for num in nums if num % 2 == 0])


if __name__ == "__main__":
    print(filter_even_numbers([5, 2, 8, 3, 11, 4]))
    print(filter_even_numbers_list_comp([5, 2, 8, 3, 11, 4]))