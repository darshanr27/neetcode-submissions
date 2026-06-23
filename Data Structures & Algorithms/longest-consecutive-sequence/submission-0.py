class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        maxLen = 0
        for i in range(n):
            consArr = set([nums[i]])
            j = 1
            while j < n:
                if nums[i] + j in nums:
                    consArr.add(nums[i] + j)
                    j += 1
                else:
                    break
            if len(consArr) > maxLen:
                maxLen = len(consArr)
        return maxLen