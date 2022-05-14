import sys
import MorrisAlgo

enumerate_list = list()
place_of_board = list()
max = 9223372036854775807
min = -9223372036854775807
depth = int(sys.argv[3])

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

        def minimax_opening(z,board_contest,label):
            exit = MorrisAlgo.main()
            entry = MorrisAlgo.main()
        
            if(label==0):
                enumerate_list = MorrisAlgo.GenerateMovesOpeningBlack(board_contest);exit.head = max
            else:
                enumerate_list = MorrisAlgo.GenerateMovesOpening(board_contest);exit.head = min
            if(z==0):
                counter_last = MorrisAlgo.Static_estimate_for_whiteopening(board_contest);exit = MorrisAlgo.main(counter_last,exit.counter+1,board_contest);return exit
            
            for place in enumerate_list:
                if(label==0):
                    entry = minimax_opening(z-1,place,1)
                    if(entry.head<exit.head):
                        exit.place_of_board = place
                        exit.head=entry.head
                    exit.counter += entry.counter
                else:
                    entry = minimax_opening(z-1,place,0)
                    if(entry.head>exit.head):
                        exit.place_of_board = place
                        exit.head=entry.head
                    exit.counter += entry.counter   
            return exit
                    
        def display(): 
            exit = minimax_opening(depth,MorrisAlgo.boardreverse(read_board()),1)
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

    


    