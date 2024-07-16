# LeetCode Question One
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        set_numbers = set([])
        for num in nums:
            if num in set_numbers:
                return True
            set_numbers.add(num)
        return False        
        print(set_numbers)