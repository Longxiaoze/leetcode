class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        j = 0
        for i in xrange(len(nums)):
            if nums[i]!=nums[j]:
                j += 1
                nums[j] = nums[i]
        return j+1

# 作者：wang_ni_ma
# 链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/solution/duo-tu-yan-shi-26shan-chu-pai-xu-shu-zu-zhong-de-z/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
