# Find the smallest number in an array

def find_smallest_number(arr):
    if not arr:
        return -1
    
    smallest = arr[0]
    for num in arr[1:]:
        if smallest > num:
            smallest = num
    return smallest

if __name__ == "__main__":
    arr = [-1, -5, 0, -10]
    print(find_smallest_number(arr))