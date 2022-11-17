#숫자카드 100장 1~100까지 
# 2 이상 100이하의 자연수를 하나 정해 그 수보다 작거나 같은 숫자카드를 준비
# 준비한 카드의 수만큼 작은 상자를 준비하면 시작

#rule 준비된 상자에 카드를 한장씩 넣고, 상자를 무작위로 썩어 일렬로 나열한다
#상자가 일렬로 나열되면 상자가 나열된 순서에 따라 1번부터 순차적으로 증가하는 번호를 붙힌다.
#임의의 상자를 하나 선택하여 상자안의 숫자 카드를 확인
#확인한 카드에 적힌 번호에 해당하는 상자를 열어 안에 담긴 카드에 적힌 숫자를 확인
#계속 반복하다 열어야 하는 상자가 이미 열려있을 때 멈춘다

#이렇게 연 상자들은 1번 그룹이다
#1번 그룹은 다른 상자들과 섞이지 않도록 따로 둔다
#만약 1번 그룹을 제외하고 남는 상자가 없으면 게임이 졸료되고, 이때 획득하는 점수는 0점이다

#그렇지 않으면 남은 상자 중 다시 임의의 상자 하나를 골ㄹ ㅏ같은 방식으로 진행한다
#이 상자들이 2번 그룹이다

#1번그룹에 속한 상자의 수와 2번 그룹에 속한 ㄴ상자의 수를 곱한 값이 게임의 점수다

#상자안에 들어있는 카드번호가 순서대로 담긴 카드배열 cards가 매개변수로 주어질 때 
#이 게임에서 얻을수 있는 최고점수를 구해서 return하는 solution함수를 만들어라

#2 <= cards의 길이 <= 100
# cards의 원소는 cards길이 이하인 임의의 자연수
# cards에는 중복되는 원소 없음
# cards[i]는 i+1 상자에 담긴 카드의 숫자

#ex 입력 cards : 8 6 3 7 2 5 1 4
#   출력 12
import random , copy

cards = []
cards2 = []
gloop=[[]]
gloop_T=[]
for i in range(1,9):
    cards2.append(i)
for i in range(len(cards2)):
    cards.append(cards2.pop(random.randrange(0 , len(cards2))))
    # cards.append(cards2.pop(random.choice(cards2)))
    gloop.append([])

def solution(cards):
    # cards = [8,6,3,7,2,5,1,4]
    # cards2 = cards[:]
    m=0
    i = cards.index(random.choice(cards))
    while len(cards) != len(gloop_T):
        try:
            i = cards[i-1]
            if i in gloop_T:
                m += 1
                i = cards[random.choice(cards)-1]
            else: 
                gloop[m].append(i)
                gloop_T.append(i)           
        except IndexError:
            # print('에러남')
            break
    cards2 = []
    
    for i in gloop:
        G_size=len(i)
        if G_size > 0:
            cards2.append(G_size)
            print(i)
            
    if len(cards2) > 2:
        max1 = cards2.pop(cards2.index(max(cards2)))
        print('max1',max1)

        max2 = cards2.pop(cards2.index(max(cards2)))
        print('max2',max2)
        answer = max1 * max2
    else:
        answer = 0
    print(cards2)
        
        
        

    
    return answer
           
A=solution(cards)
print(A)
