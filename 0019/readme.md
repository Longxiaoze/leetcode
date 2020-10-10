# 19. leetcode第十九题

**欢迎来到[leetcode第十九题](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/)**

```markdown
Given the head of a linked list, remove the nth node from the end of the list and return its head.
```

**翻译**：

```markdown
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
```

**样例:**

```markdown
给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
```

## 19.1 python解决	

​        中等难度，但是实际不难，链表的一个操作，下面介绍一下思路：

​		1.两次遍历算法：事实上这个问题可以容易地简化成另一个问题：删除从列表开头数起的第 (L - n + 1)个结点，其中 L 是列表的长度。只要我们找到列表的长度 L，这个问题就很容易解决。遍历两遍，第一遍求长度，第二遍求节点位置，然后即可解决本题。

​		2.一次遍历算法：那么我们思考有没有只需要遍历一遍就可以找到节点位置呢？其实这个思想很巧妙，我们要求倒数n个结点，那么我们可以用两个指针，他们之间的长度为n，那么，当尾指针到最后一个结点位置时，头指针就是倒数个结点的位置。参考讨论区，把这种方法叫做快慢指针。

**代码及注释如下：**

```python
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

```

**提交结果：**

- 208/208 cases passed (28 ms)
- Your runtime beats 86.59 % of python submissions
- Your memory usage beats 23.44 % of python submissions (12.5 MB)

**自己的体会：**

本题是一种很巧妙的思想，但是仔细思考一下似乎之前很多题都用了这种两个指针的方法。
