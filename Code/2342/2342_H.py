import sys
sys.stdin = open('input.txt', 'r')
#####
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def move(a, b):  # a를 b로 이동
    if a == b:
        return 1
    elif a == 0:
        return 2
    elif abs(b - a) % 2 == 0:
        return 4
    else:
        return 3

# 발의 위치가 (l,r) 일 때 n번째 팔판부터 밟았을 때 소모되는 힘을 재귀로
def solve(n, l, r):
    global dp
    # 종료 조건
    if n >= len(arr) - 1:
        return 0

    # prunning
    if dp[n][l][r] != -1:
        return dp[n][l][r]

    # 왼발을 올리고 다음으로 진행 했을 때의 합과 오른쪽 발을 올리고 다음으로 진행했을 때의 합 중 최솟값을 리턴
    dp[n][l][r] = min(move(l, arr[n]) + solve(n + 1, arr[n], r),
                      move(r, arr[n]) + solve(n + 1, l, arr[n]))
    return dp[n][l][r]

MAXLEN = 100000
arr = list(map(int, input().split()))
dp = [[[-1] * 5 for _ in range(5)] for _ in range(MAXLEN)]

print(solve(0, 0, 0))
