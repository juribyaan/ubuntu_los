import os
f1 = open("/home/juribyaab/catkin_ws/maze.txt" , 'r')
lines = f1.readlines()
f1.close()
   
def main():
    global lines
    X_point = len(lines)
    line = " ".join(lines)
    list_line = line.split(" ")
    set_play = list_line.index('S')
    list_line.pop(set_play)
    list_line.insert(set_play,'P')
       
    while True:  
        os.system('clear')
        for i in range(X_point):
            print(" ".join(list_line[i*X_point:(i+1)*X_point]) ,end="" )                    
        print("어디로 갈까?")
        print("1. 동 쪽으로 2. 서 쪽으로 3. 남 쪽으로 4. 북 쪽으로")        
        x = int(input())
        set_play = list_line.index('P')
        if   x == 1:
            set_play +=  1    
        elif x == 2:
            set_play += -1
        elif x == 3:
            set_play +=  X_point
        elif x == 4:
            set_play += -X_point
        try:
            wall = list_line[set_play]
            if wall == "o" or wall == "S":
                list_line = line.split(" ")
                list_line.pop(set_play)
                list_line.insert(set_play,'P')
            elif wall =="F\n":
                break
        except IndexError:            pass             # print("거긴 못가")            
            
if __name__ == "__main__":
    main()
    print('끝')