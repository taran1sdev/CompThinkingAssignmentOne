# Since we are converting the data into objects we 
# pass in the attribute to sort by as an argument


# This function merges two sorted arrays
def merge(arr, low, mid, high, attr):
    
    left_side = arr[low : mid + 1]
    right_side = arr[mid + 1 : high + 1]

    i = j = 0
    k = low

    while i < len(left_side) and j < len(right_side):
        if getattr(left_side[i], attr) < getattr(right_side[j], attr):
            arr[k] = left_side[i]
            i += 1
        else:
            arr[k] = right_side[j]
            j += 1
        k += 1

    while i < len(left_side):
        arr[k] = left_side[i]
        i += 1
        k += 1

    while j < len(right_side):
        arr[k] = right_side[j]
        j += 1
        k += 1

# This function calls itself recursively - splitting our array in half each time
def indexMergeSort(arr, low, high, attr):
    if low < high:
        mid = (low + high) // 2

        indexMergeSort(arr, low, mid, attr)
        indexMergeSort(arr, mid + 1, high, attr)

        merge(arr, low, mid, high, attr)

def mergeSort(arr, attr):
    indexMergeSort(arr, 0, len(arr) - 1, attr)
    return arr
