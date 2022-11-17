#공원 꽃길
# 구매경비  n < x < 2000
# 최소 5개씩
# 노란꽃은 빨간꽃의 2배가 필요하다 or 보라꽃은 노란꽃의 1/3 이다
# 입력문 :'%d' // 구매경비 최소값 n 입력
# 출력문 :"" 빨갛,노랑,보라 순 / 빨갛꽃의 오름차순 출력
# x = yellow_F_count*6 + red_F_count*3 + puple_F_count*2
red_F = 80
yellow_F = 50
puple_F =36
min = 5
max=2000

r = max//red_F
y = max//yellow_F
p = max//puple_F
# print(r,y,p)

cost = int(input())

for R in range(min,r):
    for Y in range(min,y):
        for P in range(min,p):
            F_cost = Y*yellow_F + R*red_F + P*puple_F
            if cost < F_cost and (R*2 == Y or Y/3 == P) and F_cost < max:
                print(R,Y,P , R*red_F+Y*yellow_F+P*puple_F)
                break
            

                
                
