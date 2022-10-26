f1 = open("maze" , 'r')
lines = f1.readlines()
f1.close()
lines
#불러온거 문자열로 바꾸고 공백 추가
line = " ".join(lines)
line = " ".join(line)
line
#공백 지우고 가공
line = line.replace(" ","")
line = " ".join(line)
list_line = line.split(" ")
line
#list
list_line
#문자열
str_line = " ".join(list_line)
str_line

start_p = list_line.index('S')
# start_p

#플레이어 넣어주고
list_line.insert(start_p,'P')
player = list_line.index('P')
next = list_line.pop(start_p+1)
next

for i in list_line:
    print(i,end="")

class move(x):
    x=x
    def right():
        player = list_line.index('P')
        list_line.insert(player,next)
        next = list_line.pop(player+1)
        list_line.insert(player+1,next)
        player = list_line.index('P')
        next = list_line.pop(player+1)
        for i in list_line:
            print(i,end="")

        return list_line
            
    def left():
        player = list_line.index('P')
        list_line.insert(player,next)
        player = list_line.index('P')
        next = list_line.pop(player)
        list_line.insert(player-1,next)
        player = list_line.index('P')
        next = list_line.pop(player-1)
        for i in list_line:
            print(i,end="")

    if x == 3:
        player = list_line.index('P')
        list_line.insert(player+1, next)
        player = list_line.index('P')
        next = list_line.pop(player)
        list_line.insert(player+10,next)
        player = list_line.index('P')
        next = list_line.pop(player+1)
        for i in list_line: 
            print(i,end="")

    if x == 4:
        player = list_line.index('P')
        player
        next
        list_line.insert(player, next)
        next = list_line.pop(player+1)
        list_line.insert(player-9,next)
        player = list_line.index('P')
        next = list_line.pop(player-1)
        for i in list_line: 
            print(i,end="")
    

def main():
    while next != 'x':
        print("어디로 갈까?")
        print("1. 동 쪽으로")
        print("2. 서 쪽으로")
        print("3. 남 쪽으로")
        print("4. 북 쪽으로")
        
        x = int(input())
        m = move()
        m.right

        if x == 1:
            player = list_line.index('P')
            list_line.insert(player,next)
            next = list_line.pop(player+1)
            list_line.insert(player+1,next)
            player = list_line.index('P')
            next = list_line.pop(player+1)
            for i in list_line:
                print(i,end="")
        
        if x == 2:
            player = list_line.index('P')
            list_line.insert(player,next)
            player = list_line.index('P')
            next = list_line.pop(player)
            list_line.insert(player-1,next)
            player = list_line.index('P')
            next = list_line.pop(player-1)
            for i in list_line:
                print(i,end="")

        if x == 3:
            player = list_line.index('P')
            list_line.insert(player+1, next)
            player = list_line.index('P')
            next = list_line.pop(player)
            list_line.insert(player+10,next)
            player = list_line.index('P')
            next = list_line.pop(player+1)
            for i in list_line: 
                print(i,end="")

        if x == 4:
            player = list_line.index('P')
            player
            next
            list_line.insert(player, next)
            next = list_line.pop(player+1)
            list_line.insert(player-9,next)
            player = list_line.index('P')
            next = list_line.pop(player-1)
            for i in list_line: 
                print(i,end="")
