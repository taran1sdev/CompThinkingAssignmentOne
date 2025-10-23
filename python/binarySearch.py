
def binarySearchRecurse(arr, low, high, target, attr):
    if high >= low:
        mid = (high + low) // 2
        
        if getattr(arr[mid], attr) == target:
           return mid
        
        elif getattr(arr[mid], attr) > target:
            return binarySearchRecurse(arr, low, mid - 1, target, attr)
        else:
            return binarySearchRecurse(arr, mid + 1, high, target, attr)
    else:
        return -1

def binarySearch(arr, target, attr):
    return binarySearchRecurse(arr, 0, len(arr) - 1, target, attr)
