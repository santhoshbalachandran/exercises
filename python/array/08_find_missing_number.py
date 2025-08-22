# Given an array containing n distinct numbers in the range [0, n], find the one number missing.

# Example: [3, 0, 1] → Output: 2

def find_missing_sum(arr):
    n = len(arr)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    
    return expected_sum - actual_sum

if __name__ == '__main__':
    arr = [1,3,2]
    # print(find_missing_num_brute_force(arr))

    print(find_missing_sum(arr))
