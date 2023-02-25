class Solution:
    def jump(self, nums: List[int]) -> int:
        cur, jump_max = 0, 0 
        n = len(nums)
        if n == 1: return 0
        cnt = 1
        while True:
            if nums[cur] + cur >= n-1: break
            for i in range(1 , nums[cur] + 1):
                if nums[cur + i] + cur + i > jump_max + nums[jump_max]:
                    jump_max = cur + i
            cur = jump_max
            cnt += 1
        return cnt 

# Another Approach
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         cnt, n = 0, len(nums)
#         cur_end, cur = 0, 0
        
#         for i in range(n - 1):
#             cur = max(cur, i + nums[i])
#             if i == cur_end:
#                 cnt += 1
#                 cur_end = cur
#         return cnt