import sys

input = sys.stdin.readline

n = int(input())
X = []
Y = []
for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

area = (max(X)-min(X))*(max(Y)-min(Y))
print(area)