# given an undirected graph with v viretis and e edges, check if there is a cycle in the graph

def is_cycle_util(v, visited, parent, adj):
    # Mark the current node as visited
    visited[v] = True
    
    # Recur for all the vertices adjacent to this vertex
    for i in adj[v]:
        # If an adjacent vertex is not visited, then recur for that adjacent vertex
        if not visited[i]:
            if is_cycle_util(i, visited, v, adj):
                return True
        # If an adjacent vertex is visited and not the parent of the current vertex, then there is a cycle
        elif i != parent:
            return True
    return False

def is_cycle(V, adj):
    # Initialize visited array
    visited = [False] * V
    
    # Call the recursive helper function to detect cycle in different DFS trees
    for i in range(V):
        if not visited[i]: # Don't recur for already visited vertex
            if is_cycle_util(i, visited, -1, adj):
                return True
            
    return False

# Example Usage
V = 5
adj = [[] for _ in range(V)]
adj[0].append(1)
adj[1].append(0)
adj[1].append(2)
adj[2].append(1)
adj[2].append(3)
adj[3].append(2)
adj[3].append(4)
adj[4].append(3)
adj[4].append(1)
adj[1].append(4)

print(adj)

print(is_cycle(V, adj))  # Output: True (since there is a cycle in the graph)


## A Different Approach

