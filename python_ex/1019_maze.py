f2 = open("playMaze" , 'w');
f2.close();

f1 = open("maze" , 'r')
f2 = open("playMaze" , 'w')

mapreads = f1.readlines()
for mapread in mapreads:
    data = mapread
    f2.write(data)
f2.close()
f1.close()

A=len(mapreads)


def maze_map():
    for i in range(A):
        print("".join(mapreads[i]))


#maze_map()
#mapreads[0]

def move_choice():
    print("1. 동")
    print("2. 서")
    print("3. 남")
    print("4. 북")


P = 'P'
for i in range(A):
    mapreads[i]
a = A-1
now = list(mapreads[a])
up = +1
down = -1
#print(now[0:])
#type(now)
start = now.index('S')
#print(start)

now.insert(start,P)
P = now.pop(start+1)
#now.remove('S')

point = now.index('P')
print(point)
#print(P)

#
print(now)

now.insert(start,P)
P = now.pop(start+1)

p_point=point
while True:
    P
    now
    print("어디로 가볼까?")
    M = input()


    if M == 1:
        right = +2
        now.insert(p_point+3,P)
        PP = now.pop(p_point+4)
        P = PP
        p_point = p_point+3
        # return P 
    elif M == 2:
        now.insert(point,P)
        PP = now.pop(point-1)
        # return P
    elif M == 3:
        downnow = list(mapreads[a+down])
        downnow.insert(point,P)
        PP = downnow.pop(point+1)
        P = PP
        # return P
    elif M == 4:
        upnow = list(mapreads[a+up])
        upnow.insert(point,P)
        PP = upnow.pop(point+1)
        P = PP
        # return P
    else : 
        print("다시 눌러")

