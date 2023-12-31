#1193, 분수 찾기
#분수의 순서에서 규칙을 찾는 문제

#전체 적인 그래프를 아래처럼 구상함 (층수| (왼:순서{X번째}, 오:분수))
"""
1|1, 1/1
2|(2, 1/2) | (3, 2/1)
3|(4, 3/1) | (5, 2/2) | (6, 1/3)
...
"""

X = int(input())
if X == 1:          #아래랑 묶을려 했는데 그러면 복잡해서 따로 뺌
    print("1/1")
else:               
    i = 0           #i를 층수라고 봄
    while X > 0:    #층수를 알려고
        X -= i
        i += 1

    n = i-1
    X = X + n -1    #각 층수에서 X는 인덱스가 이렇게 결정됨 ex) 13은 5층에서 인덱스 2로 결정
 
    #아래와 같은 규칙성을 띔
    if i%2==0:
        arr = [f"{i-j}/{j}"for j in range(1, i)]
    else:
        arr = [f"{j}/{i-j}"for j in range(1, i)]

    print(arr[X])