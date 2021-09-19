import sys
'''
16. 最接近的三数之和
给定一个包括n 个整数的数组nums和 一个目标值target。找出nums中的三个整数，使得它们的和与target最接近。返回这三个数的和。假定每组输入只存在唯一答案。
示例：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
'''

class Solution:
    def threeSumClosest(self, nums, target):
        numLen = len(nums)
        nums.sort()
        minRes = sys.maxsize
        res = 0
        for first in range(0, numLen - 2):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            third = numLen - 1
            second = first + 1
            while second < third:
                if second > first + 1 and nums[second] == nums[second - 1]:
                    second += 1
                    continue
                temp = nums[first] + nums[second] + nums[third] - target
                if abs(temp) < minRes:
                    minRes = abs(temp)
                    res = nums[first] + nums[second] + nums[third]
                if temp > 0:
                    third -= 1
                elif temp < 0:
                    second += 1
                else:
                    return res
                if third <= second:
                    break
        return res


if __name__ == "__main__":
    nums = [1, 1, -1, -1, 3]
    target = -1
    so = Solution()
    res = so.threeSumClosest(nums, target)
    print(res)
