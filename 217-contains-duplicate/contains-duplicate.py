class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        counts = {}
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1

        for i in counts.values():
            if i != 1:
                return True

        return False