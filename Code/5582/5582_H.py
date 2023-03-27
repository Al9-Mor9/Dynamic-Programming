import sys
from pprint import pprint
sys.stdin = open('init.txt', 'r')
#####
word1 = list(input())
word2 = list(input())
lcs = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]

ans = 0
for i in range(len(word1)):
    for j in range(len(word2)):
        if word1[i] == word2[j]:
            lcs[i][j] = lcs[i-1][j-1] + 1
    ans = max(ans, max(lcs[i]))
print(ans)
