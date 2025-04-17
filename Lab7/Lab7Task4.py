graph = {# Graph banaya jisme har city ke connected cities hain aur unke distances bhi
    "Arad": [("Zerind", 75), ("Sibiu", 140), ("Timisoara", 118)],
    "Zerind": [("Arad", 75), ("Oradea", 71)],
    "Oradea": [("Zerind", 71), ("Sibiu", 151)],
    "Sibiu": [("Oradea", 151), ("Arad", 140), ("Fagaras", 99), ("Rimnicu Vilcea", 80)],
    "Fagaras": [("Sibiu", 99), ("Bucharest", 211)],
    "Rimnicu Vilcea": [("Sibiu", 80), ("Pitesti", 97), ("Craiova", 146)],
    "Pitesti": [("Rimnicu Vilcea", 97), ("Bucharest", 101), ("Craiova", 138)],
    "Timisoara": [("Arad", 118), ("Lugoj", 111)],
    "Lugoj": [("Timisoara", 111), ("Mehadia", 70)],
    "Mehadia": [("Lugoj", 70), ("Drobeta", 75)],
    "Drobeta": [("Mehadia", 75), ("Craiova", 120)],
    "Craiova": [("Drobeta", 120), ("Rimnicu Vilcea", 146), ("Pitesti", 138)],
    "Bucharest": [("Fagaras", 211), ("Pitesti", 101), ("Giurgiu", 90), ("Urziceni", 85)],
    "Giurgiu": [("Bucharest", 90)],
    "Urziceni": [("Bucharest", 85), ("Hirsova", 98), ("Vaslui", 142)],
    "Hirsova": [("Urziceni", 98), ("Eforie", 86)],
    "Eforie": [("Hirsova", 86)],
    "Vaslui": [("Urziceni", 142), ("Iasi", 92)],
    "Iasi": [("Vaslui", 92), ("Neamt", 87)],
    "Neamt": [("Iasi", 87)]
}
#Yeh list banayi gayi hai jo current path ko track karegi — yani Arad se le kar Bucharest tak ka safar.Yeh set un cities ko yaad rakhne ke liye hai jinko hum already visit kar chuke hain — taake DFS bar bar same jagah na jaye
#set:Duplicate values allow nahi karta
def dfs(graph, start, goal, path=[], visited=set()):# DFS function jo ek city se doosri city tak path find karta hai
    path.append(start) # Current city ko path mein add karo
    visited.add(start)#us city ko visited mark karo, taake dobara na jaye
    if start == goal:## Agar goal mil gaya to path return karo
        return path
    for neighbor, _ in graph[start]:#current node ke neighbors ko iterate karta hai.
        if neighbor not in visited:#gar neighbor pehle visit nahi kiya gaya, to usko explore karo.
            new_path = dfs(graph, neighbor, goal, path.copy(), visited.copy())#Yeh current neighbor hai, jo hum DFS ke next step me explore karenge.
            #nayi path aur nayi visited cities ke saath DFS ko call kiya ja raha hai, taake backtracking ho sake.
            if new_path:#agar valid path mil gaya, to usko return karo.
                return new_path
    return None  # No path found
# DFS call kiya from Arad to Bucharest
result = dfs(graph, "Arad", "Bucharest")
if result:#Agar DFS ne valid path return kiya ho tu phr path print hojayega
    print("DFS Path from Arad to Bucharest:", " → ".join(result))
else:
    print("No path found.")
