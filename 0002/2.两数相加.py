#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None



class Solution:
    def addTwoNumbers(self, l1, l2):
        prenode = ListNode(0)
        lastnode = prenode
        val = 0
        while val or l1 or l2:
            val, cur = divmod(val + (l1.val if l1 else 0) + (l2.val if l2 else 0), 10)
            lastnode.next = ListNode(cur)
            lastnode = lastnode.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return prenode.next


# def generateList(l: list) -> ListNode:
#     prenode = ListNode(0)
#     lastnode = prenode
#     for val in l:
#         lastnode.next = ListNode(val)
#         lastnode = lastnode.next
#     return prenode.next

# def printList(l: ListNode):
#     while l:
#         print("%d, " %(l.val), end = '')
#         l = l.next
#     print('')

# if __name__ == "__main__":
#     l1 = generateList([1, 5, 8])
#     l2 = generateList([9, 1, 2, 9])
#     printList(l1)
#     printList(l2)
#     s = Solution()
#     sum = s.addTwoNumbers(l1, l2)
#     printList(sum)
    

# 作者：xiao-lin-20
# 链接：https://leetcode-cn.com/problems/add-two-numbers/solution/cjie-ti-de-wan-zheng-dai-ma-bao-gua-sheng-cheng-ce/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# @lc code=end

