# 24. leetcode第二十四题

**欢迎来到[leetcode第二十四题](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)**

```markdown
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes. Only nodes itself may be changed.
```

**翻译**：

```markdown
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

提示：
链表中节点的数目在范围 [0, 100] 内
0 <= Node.val <= 100
```

![swap_ex1](https://assets.leetcode.com/uploads/2020/10/03/swap_ex1.jpg)

**样例:**

```markdown
输入：head = [1,2,3,4]
输出：[2,1,4,3]
```

## 24.1 python解决	

​        不难，看[官方题解](https://leetcode-cn.com/problems/swap-nodes-in-pairs/solution/liang-liang-jiao-huan-lian-biao-zhong-de-jie-di-91/)吧...

**代码及注释如下(官方题解迭代法)：**

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        dummyHead = ListNode(0)
        dummyHead.next = head
        temp = dummyHead
        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            temp = node1
        return dummyHead.next
```

**提交结果：**

- 55/55 cases passed (16 ms)
- Your runtime beats 88.94% of python submissions
- Your memory usage beats 5.12% of python submissions (13.2 MB)

**自己的体会：**

前几天结的课比较多，从今天开始继续更新哈
