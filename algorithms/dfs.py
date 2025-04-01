def DFS(graph: dict[list[str]], node: str, visited=None, traversal=None) -> list:
    """
    Depth-first search algorithm
    
    Parameters:
        visited (set): a set of visited nodes
        graph (dict): a graph represented as a dictionary (adjacency list)
        node (str): the node to start the search from
        
    Time Complexity: 
        O(V + E), where V is the no. of vertices and E is the no. of edges
        
    Space Complexity:
        O(V), where V is the no. of vertices
    """
    if visited is None:
        visited = set()
    if traversal is None:
        traversal = []
        

    if node not in visited:
        visited.add(node)
        traversal.append(node)
        
        for neighbour in graph[node]:
            DFS(graph, neighbour, visited, traversal)
            
    return traversal
            
            
if __name__ == '__main__':
    # Test graph
    graph = {
        '5': ['3', '7'],
        '3': ['2', '4'],
        '7': ['8'],
        '2': [],
        '4': ['8'],
        '8': []
    }
    
    # Run DFS
    DFS(graph, '5')