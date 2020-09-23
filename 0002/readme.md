# 2. leetcode第二题

**欢迎来到[leetcode第二题](https://leetcode-cn.com/problems/add-two-numbers/)**

```markdown
  You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
  You may assume the two numbers do not contain any leading zero, except the number 0 itself.
```

**翻译**：

```markdown
   给定两个非空的链表，代表两个非负整数。这两个整数都是倒叙存储，要求返回一个链表， 表示这两个整数的和。
```

**样例:**

```markdown
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4) Output: 7 -> 0 -> 8 Explanation: 342 + 465 = 807.
```

## 2.1 python解决	

这道题是一个很普通的链表题，需要注意的点如下

1. 因为不是数组，所以我们无法拿到链表的长度。会出现两个链表长度不一致的情况 
2. 返回结果是一个链表，需要我们自己手动创建返回
3. 计算产生的进位处理需要处理的代码

**代码及注释如下：（参考[xiao-lin-20](https://leetcode-cn.com/problems/add-two-numbers/solution/cjie-ti-de-wan-zheng-dai-ma-bao-gua-sheng-cheng-ce/))**

```python
class Solution:
    def addTwoNumbers(self, l1, l2):
        prenode = ListNode(0)#新建一个链表
        lastnode = prenode#备份链表的起始地址
        val = 0#设定初值
        while val or l1 or l2:#判断是否到尾节点
            #这里详细解释一下：divmod()为取整和求余函数，在本题中，divmod(x,10)为取x的十位数的数字和x个位数的数字。
            #(l1.val if l1 else 0)为python的if函数缩减版，意思是如果l1不为空，返回l1.val，否则返回0。
            #所以这条语句的意思是判断每一个位置上是否有值，无值用0，将每个位置求和，将进位传给val变量，将个位数传给cur。
            val, cur = divmod(val + (l1.val if l1 else 0) + (l2.val if l2 else 0), 10)
            lastnode.next = ListNode(cur)#将个位数的值赋值给新建的链表结点
            lastnode = lastnode.next#python模拟移动指针，不明白的可以去学一下链表的相关知识。
            l1 = l1.next if l1 else None#移动l1指针
            l2 = l2.next if l2 else None#移动l2指针
        return prenode.next#返回起始链表的地址
```

**trick（不容易注意到的点）：**

​	本题无trick，主要是链表的操作。

**提交结果：**

- 1563/1563 cases passed (72 ms)
- Your runtime beats **62.22 %** of python submissions
- Your memory usage beats **33.65 %** of python submissions (12.6 MB)

**自己的体会：**

​	本题我自己也写了一下，不过代码没有这个作者写的这么清楚简洁，所以分享这个作者的代码了，不过注释是我自己加的，以学习为主，这道题也不太难，击败也没有很多，但是作者代码看着就很舒服也很明白。

## 2.2 c++解决

​	上述已经介绍了很多东西了，这里只放这个作者的c++代码就不多解释了。

```c++
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // 使用prenode而不需要单独考虑头节点，以简化代码
        ListNode *prenode = new ListNode(0);
        ListNode *lastnode = prenode;
        int val = 0;
        while(val || l1 || l2) {
            val = val + (l1?l1->val:0) + (l2?l2->val:0);
            lastnode->next = new ListNode(val % 10);
            lastnode = lastnode->next;
            val = val / 10;
            l1 = l1?l1->next:nullptr;
            l2 = l2?l2->next:nullptr;
        }
        ListNode *res = prenode->next;
        delete prenode; // 释放额外引入的prenode
        return res;
    }
};
```

**提交结果：**

- 1563/1563 cases passed (36 ms)
- Your runtime beats 57.79 % of cpp submissions
- Your memory usage beats 62.56 % of cpp submissions (9.1 MB)

**自己的体会：**

​    我突然发现，这个提交的运行时间和内存好像也挺随机的。。。。。。。

## 1.3总结

​    没什么想说的，今天的不难，就当练手了吧。。。
