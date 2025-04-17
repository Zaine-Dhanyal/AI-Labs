def find_blank(matrix):#Ye function 3x3 puzzle matrix mein 0 (blank space) dhoondhne ke liye bana hai.
    for i in range(3):
        for j in range(3):#Har row ke 3 columns bhi check karega.
            if matrix[i][j] == 0:#Agar kisi position pe 0 mil gaya, to...
                return i, j#Us 0 ki row aur column ki position return karega.
def swap_positions(matrix, row, col, new_row, new_col):#Ye function 0 ko ek naye position pe move karta hai (swap karta hai).
    new_matrix = [row[:] for row in matrix]#row[:] ka matlab hota hai: us row ka full copy banao
    #Yeh line swap kar rahi hai values ko — yaani dono jagah ki values ko aapas mein badal rahi hai.
    #1 Jahan blank (0) originally tha, Jahan se value swap karni hai,right side py position dekhrhy hein Pehli value (jo 0 ki jagah ayegi), (right side) → Doosri value (jo dusri position pe chali jayegi)
    new_matrix[row][col], new_matrix[new_row][new_col] = new_matrix[new_row][new_col], new_matrix[row][col]
    return new_matrix#Nayi matrix (jisme swap ho chuka) return karta hai.
def bfs_8_puzzle(start, goal):#Ye main function hai jo BFS algorithm se puzzle solve karta hai.
    queue = [(start, [])]#Ye list ab tak ka path represent karti hai or start is the point jahan sy puzzle solve krna start hota ha
    visited = set()#Already visit ki hui matrices ko track karne ke liye set bana raha hai.
    while queue:#Jab tak queue empty na ho, loop chalta rahega.
        #Queue se first matrix aur uska path nikalta hai.
        current_matrix, path = queue.pop(0)#queue ek list hai jisme aise items hain: (matrix, path),
        # current_matrix = jo matrix ab hum explore karenge,path = ab tak ka move history (steps)
        visited.add(tuple(map(tuple, current_matrix)))# current_matrix ko visited set mein daalti hai,
        #Lekin matrix ko directly set mein add nahi kar sakte,Because list is unhashable (mutable cheez set mein nahi daal sakte).
        #Matrix ki har row ko tuple bana deta hai,Ab ye matrix ek immutable tuple ban gaya, isliye set mein daal sakte hain.
#Ab ye matrix ek immutable tuple ban gaya, isliye set mein daal sakte hain.
        if current_matrix == goal:#Agar current matrix goal ke barabar ho, to...
            return path#Solution mil gaya, us tak ka path return karo.
        row, col = find_blank(current_matrix)#Current matrix mein blank space (0) ka location dhoondta hai.
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]#Yeh possible directions hain: up, down, left, right.
        for dr, dc in moves:#Har direction ke liye try karega. dr = delta row , row ka change
            #new row aur new column position ban rahi hai jahan 0 ko move karna hai.
            new_row, new_col = row + dr, col + dc#Nayi position calculate karta hai.
            #Ye current row position mein change (direction) add karta hai.
            if 0 <= new_row < 3 and 0 <= new_col < 3: #Check karta hai ke nayi position matrix ke andar hi ho. new row index 0, 1 ya 2 ho sakti hai
                new_matrix = swap_positions(current_matrix, row, col, new_row, new_col)#0 ko nayi position pe move karta hai.
                if tuple(map(tuple, new_matrix)) not in visited:  # Avoid revisiting
                    queue.append((new_matrix, path + [new_matrix]))  # Add new state, new-matrix updated puzzle state after moving 0
                    # current state of puzzle,row, col → jahan abhi 0 hai, new_row, new_col → jahan 0 ko move karna hai
    return None#Function kuch bhi return nahi kar raha
initial_state = [
    [1, 2, 3],
    [5, 6, 0],
    [7, 8, 4]
]
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
solution = bfs_8_puzzle(initial_state, goal_state)
if solution:
    print("Solution Found! Moves:")
    for step in solution:#Har step (move) ko print karega.
        for row in step:#Har step ek matrix hai, jise row by row print kiya jaata hai.
            print(row)
        print("---")
else:
    print("No Solution Found!")

