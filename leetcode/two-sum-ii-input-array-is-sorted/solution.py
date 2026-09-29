class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        l = 0 
        r = n - 1

        while l<r:
            sum_2 = numbers[l] + numbers[r]
            if sum_2 == target:
                return [l+1,r+1]
            elif sum_2 < target:
                l +=1 
            else:
                r -=1 