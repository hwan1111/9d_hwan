# 윤년 구하기 (이중선택)

year = int(input())

if year % 4 == 0 :                              #4로 나눠떨어지는 year값중~
    if year % 100 == 0 :                        #100으로 나눠 떨어지는 값중~
        if year % 400 == 0 :                    #400으로 나눠 떨어지는 값은 윤년임
            print("1") 
        else :                                  #4와 100으로 나눠 떨어지지만 400으로는 나눠 떨어지지는 않는 값은 평년임
            print("0")
    else :                                      #4로만 나눠 떨어지는 값은 윤년임
        print("1")
else :                                          #4로 나눠 떨어지지 않는 값은 평년
    print("0")