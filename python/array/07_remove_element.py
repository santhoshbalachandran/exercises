# Given an array and a value, remove all instances of that value in-place and return the new array

# Example: nums = [3,2,2,3], val = 3 → [2,2]

# Time complexity: O(n^2) | Space complexity: O(1)
def remove_element_brute_force(arr, value):
    if not arr:
        return []
    
    value_count = 0
    k = -1
    
    for _ in range(len(arr)):
        k += 1
        print(f'k: {k}')
        if arr[k] == value:
            value_count += 1
            for j in range(k+1, len(arr)):
                arr[j-1] = arr[j]
            k -= 1
    return arr[:-value_count]

# Time complexity: O(n) | Space complexity: O(n)
def remove_element_extra_space(arr, value):
    if not arr:
        return []
    
    res = []
    for num in arr:
        if num != value:
            res.append(num)
    return res

# Time complexity: O(n) | Space complexity: O(1)
def remove_element_two_pointer(arr, value):
    if not arr:
        return []
    
    write_index = 0

    for read_index in range(len(arr)):
        if arr[read_index] != value:
            arr[write_index] = arr[read_index]
            write_index += 1
    
    return arr[:write_index]

if __name__ == '__main__':
    # arr = [3, 2, 2, 3, 1, 5]
    value = 3

    # arr = [3,3,3,3,3,3]
    arr = [3, 3, 3]
    
    # print(remove_element_extra_space(arr, value))
    # print(remove_element_brute_force(arr, value))
    print(remove_element_two_pointer(arr, value))