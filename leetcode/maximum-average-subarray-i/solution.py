class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n = len(nums)
        curr_sum= sum(nums[:k])
        max_avg = curr_sum        
        for i in range (k,n):
            curr_sum += nums[i]
            curr_sum -= nums[i-k]

            max_avg = max (max_avg, curr_sum )
        return max_avg/k
        # Time: O(n)