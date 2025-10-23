# Search though the array until we find the target value
def linearSearch(arr, target,  attr):
    for i, item in enumerate(arr):
        if getattr(item, attr) == target:
            return i
    return -1
