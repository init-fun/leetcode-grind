class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # two pointer technique
        sptr = 0
        for i, ele in enumerate(nums):
            sptr = i + 1
            while sptr < len(nums):
                if nums[i] + nums[sptr] == target:
                    return [i,sptr]
                sptr += 1
