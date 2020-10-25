class Solution(object):
    def removeElement(self, nums, val):
        if nums!=None:
            for i in range(nums.count(val)):
                nums.remove(val)
            return len(nums)
        else:
            return len(nums)
