import copy

copy.copy

def solve(board=None):

    if not board:
        board=[[[-1,False] for j in range(9)] for i in range(9)]

    for i in board:
        print(i)

    global found
    found=False

    solutions=[]
   

    def backtrack(col,row):
        global found
        if row == 9 or found==True :
            solution = copy.deepcopy(board)
            solutions.append(solution)
            found=True
            return

        flag=False

        for i in range(10):
            flag=False

            if board[row][col][1]==False:

                if any(i == j[0] for j in board[row]):
                    continue
                if any(i == j[col][0] for j in board):
                    continue

                y=(row//3)*3
                x=(col//3)*3
                for j in (board[y:y+3]):
                    for k in (j[x:x+3]):                                        
                        if i == k[0]:                          
                            flag=True
                if flag:
                    continue
             
                board[row][col][0] = i

            if col<8:
                backtrack(col+1,row)
            if col==8:
                backtrack(0,row+1)

            if board[row][col][1]==False:
                board[row][col][0] = -1

    backtrack(0,0)

    for i in solutions[0]:
        print(i)

        
