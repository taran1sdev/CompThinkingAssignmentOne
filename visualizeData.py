import pandas as pd 

import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")

def get_results():
    search_df = pd.read_csv("results/search.csv")
    sort_df = pd.read_csv("results/sorting_unshuffled.csv")
    sort_shuffle_df = pd.read_csv("results/sorting_shuffled.csv")

    return [ 
        (search_df, "Search Results"),
        (sort_df, "Unshuffled Sort Results"),
        (sort_shuffle_df, "Shuffled Sort Results")]


def create_graph(df, key, graphname):
    fig, ax = plt.subplots()
    ax.bar(df["Algorithm"], df[key])

    plt.xlabel("Algorithm")
    plt.ylabel(key)
    
    plt.title(f"{graphname} - {key}")
    
    plt.savefig(f"results/graphs/{graphname.replace(' ', '_')}_{key.replace(' ', '_')}.png")

    #plt.show()

if __name__ == "__main__":
    results = get_results()
    
    keys = [
        "Mean Time",
        "Standard Deviation",
        "Top 95",
        "Peak Memory"
    ]

    for df, graphname in results:
        for key in keys:
            create_graph(df, key, graphname)

