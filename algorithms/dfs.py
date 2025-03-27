def DFS(visited: set, graph: dict[list[str]], node: str) -> None:
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
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            DFS(visited, graph, neighbour)
            
if __name__ == '__main__':
    graph = {
        '5': ['3', '7'],
        '3': ['2', '4'],
        '7': ['8'],
        '2': [],
        '4': ['8'],
        '8': []
    }
    
    visited = set()
    DFS(visited, graph, '5')