# 21. leetcode第二十一题

**欢迎来到[leetcode第二十一题](https://leetcode-cn.com/problems/merge-two-sorted-lists/)**

```markdown
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.
```

![img](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

**翻译**：

```markdown
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
```

**样例:**

```markdown
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
```

## 21.1 python解决	

​        简单题，链表的基础操作，使用递归即可。

**代码及注释如下：**

```python
class Solution():
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
```

**提交结果：**

- 208/208 cases passed (16 ms)
- Your runtime beats 53.86% of python submissions
- Your memory usage beats 13.45% of python submissions (12.6 MB)

