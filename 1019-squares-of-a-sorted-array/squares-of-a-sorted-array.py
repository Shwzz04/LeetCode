class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        sarr = []
        n = len(nums)

        for i in range(n):
            temp = nums[i]
            s = temp ** 2
            sarr.append(s)
            
        sarr.sort()    
        return sarr
