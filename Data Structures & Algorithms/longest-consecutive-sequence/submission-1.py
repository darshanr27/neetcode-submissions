class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # For efficient checks converting array to set 
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # Check start of the sequence
            if (n-1) not in numSet:
                length = 0
                # If it's the start, find the sequence and length
                while (n+length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest