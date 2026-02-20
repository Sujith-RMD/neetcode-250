#Boyer–Moore Approach

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        r = nums[0]
        count = 1
        for i in nums[1:]:
            if r == i:
                count += 1
            else:
                count -= 1
            if count == 0:
                r = i
                count = 1
        return r