from data.getData import getData
from data.getGraphData import getGraphData

from algorithms.sort.insertionSort import insertionSort
from algorithms.sort.bucketSort import bucketSort 
from algorithms.sort.mergeSort import mergeSort 

from algorithms.search.linearSearch import linearSearch
from algorithms.search.binarySearch import binarySearch

from algorithms.routing.dijkstra import dijkstra

import random, time, statistics as stats
import pandas as pd

import copy
import tracemalloc

# Function to call per time test
def time_execution(alg, data, key, target=None):
    start = time.perf_counter() # mark the time we start execution
    if target == None:
        _ = alg(data, key)
    else:
        _ = alg(data, target, key)
    return (time.perf_counter() - start) * 1000 # return the current time - the start time in ms


# Run multiple time tests on an algorithm and generate a report
def get_execution_times(alg, data, key, repeats=30, shuffle=False, search=False, route=False):
    results = []    
    for _ in range(repeats):
        cloneData = copy.deepcopy(data)
        if shuffle:
            random.shuffle(cloneData)
        
        if search:
            # When we introduce searching / sorting by different data types
            # we need to change this
            results.append(time_execution(alg, data, key, target=random.randint(1,2000))) 
        elif route:
            for node in key:
                results.append(time_execution(alg, data, node))
        else:
            results.append(time_execution(alg, cloneData, key))
    return {
        "mean": sum(results) / len(results),
        "sdev": stats.pstdev(results),
        "p95": sorted(results)[int(0.95*len(results)) - 1],
        "size": len(results),
        "data": data
    }

# Function to track the peak memory used by an algorithm
def get_peak_memory(alg, data, key, target=None):
    tracemalloc.start()
    if target == None:
        _ = alg(data, key)
    else:
        _ = alg(data, target, key)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak


if __name__ == "__main__":
    logs = getData()

    sortTests = {
        (insertionSort, "Insertion Sort", "No"),
        (bucketSort, "Bucket Sort", "No"),
        (mergeSort, "Merge Sort", "No"),
    }

    results_shuffled = []
    results = []

    for alg, name, key in sortTests:
        time_stats_shuffle = get_execution_times(
                    alg, 
                    logs,
                    key,
                    repeats=30,
                    shuffle=True)
        time_stats = get_execution_times(
                    alg,
                    logs,
                    key,
                    repeats=30,
                    shuffle=False
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
        
    
    # Run the search tests
    searchTests = {
            (linearSearch, "Linear Search", "No"),
            (binarySearch, "Binary Search", "No")
    }

    results = []
        
        

    for alg, name, key in searchTests:
        logs_sorted = bucketSort(logs, key)

        time_stats = get_execution_times(
                alg,
                logs_sorted,
                key,
                repeats=30,
                search=True)

        memory_stats = get_peak_memory(alg, logs_sorted, key, target=random.randint(1,2000))

        results.append({
            "Algorithm": name,
            "Key": key,
            "Repeats": time_stats["size"],
            "Mean Time": time_stats["mean"],
            "Standard Deviation": time_stats["sdev"],
            "Top 95": time_stats["p95"],
            "Peak Memory": memory_stats})

        pd.DataFrame(results).to_csv("results/search.csv", index=False)
        print("Search results written to csv")

    routingTests = {
            (dijkstra, "Dijkstra's Algorithm")
            }
    
    results = []

    for alg, name in routingTests:
        graphs = getGraphData()
        
        for researcher in graphs.keys():
            
            time_stats = get_execution_times(
                    alg,
                    graphs[researcher],
                    graphs[researcher].keys(),
                    repeats=10,
                    route=True)

            memory_stats = get_peak_memory(alg, graphs[researcher], "1")

            results.append({
                "Algorithm": name,
                "Key": researcher,
                "Repeats": time_stats["size"],
                "Mean Time": time_stats["mean"],
                "Standard Deviation": time_stats["sdev"],
                "Top 95": time_stats["p95"],
                "Peak Memory": memory_stats})
                
        pd.DataFrame(results).to_csv("results/routing.csv", index=False)
        print("Routing results written to csv")

                    

