#NICE!
#https://www.reddit.com/r/learnpython/comments/g8rvag/do_programmers_save_chunks_of_code_for_repeated/
#hier sollte etwas mehr kommentiert werden
#a message from degi
def iswinner(b, p):
    if 3*p in [b[x]+b[y]+b[z] for x,y,z in [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]]: return True

def iswinner_original(b, p):    
    for x,y,z in [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]:
        if p==b[x]==b[y]==b[z]:
            return True
    return False


##CodeGolf Challenge

def iswinner5(b, p):
    s,c,l,w=0,"cat","loose","win"
    for i in 1,2,3,4:
        u=2*i-1  
        a=i*i-5*i+3
        if b[4]==b[4+i]==b[4-i]:
            if p==b[4]:s+=1
            else:s-=1            
        if b[u]==b[u+a]==b[u-a]:
            if p==b[u]:s+=1
            else:s-=1
    if s>0:c=w
    if s<0:c=l
    return c
           

##AKTUELL
## Magisches Quadrat
def iswinner6(b,p=1):
 n=[x*y for x,y in zip(b,(2,9,4,7,5,3,6,1,8))]
 if 15 in [x+y+z for x in n for y in n if x!=y for z in n if z!=x and z!=y]: return True

## 3b umformen
def iswinner4(b, p):
 for i in 1,2,3,4:
  u=2*i-1  
  a=i*i-5*i+3   
  if b[4]+b[4+i]+b[4-i]==3*p or b[u]+b[u+a]+b[u-a]==3*p: return True
        

## Dani 29042020, IDEE: Abstandsfunktion Merge - elegante Lösung
## 4 +- 1,2,3,4
## f(x)=-(0.5x-2)^2 + 13/4 im Code wird wegen +- ein Zeichen gespart :)
def iswinner3(b, p):
    for i in 1,2,3,4:
        u=2*i-1    
        a=int(u*u/4-2*u+3/4)        
        if b[4]==b[4+i]==b[4-i]==p or b[u]==b[u+a]==b[u-a]==p:
            return True
    else:
        return False
    
## Dani 29042020, Idee: Abstände
## 1,7 +- 1
## 4 +- 1,2,3,4
## 3/5+-3
def iswinner2(board, player):
    for i in (1,2,3,4):
        if board[4]==board[4-i]==board[4+i]==player:
            return True
    for i in (1,7):
        if board[i]==board[i-1]==board[i+1]==player:
            return True    
    for i in (3,5):
        if board[i]==board[i+3]==board[i-3]==player:
            return True
    else: return False


#fields = (1,1,1,0,0,0,0,1,1)
fields = (0,0,0,0,0,1,1,1,1)
player = 1
check = iswinner(fields, player)
print ("Check1:", check)
check2 = iswinner2(fields, player)
print ("Check2:", check2)
check3 = iswinner3(fields, player)
print ("Check3:", check3)
check4 = iswinner4(fields, player)
print ("Check4:", check4)
check5 = iswinner5(fields, player)
print ("Codegolf:", check5)
check6 = iswinner6(fields, player)
print ("Check6:", check6)

p=player
b=fields


    

