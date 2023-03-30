import sys
from pprint import pprint
sys.stdin = open('input.txt', 'r')
#####
arr1 = [0] + list(input())
arr2 = [0] + list(input())
n1 = len(arr1)
n2 = len(arr2)
dp = [[0]*n2 for _ in range(n1)]

# LCS 길이 찾기
for i in range(1, n1):
    for j in range(1, n2):
        # 같으면 i-1, j-1번째 값에 + 1
        if arr1[i] == arr2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        # 다르면 위랑 왼쪽 값중 큰값
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])

# LCS 찾기
# 끝에서부터 시작
i, j = n1 - 1, n2 - 1
res = []
# 0을 만날 때까지
while dp[i][j] != 0:
    # 위나 왼쪽이랑 같으면 해당 인덱스로 이동
    if dp[i][j] == dp[i-1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j-1]:
        j -= 1
    # 위나 왼쪽이랑 같은 값이 없으면 해당 인덱스에 해당하는 val 넣고 i-=1, j-=1
    else:
        res.append(arr2[j])
        i, j = i-1, j-1

# res를 거꾸로 출력
print(''.join(res[::-1]))