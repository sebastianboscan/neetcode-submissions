class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()

        for n in nums:
            if n in hashSet:
                return True
            hashSet.add(n)
        return False
        
        # length = len(nums)
        # nums.sort()

        # for i in range(len(nums) - 1):
        #     if (nums[i] == nums[i+1]):
        #         return True
        # return False
        