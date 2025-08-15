# Find the second largest number in an array. Return -1 if not

# Sort method
# Big(0) of 2n
def find_second_largest_sort(arr):
    arr.sort()
    for item in arr[-2::-1]:
        if item < arr[-1]:
            return item
    return -1

def find_second_larges_two_pass(arr):
    if not arr or len(arr) < 2:
        return -1
    
    first_largest = arr[0]
    # Find the first largest
    for item in arr[1:]:
        if item > first_largest:
            first_largest = item

    # Find the second largest
    second_largest = None
    for item in arr:
        if item != first_largest:
            if second_largest is None or item > second_largest:
                second_largest = item

    return second_largest if second_largest is not None else -1

def find_second_largest(arr):
    if not arr or len(arr) < 2:
        return -1

    first_largest = arr[0]
    second_largest = None

    for item in arr[1:]:
        if item > first_largest:
            second_largest = first_largest
            first_largest = item
        elif item != first_largest:
            if second_largest is None or item > second_largest:
                second_largest = item
    return second_largest if second_largest is not None else -1
            
if __name__ == '__main__':
    arr = [10,10,5]
    print(find_second_larges_two_pass(arr))
    
    