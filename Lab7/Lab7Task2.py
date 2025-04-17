graph = {# Graph banaya gaya jisme har node ke connected nodes (neighbors) diye gaye hain
    "A": ["B", "C", "H"],
    "B": ["A"],
    "C": ["A", "D"],
    "D": ["C", "E", "F"],
    "E": ["D", "G", "H"],
    "F": ["D", "G"],
    "G": ["E", "F"],
    "H": ["A", "E"]
}
visited = []# Yeh list track karegi ke kaunse nodes visit ho chuke hain
def dfs(graph, node):#node: wo current node hai jahan se DFS start ya continue ho raha hai.
    if node not in visited: # Agar node pehli baar visit ho rahi hai
        print(node, end=" ") # Node ka naam print karo with space,end=" " isliye likha hai taake print karte waqt har node same line me space ke sath aaye, new line na ho.
        visited.append(node)# Node ko visited list mein daal do
        for neighbor in graph[node]:#current node ke sab neighbors ko loop se check karo.
            dfs(graph, neighbor)#har neighbor pe DFS ko recursively call karo.
print("Depth First Search Traversal:")
dfs(graph, "A")
