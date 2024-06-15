def solution(arr1, arr2):
    # 결과 행렬 초기화
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    
    # 행렬 곱셈
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr2)):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    
    return answer