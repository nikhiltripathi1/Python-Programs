from random import choice
value=["","","","","","","","",""]
index=[0,1,2,3,4,5,6,7,8]
get=""
out=""
take=0
def board(value):
    print("\tTIC-TAC-TOE\n")
    print(" | ",value[0]," | ",value[1]," | ",value[2]," | ")
    print("-----------------")
    print(" | ",value[3]," | ",value[4]," | ",value[5]," | ")
    print("-----------------")
    print(" | ",value[6]," | ",value[7]," | ",value[8]," | ")

def chance():
    ch=input("want first chance?(y/n):").lower()
    if ch=='y':
       first="human"
    else:
       first="computer"
    return first   
       

def symbol():
    get=input("choose either \"x\" or \"o\":").lower()   
    return get

def assign(value,first,get,out):
    if first=="human":
        take=int(input("enter no.(0-8):"))
        value[take]=get
        index.remove(take)
        let=choice(index)
        value[let]=out
        index.remove(let)
    else:
        let=choice(index)
        value[let]=out
        index.remove(let)
        take=int(input("enter no.(0-8):"))
        value[take]=get
        index.remove(take)


def winnerg(value,get):
    winner='n'
    win=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for row in win:
         if value[row[0]]==value[row[1]]==value[row[2]]!="":
            if value[row[0]]==get:
                winner="human"
                print("\nyouwon!!!\n congratulations!!!")
            else:
                winner="computer"
                print("\nyou lose...\ntry again...")
    return winner           
    
    
def main():
    print("\tTIC-TAC-TOE\n")
    print(" | 0 | 1 | 2 | ")
    print("-----------------")
    print(" | 3 | 4 | 5 | ")
    print("-----------------")
    print(" | 6 | 7 | 8 | ")

    f=chance()
    get=symbol()
    if get=='x':
        out='o'
    else:
        out='x'
    for i in range(4):
         assign(value,f,get,out)
         board(value)
         winner=winnerg(value,get)
         if winner!="n":
             break

    if winner=="n":
         print("TIE")

main()
