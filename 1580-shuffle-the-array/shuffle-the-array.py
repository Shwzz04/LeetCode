class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n = len(nums)
        mid = n//2
        arr= []
        for i in range(mid):
            arr.append(nums[i])
            arr.append(nums[mid+i])
        return arr
