num1 = int(input())
num2 = int(input())

num3 = (num2%10)*num1
num4 = ((num2//10)%10)*num1
num5 = ((num2//100)%10)*num1
num6 = num3 + num4*10 + num5*100

print(num3)
print(num4)
print(num5)
print(num6)