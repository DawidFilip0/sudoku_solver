import solver
import numpy


if __name__ == "__main__":

    board=[]

    def enter_info(board):
        for i in range(9):
            board.append([])

            print("\n")

            for j in board:
                print(j,"\n")

            for j in range(9):
                num=input("What number is in sudoku?: ")
                if num=="":
                    board[i].append(-1)
                else:
                    board[i].append(int(num))

                print(board[i],"\n")

        for i in board:
            print(i,"\n")

        chng=input("want to edit something(y/n):")
        while chng=="y":
            col=int(input("give col: "))
            row=int(input("give row: "))
            val=int(input("give value: "))
            board[row][col]=val

            for i in board:
                print(i,"\n")

            chng=input("want to edit something(y/n):")





        return board

    board=enter_info(board)


    board=numpy.array(board,dtype='int8')



    # board=numpy.array([ [-1,-1,-1,-1,-1,-1,-1,-1,4],
    #                     [5,-1,-1,-1,8,-1,-1,1,7],
    #                     [-1,2,-1,5,-1,-1,-1,-1,-1],
    #                     [-1,-1,6,-1,-1,9,-1,-1,-1],
    #                     [2,-1,-1,-1,7,-1,-1,8,5],
    #                     [-1,-1,-1,-1,-1,-1,3,-1,-1],
    #                     [-1,-1,-1,-1,3,-1,2,-1,-1],
    #                     [1,-1,-1,-1,-1,-1,4,-1,-1],
    #                     [-1,9,-1,-1,-1,7,-1,3,1]],dtype='int8')


    solver.solve(board)





    
        
            