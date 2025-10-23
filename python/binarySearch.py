
def binarySearchRecurse(arr, low, high, target, attr):
    if high >= low:
        mid = len(arr) // 2
        
        if getattr(arr[mid], attr) == target:
           return mid
        
        elif getattr(arr[mid], attr) > target:
            return binarySearchRecurse(arr, low, mid - 1, target, attr)
        else:
            return binarySearchRecurse(arr, mid + 1, high, target, attr)
    else:
        return -1

def binarySeach(arr, target, attr):
    return binarySearchRecurse(arr, 0, len(arr) - 1, target, attr)
