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
def bfs_shortest_path(graph, start, goal):## BFS algorithm ka function banaya gaya jo shortest path nikaalega
    queue = [[start]] # Queue mein pehle sirf start node ka path rakha
    visited = []#Yeh list visited nodes ko track karne ke liye hai, taake koi node dobara visit na ho.
    while queue: # Jab tak queue khaali na ho, loop chalta rahega
        path = queue.pop(0)#Queue se pehla path nikaala jaata hai. pop(0) se queue ke front se item nikala jaata hai.
        node = path[-1]# path ke last node ko node variable me store kiya jaata hai. Matlab, abhi tak ka last node.
        if node == goal:#Agar yeh last node goal node ke barabar ho, to wo path return kar diya jata hai.
            return path
        if node not in visited:#Agar node abhi tak visited nahi hui hai, to wo visit ki jaayegi.
            visited.append(node)#Is line me node ko visited list me add kar diya jaata hai.
            for neighbor in graph[node]:#Ab hum us node ke neighbors (connected nodes) ko explore karte hain.
                if neighbor not in visited:#Agar neighbor pehle visit nahi ho chuka, to usko explore karenge.
                    new_path = path + [neighbor]#Naye path ko banaya jaata hai by adding the neighbor to the current path.
                    queue.append(new_path)#jab hum new path ya node ko queue me add karte hain, to woh queue ke end me jata hai, taki BFS algorithm level by level search kare.
    return None#Agar goal tak ka path nahi milta, to function None return karega.
start_node = "A"
goal_node = "G"
shortest_path = bfs_shortest_path(graph, start_node, goal_node)
print("Shortest Path from", start_node, "to", goal_node, ":", shortest_path)

