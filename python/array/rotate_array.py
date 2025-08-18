def rotate_array_brute(arr,k):
    n = len(arr)

    if not arr or k < 1:
        return arr

    k = k % n
    
    for _ in range(k):   
        last_element = arr[-1]
        for j in range(len(arr)-1, 0, -1):
            arr[j] = arr[j-1]
        arr[0] = last_element
    return arr

def rotate_array_extra_space(arr, k):
    if not arr:
        return arr

    n = len(arr)
    k = k % n
    result = [0] * n

    for i in range(n):
        result[(i + k) % n ] = arr[i]

    return result

def rotate_array_reverse(arr, k):
    if not arr:
        return arr

    n = len(arr)
    k = k % n
    
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    reverse(0, len(arr)-1)
    reverse(0, k-1)
    reverse(k, len(arr)-1)
    return arr

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    k = 5
    print(rotate_array_extra_space(arr, k))