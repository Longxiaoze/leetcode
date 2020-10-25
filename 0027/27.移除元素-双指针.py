class Solution(object):
    def removeElement(self, nums, val):
        if not nums:
            return 0
        i = 0
        n = len(nums)
        while i<n:
            if nums[i]==val:
                nums[i] = nums[n-1]
                n -= 1
            else:
                i += 1
        return i
'''
作者：wang_ni_ma
链接：https://leetcode-cn.com/problems/remove-element/solution/san-chong-shi-xian-tu-jie-27yi-chu-yuan-su-by-wang/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''
