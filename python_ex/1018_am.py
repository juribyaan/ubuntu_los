import os
# os.sytem('cls')


word = input()
word_len=len(word)
word_list = list(word)

shap_list = list('000000')
shap_list_len = len(shap_list)


A = round(shap_list_len/2)
# print(len(shap_list))
for i in range(word_len):
    if word_len > shap_list_len:
        shap_list = list(word)
        break
    shap_list.insert(A+i,word[i])

while True:
    for i in shap_list[0 : 6]:
        print(i , end='')
    print('')
    a = shap_list.pop(0)
    shap_list.append(a)


    

    

