class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n ==1:return True

        visited = [0] * n
        cur = 0
        q = [cur]
        visited[cur] = 1

        while q:
            cur = q.pop(0)
            for i in range(1, nums[cur] + 1):
                if cur + i == n-1:  return True
                if not visited[cur + i]:
                    visited[cur + i] = 1
                    q.append(cur + i)
        return False


# Another Approach
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         n = len(nums)
#         cur = n - 1
#         for i in range(n-2, -1, -1):
#             if nums[i] + i >= cur:
#                 cur = i
#         return bool(not cur)