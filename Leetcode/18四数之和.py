import sys

'''
给你一个由 n 个整数组成的数组nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] ：

0 <= a, b, c, d< n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。
'''


class Solution:
    def fourSum(self, nums, target):
        res = []
        numLen = len(nums)
        if numLen < 3:
            return res
        nums.sort()
        for first in range(numLen - 3):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            if nums[first] + nums[first + 1] + nums[first + 2] + nums[first + 3] > target:
                break
            for second in range(first + 1, numLen - 2):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                fourth = numLen - 1
                for third in range(second + 1, numLen - 1):
                    if third > second + 1 and nums[third] == nums[third - 1]:
                        continue
                    while nums[first] + nums[second] + nums[third] + nums[fourth] > target and fourth:
                        fourth -= 1
                    if third >= fourth:
                        break
                    if nums[first] + nums[second] + nums[third] + nums[fourth] == target:
                        res.append([nums[first], nums[second], nums[third], nums[fourth]])
        return res


if __name__ == "__main__":
    nums = [-3, -2, -1, 0, 0, 1, 2, 3]
    target = 0
    so = Solution()
    res = so.fourSum(nums, target)
    nums.sort()
    print(nums)
    print(res)
    print([[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2], [-2, -1, 0, 3], [-2, -1, 1, 2], [-2, 0, 0, 2],
           [-1, 0, 0, 1]])
