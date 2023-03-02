import sys
sys.stdin = open('input.txt', 'r')

s = "aabbbdbaac"
p = "a*.*dba*c"

def isMatch(s: str, p: str) -> bool:
    s, p = ' '+ s, ' '+ p
    lenS, lenP = len(s), len(p)
    dp = [[0]*(lenP) for i in range(lenS)]
    dp[0][0] = 1

    # init
    for j in range(1, lenP):
        if p[j] == '*':
            dp[0][j] = dp[0][j-2]
    
    # s의 각 글자 s[i], p의 각 글자 p[j]
    for i in range(1, lenS):
        for j in range(1, lenP):
            if p[j] in {s[i], '.'}:     # 동일하거나 . 인 경우
                dp[i][j] = dp[i-1][j-1] # 대각으로 감
            elif p[j] == "*":           # *인 경우 이전 값
                dp[i][j] = dp[i][j-2] or int(dp[i-1][j] and p[j - 1] in {s[i], '.'})
                
    print('-' * 30, end ="\n  ")
    for col in range(lenP): print(f" {p[col]}", end = " ")
    print()                
    for row in range(lenS): print(f"{s[row]} {dp[row]}")

    return bool(dp[-1][-1])

print(isMatch(s, p))
