x,y,z= [],[],[]

def Input(x,y,z):
    global n ,F
    F = 0
    while True:
        X , Y  = input().split()
        X = int(X)
        Y = int(Y)
        Z =0.25*X+ 0.75*Y
        if X < 0 :
            break
        if Z < 90:
            continue
        if X+Y==200: # 그냥 1등
            F=1
        x.append(X)
        y.append(Y)
        z.append([Z,X,Y])
        n = len(z)
    return x,y,z,n
    
def Sort(x,y,z,n):
    z.sort(reverse=True)
    return x,y,z,n

def Output(x,y,z,n):
    for m in range(n):
        print(z[m][1],z[m][2],z[m][0])
    if F == 1:
        print("1등은 만점 팀")
    elif n == 0:
        print("Not found")

Input(x,y,z)
Sort(x,y,z,n)
Output(x,y,z,n)
