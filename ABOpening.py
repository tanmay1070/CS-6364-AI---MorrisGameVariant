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

        def ABOpening(z,board_contest,α,β,label):
            entry = MorrisAlgo.main()
            exit = MorrisAlgo.main()
            count_last = 0
            
            if(label==0):
                enumerate_list = MorrisAlgo.GenerateMovesOpeningBlack(board_contest) 
            else:
                enumerate_list = MorrisAlgo.GenerateMovesOpening(board_contest)
            
            if(z==0):
                count_last = MorrisAlgo.Static_estimate_for_whiteopening(board_contest)
                exit.head = count_last
                exit.counter += 1
                return exit
            
            for place in enumerate_list:
                if(α>=β):
                    break
                        
                if(label==0):
                    entry = ABOpening(z-1,place,α,β,1)
                    if(entry.head< β):
                        β = entry.head
                        exit.place_of_board = place
                    exit.counter += entry.counter
                else:
                    entry = ABOpening(z-1,place,α,β,0)
                    if(entry.head>α):
                        α = entry.head
                        exit.place_of_board = place
                    exit.counter += entry.counter

            if (label==1):
                exit.head =α
            else:
                exit.head = β
            return exit

        def display():
            exit = ABOpening(depth,read_board(),min,max,1)
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
       

