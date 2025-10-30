# Since we are converting our data into objects
# we pass in the attribute we want to sort by

# This function just iterates over the whole array
# and checks where the element should be placed

def insertionSort(arr, attr):
    for i in range(1, len(arr)):
        
        # The current item we are placing and the value to compare

        current_item = arr[i]
        current_val = getattr(arr[i], attr)
        
        # Pointer for finding the correct position
        j = i - 1

        # Find the position in the array
        while j >= 0 and getattr(arr[j], attr) > current_val:
            # Keep shifting left until sorted
            arr[j+1] = arr[j]
            j -= 1

        # Once we find the placement we can add our current item
        arr[j+1] = current_item

    return arr

