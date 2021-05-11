import time
a=[
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
    
]
"""
a[3][2]='Y'
a[4][2]='Y'
a[5][2]='Y'

a[6][4]='Y'
a[6][5]='Y'
a[6][3]='Y'"""
#__________________Heuristic Value_____________
value=[
    [6,-5,5,3,3,5,-5,6],
    [-5,-6,-2,-1,-1,-2,-6,-5],
    [5,-2,4,2,2,4,-2,5],
    [3,-1,2,0,0,2,-1,3],
    [3,-1,2,0,0,2,-1,3],
    [5,-2,4,2,2,4,-2,5],
    [-5,-6,-2,-1,-1,-2,-6,-5],
    [6,-5,5,3,3,5,-5,6]

]
#_________________________________________________
player1=0
player2=0

count=1
no=0
z=1
x_1,x_2=0,0
f=0
print('\nBoard is ready For Othello game')

a[3][3]='Y'
a[3][4]='X'
a[4][3]='X'
a[4][4]='Y'
#______________________ Initial Board Printing______________________
for i in range(1,9):
    if i==1:
        print('  ',i,end='  ')

    else:
        print(i,end='  ')
print()

for i in a:
    if z>8:
        z=1
    print(z,end='  ')
    z=z+1
    for j in i:
        print(j,end='  ')
        f=f+1
        if f==8:
            f=0
            print()

print()
f_2=0
while True:
    #______Input value_____
    x=int(input('Put value between(1-8) for "X" axis='))
    if x==9:
        print('\nGame is Terminated..!\n')
        break
    y=int(input('Put value between(1-8) for "Y" axis='))
    x=x-1
    y=y-1
    print()
    print()

    a[x][y]='X'
    print()
# ____________________________Horizontal check_______________________________________
    for c in range(8):
        
        if a[x][c]=='X':

            count=count+1
            
            if count==2:
                x_1=c+1
            elif count==3:
                x_2=c+1
    
    print()
    if x_1>x_2:
        temp=x_1
        x_1=x_2
        x_2=temp

    #print('x_1=',x_1,'x_2=',x_2)
    print()
    for c in range(x_1,x_2):
        if a[x][c]==0:
            no=1
            
    if x_1>0 and no==0:
        for c in range(x_1,x_2):
            a[x][c]='X'
   
    x_1=0
    x_2=0
    count=1
    no=0
    #_________________________finish____________________
#____________________________________vartical Check___________________
    x_3=0
    x_4=0
    count_2=1
    no_2=0
    for c in range(8):
        if a[c][y]=='X':

            count_2=count_2+1
            
            if count_2==2:
                x_3=c+1
            elif count_2==3:
                x_4=c+1
    print()
    if x_3>x_4:
        temp=x_3
        x_3=x_4
        x_4=temp
    #print('x_3=',x_3,'x_4=',x_4)
    print()
    for c in range(x_3,x_4):
        if a[c][y]==0:
            no_2=1
    if x_3>0 and no_2==0:
        for c in range(x_3,x_4):
            a[c][y]='X'

    x_3=0
    x_4=0
    count_2=1
    no_2=0
    
    #_________________________finish______________________
     #___________array printing____________
    for i in range(1,9):
        if i==1:
            print('  ',i,end='  ')

        else:
         print(i,end='  ')
    
    print()
    for i in a:
        if z>8:
            z=1
        print(z,end='  ')
        z=z+1
        for j in i:
            print(j,end='  ')
            f=f+1
            if f==8:
                f=0
                print()
            
    print()
    print()
    for i in range(8):
        for j in range(8):
            if a[i][j]=="X":
                player1=player1+1
            if a[i][j]=="Y":
                player2=player2+1

    print("X score is=",player1)
    print("Y score is=",player2)
    player1=0
    player2=0

