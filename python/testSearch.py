from getData import getData
from bucketSort import bucketSort
from linearSearch import linearSearch
from binarySearch import binarySearch
from operator import attrgetter
import random
from timeit import repeat

attr = "No"
sortedLogs = bucketSort(getData(), attr)

low = getattr(min(sortedLogs, key=attrgetter(attr)), attr)
high = getattr(max(sortedLogs, key=attrgetter(attr)), attr)

def time_execution(algorithm, target, attr):
    setup = f"from __main__ import {algorithm}, sortedLogs, random, low, high"

    stmt = f"{algorithm}(sortedLogs, {target}, \"{attr}\")"

    times = repeat(setup=setup, stmt=stmt, repeat=3, number=1000)

    print(f"{algorithm} ({target}): Best - {min(times)} Worst - {max(times)}")

def randTarget():
    return random.randint(low, high) 

time_execution("linearSearch", randTarget(), attr)
time_execution("binarySearch", randTarget(), attr)
print()

time_execution("linearSearch", randTarget(), attr)
time_execution("binarySearch", randTarget(), attr)
print()

time_execution("linearSearch", randTarget(), attr)
time_execution("binarySearch", randTarget(), attr)
print()

