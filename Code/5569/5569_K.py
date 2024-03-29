# 출근 경로
import sys
sys.stdin = open('input.txt', 'r')
from pprint import pprint

w, h = map(int, input().split())    # w는 c에 대응, h는 r에 대응

# 초기화
dp = [[[[0, 0], [0, 0]] for _ in range(w)] for _ in range(h)]

# 초기화
for r in range(1, h):
    dp[r][0][0][1] = 1      # 초기값: 북쪽 접근 + 회전 가능

for c in range(1, w):
    dp[0][c][1][1] = 1      # 초기값: 동쪽 접근 + 회전 가능

for c in range(1, w):
    for r in range(1, h):
        dp[r][c][0][0] = dp[r-1][c][1][1]                       # 북쪽 접근 + 회전 불가능 -> 이전 위치에서 동쪽 접근+ 회전 가능
        dp[r][c][0][1] = dp[r-1][c][0][0] + dp[r-1][c][0][1]    # 북쪽 접근 + 회전 가능 -> 이전 위치에서 북쪽 접근 + 회전 불가능/회전 가능
        dp[r][c][1][0] = dp[r][c-1][0][1]                       # 동쪽 접근 + 회전 불가능 -> 이전 위치에서 북쪽 접근 + 회전 가능
        dp[r][c][1][1] = dp[r][c-1][1][0] + dp[r][c-1][1][1]    # 동쪽 접근 + 회전 가능 -> 이전 위치에서 동쪽 접근 + 회전 불가능/회전 가능

ans = sum(dp[h-1][w-1][0]) + sum(dp[h-1][w-1][1])       # 도착지점에서의 모든 경우의 수의 합
print(ans % 100000)