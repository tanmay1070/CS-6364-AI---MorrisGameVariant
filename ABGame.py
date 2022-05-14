import sys
import MorrisAlgo

enumerate_list = list()
place_of_board = list()
max = 9223372036854775807
min = -9223372036854775807
depth = int(sys.argv[3])
board_contest=list()

class MyFunc():


    def __init__(self):
        def read_board():
            new=list()
            with open(sys.argv[1],'r') as f:
                for line in f:
                    for char in line:
                        new.append(char)
                    return new

        def write_board(lines1):
            with open(sys.argv[2],'w') as f:
                for line in lines1:
                    f.write(line)

        def ABGame(z,board_contest,α,β,label):
            entry = MorrisAlgo.main()
            exit = MorrisAlgo.main()
                        
            if(label==0):    
                enumerate_list = MorrisAlgo.GenerateMovesMidGameEndGameBlack(board_contest)
            else:
                enumerate_list = MorrisAlgo.GenerateMovesMidGameEndGame(board_contest)
            
            if(z==0):
                temp=len(board_contest)
                pieces_of_white = 0
                pieces_of_black = 0
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
                
                if(α>=β):
                    break
                
                if(label==0):
                    entry = ABGame(z-1,place,α,β,1)
                    if(entry.head< β):
                        β = entry.head
                        exit.place_of_board = place
                    exit.counter += entry.counter
                else:
                    entry = ABGame(z-1,place,α,β,0)
                    if(entry.head>α):
                        α = entry.head
                        exit.place_of_board = place
                    exit.counter += entry.counter
    
            if (label==1):
                exit.head = α
            else:
                exit.head = β
            return exit

        def display():
            exit = ABGame(depth,read_board(),min,max,1)
            exit.place_of_board=''.join(map(str, exit.place_of_board))
            print("----------------------------------------------------------")
            print("Board Position :", exit.place_of_board)
            print("Position Evaluated by Static Estimation :",exit.counter)
            print("AB Estimate :",exit.head)
            write_board(exit.place_of_board)
            print("----------------------------------------------------------")
        display()


if __name__ == '__main__':
    MyFunc()
       