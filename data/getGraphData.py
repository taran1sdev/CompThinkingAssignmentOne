import pandas as pd
import numpy as np
import os

def get_symmetric_dataframes():    
    df = pd.read_excel("data/Data.ods", sheet_name="Graphs", engine="odf")

    graphs = {}

    # Each graph begins with a cell "Graph" - retrieve a list of these starting points
    # we need to specify the type as string and not Series or we get an error 
    starts = df.index[df.iloc[:, 0].astype(str).str.contains("Graph", case=False, na=False)].tolist()

    for i, start in enumerate(starts):
        
        # The name of the graph is in the cell directly above the start point
        name = str(df.iloc[start-1, 0]).strip()
        
        # We get the end of the block from the start of the first block minus the name cell
        end = starts[i + 1] - 2 if i + 1 < len(starts) else len(df)

        # Get the block of cells containing our graph data - skip graph and index
        block = (df.iloc[start + 2:end].reset_index(drop=True))
        
        # Remove the left index column
        block = block.drop(columns=[block.columns[0]])
         
        # We give any NaN cells a value of 0 initially
        block.fillna(0)
        
        # Convert to a numeric type        
        block = block.apply(pd.to_numeric, errors="coerce").fillna(0)
        
        # We need our row / column names to align to make symmetrical 
        n = block.shape[0]

        block.index = range(n)
        block.columns = range(n)

        # Now we fill in the 0 values - we combine the dataframe with the transposed dataframe
        sym_block = block.combine(block.T, np.maximum, fill_value=0) 

        # Zero the diagonal - nodes should not have edges to themselves
        np.fill_diagonal(sym_block.values, 0)
        
        graphs[name] = sym_block

    return graphs 

def convert_df_to_graph(df):
    n = df.shape[0]
    
    # Initialize graph dictionary 
    graph = {str(i+1): {} for i in range(n)}
    
    for i in range(n):
        for j in range(n):
            edge = float(df.iat[i,j])
            if i != j and edge != 0:
                graph[str(i+1)][str(j+1)] = edge
    return graph

def getGraphData():
    dfs = get_symmetric_dataframes()
    graphs = {}
    for name, df in dfs.items():
        graphs[name] = convert_df_to_graph(df)
    return graphs



