class Solution(object):
    def threeSum(self, nums):
        numsLenth = len(nums)
        nums.sort()
        ans = list()
        for first in range(numsLenth):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            third = numsLenth - 1
            for second in range(first + 1, numsLenth):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while second < third and nums[first] + nums[second] + nums[third] > 0:
                    third -= 1
                if second >= third:
                    break
                if nums[first] + nums[second] + nums[third] == 0:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans


if __name__ == "__main__":
    s = Solution()
    nums = [3, 0, -2, -1, 1, 2]
    ans = s.threeSum(nums)
    print(ans)
