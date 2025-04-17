graph = {  #  Graph with nodes and edge costs
    'A': {'B': 4, 'C': 3},
    'B': {'A': 4, 'D': 5, 'E': 12},
    'C': {'A': 3, 'F': 7},
    'D': {'B': 5, 'E': 2, 'G': 9},
    'E': {'B': 12, 'D': 2, 'H': 5},
    'F': {'C': 7, 'I': 4},
    'G': {'D': 9, 'H': 6},
    'H': {'E': 5, 'G': 6, 'I': 3},
    'I': {'F': 4, 'H': 3}
}
heuristic = {#Heuristic cost is the estimated cost from any node to the goal node.
    'A': 10, 'B': 8, 'C': 9, 'D': 7, 'E': 6,
    'F': 4, 'G': 5, 'H': 3, 'I': 0
}
def a_star(graph, start, goal):
    open_list = [(0 + heuristic[start], 0, start, [])]# Format: (f = g + h, g, current_node, path)
    visited = set()#Duplicate nodes avoid karne ke liye set banaya jo already visit ho chuke hain.
    while open_list:#Jab tak explore karne ke liye nodes hain.
        #Yahan x ek tuple hai: (f, g, current, path)
        #Lambda ek anonymous function hai:x[0] → f = total cost (g + h)
        open_list.sort(key=lambda x: x[0])#List ko f = g + h ke basis par sort karo (lowest cost first).
        f, g, current, path = open_list.pop(0)#Sabse kam cost wala node nikaalo aur uska f, g, node, aur path le lo.
        if current in visited:
            continue# Agar node pehle visit ho chuka hai, to skip karo
        visited.add(current)#Node ko visited list mein daal do.
        path = path + [current]# Ab tak ka path update karo, current node ko add karke.
        if current == goal:#Agar goal mil gaya, to path aur uski total cost g return kar do.
            return path, g
        for neighbor, cost in graph[current].items():#.items(): Isse har neighbor aur uska cost milta hai (e.g., ('B', 4) where B is the neighbor and 4 is the cost).
            if neighbor not in visited:
                #Total cost (actual cost + heuristic estimate to goal).#Actual cost from start to this neighbor.
                open_list.append((g + cost + heuristic[neighbor], g + cost, neighbor, path))
    return None, float('inf')#none  indicating no valid path.  Yeh infinity ka representation hota hai. Agar koi path nahi milta, to cost ko infinity set kiya jata hai
path, cost = a_star(graph, 'A', 'I')
print("Shortest Path:", " → ".join(path))
print("Total Cost:", cost)
