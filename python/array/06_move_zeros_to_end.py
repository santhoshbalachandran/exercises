# Given an array, move all 0s to the end while maintaining the relative order of other elements

# Example: [0, 1, 0, 3, 12] → [1, 3, 12, 0, 0]

def move_zeros_to_end(arr):
    if not len(arr):
        return []
    
    tracker = None
    for i in range(len(arr)):
        if arr[i] == 0:
            if tracker == None:
                tracker = i
        else:
            if tracker != None:
                arr[i], arr[tracker] = arr[tracker], arr[i]
                if arr[tracker+1] == 0:
                    tracker += 1
                else:
                    tracker = None
    return arr

def move_zeros_to_end_extra_space(arr):
    if not len(arr):
       return []
   
    res = []
    zeros_count = 0
    for num in arr:
        if num == 0:
           zeros_count += 1
        else:
           res.append(num)
        
    if zeros_count:
       for _ in range(zeros_count):
           res.append(0)

    return res

if __name__ == '__main__':
    # arr = [1, 2, 0]
    # arr = [0,1,0,0,2, 0]
    # arr = [0, 0, 0, 0, 0]
    arr = [0,0,0,1,2,3,4,5,6]
    # print(move_zeros_to_end(arr))
    print(move_zeros_to_end_extra_space(arr))