# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        n_node = ListNode(0)
        n_node.next = head 
        
        #step1: 快指针先走n步
        slow, fast = n_node, n_node
        for _ in range(n):
            fast = fast.next 

        #step2: 快慢指针同时走，直到fast指针到达尾部节点，此时slow到达倒数第N个节点的前一个节点
        while fast and fast.next:
            slow, fast = slow.next, fast.next 
        
        #step3: 删除节点，并重新连接
        slow.next = slow.next.next 
        return n_node.next 

