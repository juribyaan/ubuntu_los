import os
import time
# os.sytem('cls')

word = input()
word_list = list(word)
word_len=len(word)

shap_list = list('00000')
shap_list_len = len(shap_list)


A = round(shap_list_len/2)
# print(len(shap_list))
for i in range(word_len):
    if word_len >= shap_list_len:
        shap_list = list(word)
        break
    shap_list.insert(A+i,word[i])

# while True:
#     for i in shap_list[0 : 5]:
#         print(i , end='')
#     print('')
#     a = shap_list.pop(0)
#     shap_list.append(a)
#     time.sleep(1)
#     os.system('clear')

# while True:
#     for i in range (word_len-1):
#         a = word_list.pop(i)
#         word_list.insert(i+1,a)
#         # print(word_list[i] , end='')
#         for i in range(word_len):
#             print(word_list[i] , end='')
#         print('')
#         time.sleep(1)
#         os.system('clear')

while True:
    for i in word_list:
        print(i , end='')
        a = word_list.pop(i)
        word_list.insert(i+1,a)
        # print(word_list[i] , end='')
    print('')
    time.sleep(1)
    os.system('clear')




    

    

