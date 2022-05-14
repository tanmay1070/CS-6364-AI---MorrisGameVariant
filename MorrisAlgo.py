from copy import deepcopy as mycopyfunc

def CloseMill(j,b):
    C=b[j]
    if(C!='x'):
        return Mills_case(j,b,C)
    else:
        return False

def Mills_case(j,b,C):
    if (C=='x'):
        return False
    
    if(j==0):
        if((b[2]==C and b[4]==C) or (b[6]==C and b[18]==C)):
            return True; return False
    
    elif(j==1):
        if((b[3]==C and b[5]==C) or (b[11]==C and b[20]==C)):
            return True; return False

    elif(j==2):
        if((b[0]==C and b[4]==C) or (b[7]==C and b[15]==C)):
            return True; return False
    
    elif(j==3):
        if((b[1]==C and b[5]==C) or (b[10]==C and b[17]==C)):
            return True; return False
    
    elif(j==4):
        if((b[0]==C and b[2]==C) or (b[8]==C and b[12]==C)):
            return True; return False

    elif(j==5):
        if((b[1]==C and b[3]==C) or (b[9]==C and b[14]==C)):
            return True; return False    
    
    elif(j==6):
        if((b[0]==C and b[18]==C) or (b[7]==C and b[8]==C)):
            return True; return False 
    
    elif(j==7):
        if((b[6]==C and b[8]==C) or (b[2]==C and b[15]==C)):
            return True; return False
    
    elif(j==8):
        if((b[4]==C and b[12]==C) or (b[6]==C and b[7]==C)):
            return True; return False
    
    elif(j==9):
        if((b[5]==C and b[14]==C) or (b[10]==C and b[11]==C)):
            return True; return False

    elif(j==10):
        if((b[3]==C and b[17]==C) or (b[9]==C and b[11]==C)):
            return True; return False 
    
    elif(j==11):
        if((b[1]==C and b[20]==C) or (b[9]==C and b[10]==C)):
            return True; return False
    
    elif(j==12):
        if((b[4]==C and b[8]==C) or (b[15]==C and b[18]==C) or (b[13]==C and b[14]==C)):
            return True; return False
    
    elif(j==13):
        if((b[16]==C and b[19]==C) or (b[12]==C and b[14]==C)):
            return True; return False    
    
    elif(j==14):
        if((b[12]==C and b[13]==C) or (b[17]==C and b[20]==C) or (b[5]==C and b[9]==C)):
            return True; return False 
    
    elif(j==15):
        if((b[12]==C and b[18]==C) or (b[16]==C and b[17]==C) or (b[2]==C and b[7]==C)):
            return True; return False
    
    elif(j==16):
        if((b[13]==C and b[19]==C) or (b[15]==C and b[17]==C)):
            return True; return False

    elif(j==17):
        if((b[3]==C and b[10]==C) or (b[14]==C and b[20]==C) or (b[16]==C and b[15]==C)):
            return True; return False

    elif(j==18):
        if((b[0]==C and b[6]==C) or (b[12]==C and b[15]==C) or (b[19]==C and b[20]==C)):
            return True; return False
    
    elif(j==19):
        if((b[13]==C and b[16]==C) or (b[18]==C and b[20]==C)):
            return True; return False   
    
    elif(j==20):
        if((b[18]==C and b[19]==C) or (b[14]==C and b[17]==C) or (b[1]==C and b[11]==C)):
            return True; return False

    else:
        return False
    
def GenerateRemove(pos_board,L3):
    x= len(pos_board)
    for location in range(0,x):
        if pos_board[location]=='B':
            if not CloseMill(location,pos_board):
                new_b=mycopyfunc(pos_board)
                new_b[location]='x'
                L3.append(new_b)
    return L3

def GenerateAdd(pos_board1):
    L1=list()
    x= len(pos_board1)
    for locate in range(0,x):
        if(pos_board1[locate]=='x'):
            b=mycopyfunc(pos_board1)
            b[locate]='W'
            if (CloseMill(locate,b)):
                L1=GenerateRemove(b,L1)
            else:
                L1.append(b)
    return L1


def adjoint_list(j):
    closelist=list()
    if(j==0):
        closelist.extend([1,2,6])
    elif(j==1):
        closelist.extend([0,3,11])
    elif(j==2):
        closelist.extend([0,3,4,7])
    elif(j==3):
        closelist.extend([1,2,5,10])
    elif(j==4):
        closelist.extend([2,5,8])
    elif(j==5):
        closelist.extend([3,4,9])
    elif(j==6):
        closelist.extend([0,7,18])
    elif(j==7):
        closelist.extend([2,6,8,15])
    elif(j==8):
        closelist.extend([4,7,12])
    elif(j==9):
        closelist.extend([5,10,14])
    elif(j==10):
        closelist.extend([3,9,11,17])
    elif(j==11):
        closelist.extend([1,10,20])
    elif(j==12):
        closelist.extend([8,13,15])
    elif(j==13):
        closelist.extend([12,14,16])
    elif(j==14):
        closelist.extend([9,13,17])
    elif(j==15):
        closelist.extend([7,12,16,18])
    elif(j==16):
        closelist.extend([13,15,17,19])
    elif(j==17):
        closelist.extend([10,14,16,20])
    elif(j==18):
        closelist.extend([6,15,19])
    elif(j==19):
        closelist.extend([16,18,20])
    elif(j==20):
        closelist.extend([11,17,19])
    else:
        return closelist
    
    return closelist


