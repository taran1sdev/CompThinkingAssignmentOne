from data.getData import getData
from algorithms.sort.insertionSort import insertionSort
from algorithms.sort.bucketSort import bucketSort 
from algorithms.sort.mergeSort import mergeSort 

import random, time, statistics as stats
import pandas as pd

import copy
import tracemalloc

# Function to call per time test
def time_execution(alg, data, key):
    start = time.perf_counter() # mark the time we start execution
    _ = alg(data, key)
    return time.perf_counter() - start # return the current time - the start time


# Run multiple time tests on an algorithm and generate a report
def get_execution_times(alg, data, key, repeats, shuffle=True):
    results = []    
    for _ in range(repeats):
        cloneData = copy.deepcopy(data)
        if shuffle:
            random.shuffle(cloneData)
        results.append(time_execution(alg, cloneData, key))
    return {
        "mean": sum(results) / len(results),
        "sdev": stats.pstdev(results),
        "p95": sorted(results)[int(0.95*len(results)) - 1],
        "size": len(results),
        "data": data
    }

# Function to track the peak memory used by an algorithm
def get_peak_memory(alg, data, key):
    tracemalloc.start()
    _ = alg(data, key)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak


if __name__ == "__main__":
    logs = getData()

    tests = {
        (insertionSort, "Insertion Sort", "No"),
        (bucketSort, "Bucket Sort", "No"),
        (mergeSort, "Merge Sort", "No"),
    }

    results_shuffled = []
    results = []

    for alg, name, key in tests:
        time_stats_shuffle = get_execution_times(
                    alg, 
                    copy.deepcopy(logs),
                    key,
                    30,
                    True)
        time_stats = get_execution_times(
                    alg,
                    copy.deepcopy(logs),
                    key,
                    30,
                    False
                )

        memory_stats = get_peak_memory(alg, copy.deepcopy(logs), key)

        results_shuffled.append({
            "Algorithm": name,
            "Key": key,
            "Repeats": time_stats_shuffle["size"],
            "Mean Time": time_stats_shuffle["mean"],
            "Standard Deviation": time_stats_shuffle["sdev"],
            "Top 95": time_stats_shuffle["p95"],
            "Peak Memory": memory_stats})
        
        results.append({
                "Algorithm": name,
                "Key": key,
                "Repeats": time_stats["size"],
                "Mean Time": time_stats["mean"],
                "Standard Deviation": time_stats["sdev"],
                "Top 95": time_stats["p95"],
                "Peak Memory": memory_stats})

        pd.DataFrame(results_shuffled).to_csv("results/sorting_shuffled.csv", index=False)
        print("Shuffled results written to csv")

        pd.DataFrame(results).to_csv("results/sorting_unshuffled.csv", index=False)
        print("Unshuffled results written to csv")

