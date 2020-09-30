#
# @lc app=leetcode.cn id=9 lang=python
#
# [9] 回文数
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        if x[0] == "-":
            return False
        elif x == x[::-1]:
            return True
        else:
            return False
            
# @lc code=end