def boardreverse(flip):
    b = list(range(0,21))
    for j in range(0,len(flip)):
        if(flip[j]=='W'):
            b[j]='B'
        elif(flip[j]=='B'):
            b[j]='W'
        else:
            b[j]='x'
    return b


def GenerateMovesOpening(posboard):
    L = list(GenerateAdd(posboard))
    return L


def GenerateMovesOpeningBlack(b):
    y = boardreverse(b)
    Bplay = list()
    Bplay = GenerateAdd(y)
    plays = list()
    for ele in range(0,len(Bplay)):
        b = Bplay[ele]
        plays.insert(ele,boardreverse(b))
    return plays 

def GenerateMove(pos_board):
    L1=list()
    x= len(pos_board)
    for location in range(0,x):
        if (pos_board[location]=='W'):
            n=adjoint_list(location)
            for j in n:
                if (pos_board[j]=='x'):
                    b=mycopyfunc(pos_board)
                    b[location]='x'
                    b[j]='W'
                    if(CloseMill(j,b)):
                        L1=GenerateRemove(b,L1)
                    else:
                        L1.append(b)
    return L1


def GenerateMovesMidGameEndGame(pos_board):
    newlist=list()
    white_counter=0
    x=len(pos_board)

    for z in range(0,x):
        if(pos_board[z]=='W'):
            white_counter+=1
    
    if(white_counter!=3):
        newlist=GenerateMove(pos_board)
    else:
        newlist=GenerateHopping(pos_board)
    return newlist

def GenerateMovesMidGameEndGameBlack(pos_board):
    k = boardreverse(pos_board)
    newlist = list()
    newlist1 = GenerateMovesMidGameEndGame(k)
    for pos in range(0,len(newlist1)):
        b = newlist1[pos]
        newlist.insert(pos,boardreverse(b))
    return newlist

def GenerateHopping(pos_board):
    x=len(pos_board)
    newlist1=list()
    for alpha_location in range(0,x):
        if(pos_board[alpha_location]=='W'):
            for beta_location in range(0,x):
                if(pos_board[beta_location]=='x'):
                    b=mycopyfunc(pos_board)
                    b[alpha_location]='x'
                    b[beta_location]='W'
                    if(CloseMill(beta_location,b)):
                        newlist1=GenerateRemove(b,newlist1)    
                    else:
                        newlist1.append(b)
    return newlist1

#Static estimater which will be used for Opening phase
def Static_estimate_for_whiteopening(pos):
    pieces_of_white = 0; pieces_of_black = 0; StaticEstimater = 0; temp=len(pos)
    for location in range(0,temp):
        if(pos[location]=='B'):
            pieces_of_black+=1
        elif(pos[location]=='W'):
            pieces_of_white+=1
    StaticEstimater = pieces_of_white-pieces_of_black
    return StaticEstimater
            
#Static estimater which will be used for Opening phase for black
def Static_estimate_for_blackopening(pos):
    pieces_of_white = 0; pieces_of_black = 0; StaticEstimater = 0; temp=len(pos)
    for location in range(0,temp):
        if(pos[location]=='B'):
            pieces_of_black+=1
        elif(pos[location]=='W'):
            pieces_of_white+=1
    StaticEstimater = pieces_of_black-pieces_of_white
    return StaticEstimater

#Static estimater which will be used for Improvement in Opening MiniMax
def Static_estimate_for_whiteopening_updated(pos):
    pieces_of_white = 0; pieces_of_black = 0; StaticEstimater = 0; temp=len(pos);gamemill=0
    for location in range(0,temp):
        if(pos[location]=='B'):
                pieces_of_black+=1
        elif(pos[location]=='W'):
                pieces_of_white+=1
    StaticEstimater = pieces_of_white-pieces_of_black
    for each in range(0,temp):
        if(pos[each]=='x'):
            if(Mills_case(each,pos,"W")==True):
                gamemill += 1
    new_estimater = gamemill + StaticEstimater
    return new_estimater

#Static estimater which will be used for Improvement in Game MiniMax 
def Static_estimate_for_whiteopening_updated1(pos):
    pieces_of_white = 0; pieces_of_black = 0; StaticEstimater = 0; temp=len(pos);gamemill=0
    for location in range(0,temp):
        if(pos[location]=='B'):
                pieces_of_black+=1
        elif(pos[location]=='W'):
                pieces_of_white+=1
    StaticEstimater = pieces_of_white-pieces_of_black
    for each in range(0,temp):
        if(pos[each]=='x'):
            if(Mills_case(each,pos,"W")==True):
                gamemill += 1
    new_estimater = gamemill + StaticEstimater
    return new_estimater,pieces_of_black,pieces_of_white

class main():
    
    def __init__(self,head=0,counter=0,place_of_board=list()):
        self.counter = counter
        self.head = head
        self.place_of_board = place_of_board
    
  


