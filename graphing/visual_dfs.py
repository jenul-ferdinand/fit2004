import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import networkx as nx
import matplotlib.pyplot as plot

from algorithms.dfs import DFS

def visual_dfs(graph, start_node):
    """
    Visualises the DFS traversal with networkx and matplotlib
    """
    # Create the directed graph
    G = nx.DiGraph()
    
    # Add edges from teh adjacency list
    for node, neighbours in graph.items():
        for neighbour in neighbours:
            G.add_edge(node, neighbour)
    
    # Get the DFS traversal order
    traversal = DFS(graph, start_node)
    
    # Set positions for nodes
    pos = nx.spring_layout(G, seed=42)
    
    plot.figure(figsize=(10, 8))
    
    # Draw the graph
    nx.draw(
        G, pos, with_labels=True, node_color='lightblue', node_size=700, 
        arrows=True, arrowsize=20
    )
    
    # Highlight the traversal path
    def dfs_edges(graph, node, visited=None, path=None, forward_edges=None, backtrack_edges=None) -> tuple[list, list]:
        if visited is None:
            visited = set()
            
        if path is None:
            path = []
            
        if forward_edges is None:
            forward_edges = []
        
        if backtrack_edges is None:
            backtrack_edges = []
        
        visited.add(node)
        path.append(node)
        
        for neighbour in graph[node]:
            # Forward edge - not visited yet
            if neighbour not in visited:
                forward_edges.append((node, neighbour))
                dfs_edges(graph, neighbour, visited, path, forward_edges, backtrack_edges)
                
            # Backtracking edge - already visited node in current path
            elif neighbour in path:
                backtrack_edges.append((node, neighbour))
                
        # Node is processed, remove from path
        path.pop()
        
        return forward_edges, backtrack_edges

    edges1, edges2 = dfs_edges(graph, start_node)
                
    # Highlight forward and backtrack edges in different colours
    nx.draw_networkx_edges(G, pos, edgelist=edges1, edge_color='red', width=3)
    nx.draw_networkx_edges(G, pos, edgelist=edges2, edge_color='blue', width=3, style='dashed')
    
    plot.title(f'DFS Traversal from {start_node}')
    plot.axis('off')
    plot.show()
    
if __name__ == '__main__':
    
    graph = {
        '5': ['3', '7'],
        '3': ['2', '4'],
        '7': ['8'],
        '2': [],
        '4': ['8', '5'],
        '8': []
    }
    
    # Print DFS traversal order
    starting_node = '5'
    traversal = DFS(graph, starting_node)
    print(f'DFS traversal starting from node {starting_node}: {traversal}')
    
    # Visualise the DFS
    visual_dfs(graph, starting_node)