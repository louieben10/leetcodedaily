class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def K_works(k):
            hours=0
            for p in piles:
                hours += ceil(p/k)
            return hours <=h 

        l = 1 
        r = max(piles)
        while l < r:
            k = (l+r) //2
            if K_works(k):
                r = k 
            else:
                l = k + 1
        return l 
