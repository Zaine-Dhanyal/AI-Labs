def check_winner(board):#Yeh function define ho raha hai jo game ke board ko check karega aur winner decide karega.
    for row in board:#Yeh loop har board ki row ko check karta hai.
        if row[0] == row[1] == row[2] and row[0] != ' ':# agr koi row me pehle teen cells aik jesy hun and vo empty na ho tu winner return krdiya jata ha
            return row[0]#return row[0] is used to return the winner, either 'X' or 'O
    for col in range(3):#Yeh loop har column ko check karne ke liye run hota hai.
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':#Agar kisi column mein teen values (0,1,2 rows) same ho aur woh empty na ho, to woh column ka winner hai.
            return board[0][col]# first row ka col
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':#Yeh check karta hai agar left-to-right diagonal mein teen values same hain aur woh empty nahi hain.
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':#board[0][2] → first row, third column
        return board[0][2]#Yeh check karta hai agar right-to-left diagonal mein teen values same hain aur woh empty nahi hain.
    return None#Agar koi winner nahi milta, to None return hota hai.
def minimax(board, is_max):#Yeh minimax function  game ke decision process karta hai. Yeh recursively board ko evaluate karta hai aur best move find karta hai.
    winner = check_winner(board)#ke through pehle board check kiya jaata hai. Agar koi winner milta hai ('X' ya 'O'), to woh value return ki jaati hai.
    if winner == 'X':
        return 1
    if winner == 'O':
        return -1
    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):#draw condition,Agar board full ho gaya ho aur koi winner na ho, to 0 return kiya jaata hai. Yeh draw ka case hai.
        return 0
    #Yeh poora process 'X' ke turn pe sabse best move ko evaluate kar raha hai.
    if is_max:#agr is_max is true tu intial value best ko -100 deygy jo k low ha
        best = -100#Iska matlab hai ke 'X' ko jo score milega, wo is value se compare hoga. Negative value use ki gayi hai taake score ko maximize kiya ja sake.
        for i in range(3):#Yeh loop board ke har cell ko iterate karta hai (3x3 grid).
            for j in range(3):
                if board[i][j] == ' ':#eh check karta hai ke agar cell empty hai (' '), toh hum us cell ko 'X' se fill kar ke move karte hain.
                    board[i][j] = 'X'#Yeh line current empty cell ko 'X' se fill karti hai,
                    best = max(best, minimax(board, False))#to evaluate 'O''s possible moves when it is 'X''s turn.
                    # recursive call hai jo board ke updated state ko
                    # evaluate karta hai, ab 'O' ka turn hai (kyunki is_max = False).,
                    #'X' ka best move find kiya ja raha hai, is liye hum best ko 'X' ke liye max score ke saath update karte hain.
                    board[i][j] = ' '#Yeh line board ko phir se reset karti hai (empty kar deti hai), taake agle cell ko evaluate kar sakein.
        return best# Jab saare possible moves evaluate kar liye jate hain, toh 'X' ka best score return hota h

    else:# Is case mein, 'O' ko minimum score chahiye, taake opponent ko zyada faida na ho.
        best = 100#Positive value use ki gayi hai taake score ko minimize kiya ja sake.
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ': #:Yeh check karta hai agar current cell empty ho, tab hi hum usse fill karenge.
                    board[i][j] = 'O'
                    best = min(best, minimax(board, True))#recursive call hai jo board ke updated state ko evaluate karta hai, ab 'X' ka turn hai (kyunki is_max = True).
#is line mein 'O' ka best move find kiya ja raha hai, is liye hum best ko 'O' ke liye minimum score ke saath update karte hain.
                    board[i][j] = ' '
        return best
def find_best_move(board):
    best_val = -100
    best_move = (-1, -1)#jo koi valid move nahi hai. Yeh best move ko track karega.
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)#Agar current move best hai, toh best_move ko is position pe set karte hain.
    return best_move
board = [['X', 'O', 'X'],
         ['O', 'X', 'O'],
         [' ', ' ', ' ']]
print("Best Move:", find_best_move(board))
#Jab hum 'X' ka best move dhoond rahe hain, toh humein minimax function ko call karna padta hai
# 'O' ke turn pe, taake hum evaluate kar sakein ki 'X' ke move ke baad 'O'
# ka response kya ho sakta hai.