import MorrisAlgo
import sys

enumerate_list = list()
place_of_board = list()
max = 9223372036854775807
min = -9223372036854775807
depth = int(sys.argv[3])
board_contest=list()

class MyFunc():

    
    def __init__(self):
        def read_board():
            new1=list()
            with open(sys.argv[1],'r+') as f:
                for line in f:
                    for char in line:
                        new1.append(char)
                    return new1

        def write_board(lines):
            with open(sys.argv[2],'w') as f:
                for line in lines:
                    f.write(line)

        def minimaxgame(z,board_contest,label):
            exit = MorrisAlgo.main()
            entry = MorrisAlgo.main()
            if(label==0):
                enumerate_list = MorrisAlgo.GenerateMovesMidGameEndGameBlack(board_contest);exit.head = max
            else:
                enumerate_list = MorrisAlgo.GenerateMovesMidGameEndGame(board_contest);exit.head = min  


            if(z==0):
                temp=len(board_contest);pieces_of_white = 0;pieces_of_black = 0
                for pos in range(0,temp):
                    if(board_contest[pos]=='B'):
                        pieces_of_black+=1
                    elif(board_contest[pos]=='W'):
                        pieces_of_white+=1
                if(pieces_of_black<=2):
                    exit.head = 10000
                elif(pieces_of_white<=2):
                    exit.head = -10000
                elif(len(MorrisAlgo.GenerateMovesMidGameEndGameBlack(board_contest))==0):
                    exit.head = 10000
                else:
                    exit.head = (1000*(pieces_of_white-pieces_of_black) - len(MorrisAlgo.GenerateMovesMidGameEndGameBlack(board_contest)))
                exit.counter +=1
                return exit
              
            for place in enumerate_list:
                if(label==0):
                    entry = minimaxgame(z-1,place,1)
                    if(entry.head<exit.head):
                        exit.place_of_board = place
                        exit.head=entry.head
                    exit.counter += entry.counter
                else:
                    entry = minimaxgame(z-1,place,0)
                    if(entry.head>exit.head):
                        exit.place_of_board = place
                        exit.head=entry.head
                    exit.counter += entry.counter   
            return exit
        
        def display(): 
            exit = minimaxgame(depth,MorrisAlgo.boardreverse(read_board()),1)
            exit.place_of_board=''.join(map(str, MorrisAlgo.boardreverse(exit.place_of_board)))
            print("----------------------------------------------------------")
            print("Board Position :", exit.place_of_board)
            print("Position Evaluated by Static Estimation :",exit.counter)
            print("Minimax Estimate :",exit.head)
            write_board(exit.place_of_board)
            print("----------------------------------------------------------")
        display()


if __name__ == '__main__':
    MyFunc()

    


    