#___________board finishing test_________________________
  
    for i in a:
        for j in i:
            if j==0:
                f_2+=1

    if f_2==0:
        print('\n ***** All turn are finished ,Game is over  *****\n')
        break
    f_2=0
    #________________Machine turn_________________
    print('Machine is thinking........')
    #____________________________________Time.Sleep()_________________________
    time.sleep(2)
    print("\n***Machine  has played...***")
    print()
    print("*****")
    
    x_v=0
    y_v=0
    #corner check
    if x==1 and y==0:
        x=x-1
        a[x][y]='Y'
        x_v,y_v=x,y
        print('Machine trun into',x+1,y+1)
    elif x==0 and y==1:
        y=y-1
        a[x][y]='Y'
        x_v,y_v=x,y
        print('Machine trun into',x+1,y+1)
    elif x==0 and y==6:
        y=y+1
        a[x][y]='Y'
        x_v,y_v=x,y
        print('Machine trun into',x+1,y+1)
    elif x==1 and y==7:
        x=x-1
        a[x][y]='Y'
        x_v,y_v=x,y
        print('Machine trun into',x+1,y+1)

    elif x==6 and y==1:
        x=x+1
        a[x][y]='Y'
        x_v,y_v=x,y
        print('Machine trun into',x+1,y+1)
    elif x==7 and y==2:
        y=y-1
        a[x][y]='Y'
        x_v,y_v=x,y
        print('Machine trun into',x+1,y+1)

    elif x==6 and y==7:
        x=x+1
        a[x][y]='Y'
        x_v,y_v=x,y
        print('Machine trun into',x+1,y+1)
    elif x==7 and y==6:
        y=y+1
        a[x][y]='Y'
        x_v,y_v=x,y
        print('Machine trun into',x+1,y+1)
    elif x!=0 and y==0:
        y=y+1
        a[x][y]='Y'
        x_v,y_v=x,y
        print('Machine trun into',x+1,y+1)
    elif x==0 and y!=0:

        x=x+1
        a[x][y]='Y'
        x_v,y_v=x,y
        print('Machine trun into',x+1,y+1)
    #_________normal check_______
    elif x!=0 and y!=0:
        if a[x][y-1]==0:
            y=y-1
            a[x][y]='Y'
            x_v,y_v=x,y
            print('Machine trun into',x+1,y+1)
        elif a[x][y-1]!=0 and a[x][y+1]==0:
            y=y+1
            a[x][y]='Y'
            x_v,y_v=x,y
            print('Machine trun into',x+1,y+1)
        elif a[x][y-1]!=0 and a[x][y+1]!=0 and a[x+1][y]==0:
            x=x+1
            a[x][y]='Y'
            x_v,y_v=x,y
            print('Machine trun into',x+1,y+1)
        
    print("*****")
    
        
    #___________________Machine Horijontal Check______________
    
    count_3=1
    no_3=0
    x_5,x_6=0,0
    for c in range(8):
        
        if a[x_v][c]=='Y':

            count_3=count_3+1
            
            if count_3==2:
                x_5=c+1
            elif count_3==3:
                x_6=c+1
    #print()
    if x_5>x_6:
        temp=x_5
        x_5=x_6
        x_6=temp
    #print('x_5=',x_5,'x_6=',x_6)
    #print()
    for c in range(x_5,x_6):
        if a[x][c]==0:
            no_3=1
    if x_5>0 and no_3==0:
        for c in range(x_5,x_6):
            a[x][c]='Y'
    x_5=0
    x_6=0
    count_3=1
    no_3=0
    #____________________machine vertical Check________________________
    x_7=0
    x_8=0
    count_4=1
    no_4=0
    for c in range(8):
        if a[c][y_v]=='Y':

            count_4=count_4+1
            
            if count_4==2:
                x_7=c+1
            elif count_4==3:
                x_8=c+1
    print()
    if x_7>x_8:
        temp=x_7
        x_7=x_8
        x_8=temp
    #print('x_3=',x_3,'x_4=',x_4)
    print()
    for c in range(x_7,x_8):
        if a[c][y]==0:
            no_4=1
    if x_7>0 and no_4==0:
        for c in range(x_7,x_8):
            a[c][y]='Y'

    x_7=0
    x_8=0
    count_4=1
    no_=0
    #___________array printing____________
    for i in range(1,9):
        if i==1:
            print('  ',i,end='  ')

        else:
         print(i,end='  ')
    print()
    print()
    for i in a:
        if z>8:
            z=1
        print(z,end='  ')
        z=z+1
        for j in i:
            print(j,end='  ')
            f=f+1
            if f==8:
                f=0
                print()
    print()
    print()
    for i in range(8):
        for j in range(8):
            if a[i][j]=="X":
                player1=player1+1
            if a[i][j]=="Y":
                player2=player2+1

    print("Your score is=",player1)
    print("Computer score is=",player2)
    player1=0
    player2=0
    print()

 

    
                
        

     