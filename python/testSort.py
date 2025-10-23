from timeit import repeat
import random 
import copy

from insertionSort import insertionSort
from bucketSort import bucketSort
from mergeSort import mergeSort
from getData import getData

logs = getData()

def time_execution(algorithm, arr, attr):
    setup = f"from __main__ import {algorithm}, logs, copy; arr=copy.deepcopy(logs)"

    stmt = f"{algorithm}(arr, \"{attr}\")"

    times = repeat(setup=setup, stmt=stmt, repeat=3, number=10)

    print(f"{algorithm}: Best - {min(times)}. Worst - {max(times)}")


attr = "No"
# We measure the time taken with each algorithm with the data in a near-sorted state
time_execution("insertionSort", copy.deepcopy(logs), attr)
time_execution("bucketSort", copy.deepcopy(logs), attr)
time_execution("mergeSort", copy.deepcopy(logs), attr)
print()
# We randomize the order and test again
random.shuffle(logs)

time_execution("insertionSort", copy.deepcopy(logs), attr)
time_execution("bucketSort", copy.deepcopy(logs), attr)
time_execution("mergeSort", copy.deepcopy(logs), attr)
print()
# We make the data set larger and test again

logs += logs

random.shuffle(logs)

time_execution("insertionSort", copy.deepcopy(logs), attr)
time_execution("bucketSort", copy.deepcopy(logs), attr)
time_execution("mergeSort", copy.deepcopy(logs), attr)
print()
