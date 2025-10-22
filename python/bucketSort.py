from insertionSort import insertionSort
from operator import attrgetter


def bucketSort(arr, attr):
    # We find the highest and lowest values in the array   
    high = getattr(max(arr, key=attrgetter(attr)), attr)
    low = getattr(min(arr, key=attrgetter(attr)), attr)
    span = high - low + 1
    # We create a bucket for each element
    total_buckets = len(arr)    
    buckets = [[] for _ in range(total_buckets)]

    for item in arr:
        val = getattr(item, attr)
        bucket_number = int(total_buckets * (val - low) / span)
        buckets[bucket_number].append(item)

    for bucket in buckets:
        insertionSort(bucket, attr)

    return_arr = []
    for i in range(len(arr)):
        return_arr += buckets[i]
    return return_arr 
