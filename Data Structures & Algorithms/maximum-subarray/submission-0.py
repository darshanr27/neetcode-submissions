class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = best_sum = nums[0]

        for num in nums[1:]:
            # Either extend the subarray or start a new one 
            current_sum = max(num, current_sum + num)
            # Update best_sum if current_sum is larger
            best_sum = max(best_sum, current_sum)
            
        return best_sum