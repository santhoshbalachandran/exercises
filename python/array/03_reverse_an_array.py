# Given an array, reverse it without using an extra array

def reverse(arr):
    if not arr:
        return "Empty array"
    
    if len(arr) == 1:
        return arr
    
    left, right = 0, len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return arr

if __name__ == '__main__':
    arr = [10, 10, 10]
    print(reverse(arr))