#수컷 5달러 암컷 3달러 병아리3 1달러
#100마리 채우기
max =101
#마리수
a = 1
b = 1
c = 3

for c1 in range(max):
    for c2 in range(max):
        for c3 in range(max):
            if c1*a+c2*b+c3*c == max-1: 
                #가격
                A = c1*a*5
                B = c2*b*3
                C = c3*c*1
                print('수컷 %d 암컷 %d 병아리 %d [가격 : %d]'  % (c1*a ,c2*b , c3*c ,A+B+C))
                break
