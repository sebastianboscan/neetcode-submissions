class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. list to hashmap
        nums_hashmap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in nums_hashmap:
                return [nums_hashmap[diff], i]
            nums_hashmap[n] = i
        return















        # # x + y = target hence y = target - x
        # # 1. Convert list into hashmap
        # nums_hashmap = {}
        # for i in range(len(nums)):
        #     nums_hashmap[nums[i]] = nums_hashmap.get(nums[i], i)

        # # 2. Then we calculate for y
        # for i in range(len(nums)):
        #     y = target - nums[i]
            
        #     # if i == nums_hashmap.get(y):
        #     #     continue

        #     # 3. Lastly we check if y is in the hashmap as a key
        #     if y in nums_hashmap:
        #         return [i, nums_hashmap.get(y)]

