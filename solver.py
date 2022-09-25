import copy
import numpy


copy.copy

def solve(board):

    print(board)
   
    found = False

    solutions = []
    
    def backtrack(col, row,found):
       
        
        if row == 9 or found == True:
            solution = copy.deepcopy(board)
            solutions.append(solution)            
            return True

        flag = False
        
        if board[row,col] == -1:
            for i in range(1,10):
                flag = False
                

                if any(i == j for j in board[row]):
                    continue
                if any(i == j[col] for j in board):
                    continue

                y = (row//3)*3
                x = (col//3)*3
                for j in (board[y:y+3]):
                    for k in (j[x:x+3]):
                        if i == k:
                            flag = True
                if flag:
                    continue

                board[row,col] = i

                if col < 8:
                    found= backtrack(col+1, row,found)

                if col == 8:
                    found= backtrack(0, row+1,found)
               
                board[row,col] = -1

        else:
            
            if col < 8:
                found= backtrack(col+1, row,found)
                if found==True:
                    return True 

            if col == 8:
                found= backtrack(0, row+1,found)
                if found==True:
                    return True


    backtrack(0, 0,found)

    print(solutions[0])