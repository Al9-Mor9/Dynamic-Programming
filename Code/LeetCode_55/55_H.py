class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n ==1:return True

        visited = [0] * n
        now = 0
        q = [now]
        while q:
            now = q.pop(0)
            visited[now] = 1
            for i in range(1, nums[now]+1):
                # 조건문 for문 안에 안넣으니 시간초과 떴음ㅠ
                if now+i == n - 1: return True
                if 0 <= now+i < n and not visited[now+i]:
                    visited[now+i] = 1
                    q.append(now+i)
        return False