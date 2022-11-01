f1 = open("maze.txt" , 'r')
lines = f1.readlines()
f1.close()
lines
X_point = len(lines)
X_point

#리스트를 문자열로 바꾼뒤 줄바꿈 지우고 가공
line = " ".join(lines)
line
line = line.replace("\n","")
list_line = line.split(" ")

#list
list_line
print(len(list_line))
list_line.index('S')
Y_point = len(list_line)/X_point
Y_point = round(Y_point)
Y_point
        
#맵 2차 리스트로
maze_map = list()
X = 0
Y = X_point
for i in range(X,Y_point):
    maze_map.append(list_line[ X : Y ])
    print(i ,end=" ")
    print("X",X ,end="")
    print(" Y",Y)
    X = +Y
    Y += X_point
maze_map
type(maze_map)
maze_map[0].index('F')
maze_map[8].index('P')
# print(" ".join(maze_map))
               
for i in range(X_point):
    for j in range(Y_point):
        print("[ %d : %d ]" %(i,j) , end=" ")
    # print("")
        print(maze_map[i][j],end="")
        if maze_map[i][j]=='S':
            # print(maze_map[i][j])
            Start_P = maze_map[i].pop(j)
            maze_map[i].insert(j,'P')


# next_P = Start_P

class Move():
    global X_point
    global Y_point
    global maze_map        
    for i in range(X_point):
        maze_map[i].index('P')
        x = i
        y = j
        print( x, y )

    for i in range(X_point):
        for j in maze_map:
            j[i].index('P')
            if j[i] == 'P'
                x=i
                y=j
                break
    print( x , y )
        
    
def main():
    #초기 S 에 P 놓기
    while True:
        for i in range(X_point):
            for j in range(Y_point):
                # print("[ %d : %d ]" %(i,j) , end=" ")
                print(maze_map[i][j],end="")
            print("")
        #P꺼내기    
        print("어디로 갈까?")
        print("1. 동 쪽으로")
        print("2. 서 쪽으로")
        print("3. 남 쪽으로")
        print("4. 북 쪽으로")        
        x = int(input())
                
        for i in range(X_point):
            for j in range(Y_point):
                # print("[ %d : %d ]" %(i,j) , end=" ")
                # print(maze_map[i][j],end="")
                if maze_map[i][j]=='P':
                    print(maze_map[i][j])
                    Player = maze_map[i].pop(j)
                    maze_map[i].insert(j,next_P)
                    
                    next_P = maze_map[i+1].pop(j)
                    maze_map[i+1].insert(j,Player)
                    
                    if x == 1:
                        next_P = maze_map[i].pop(j+1)
                        maze_map[i].insert(j+1,Player)    
                    elif x == 2:
                        maze_map[i].insert(j,next_P)
                        maze_map[i].insert(j,next_P)    
                    elif x == 3:
                        maze_map[i].insert(j,next_P)
                        maze_map[i].insert(j,next_P)    
                    elif x == 4:
                        maze_map[i].insert(j,next_P)
                        maze_map[i].insert(j,next_P)    
                    else: print("다시골라")
                    
                    
            
        
        