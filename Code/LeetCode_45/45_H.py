class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(1, nums[i] + 1):
                # print(i, j)
                # 범위 넘어가면 continue
                if i + j >= len(nums):
                    continue
                # 한번도 안간 곳이면 count += 1
                if cnt[i + j] == 0:
                    # 도착했으면 바로 리턴
                    if i+j == n-1: return cnt[i] + 1
                    cnt[i + j] = cnt[i] + 1
                # print(cnt)
        return cnt[len(nums) - 1]
#
# def jump(nums):
#     n = len(nums)
#     cnt = [0] * len(nums)
#     for i in range(len(nums)):
#         for j in range(1, nums[i] + 1):
#             # print(i, j)
#             # 범위 넘어가면 continue
#             if i + j >= len(nums):
#                 continue
#             # 한번도 안간 곳이면 count += 1
#             if cnt[i + j] == 0:
#                 # 도착했으면 바로 리턴
#                 if i+j == n-1: return cnt[i] + 1
#                 # 현재단계까지 오는데 필요한 cnt + 1 저장
#                 cnt[i + j] = cnt[i] + 1
#             # print(cnt)
#     return cnt[len(nums) - 1]
#
#
# arr = [2,3,0,1,4]
# print(arr)
# print()
# print(jump(arr))