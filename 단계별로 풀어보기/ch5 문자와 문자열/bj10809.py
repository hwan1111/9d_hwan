#10809, 알파벳 찾기
#한 단어에서 각 알파벳이 처음 등장하는 위치를 찾는 문제

S  = input()
alphabets = 'abcdefghijklmnopqrstuvwxyz'
List = []

for i in alphabets:
    if i in S :
        List.append(str(S.index(i)))
    else:
        List.appen("-1")

print(" ".join(List))