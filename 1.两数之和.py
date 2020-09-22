# -*- coding: utf-8 -*-
#
# @lc app=leetcode.cn id=1 lang=python3
#

# [1] 
#

# @lc code=start
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dic = {}
        for i in range(len(num)):
            if num[i] not in dic:
                dic[target - num[i]] = i
            else:
                return dic[num[i]], i

        return -1, -1

# @lc code=end

