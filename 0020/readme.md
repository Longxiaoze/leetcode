# 20. leetcode第二十题

**欢迎来到[leetcode第二十题](https://leetcode-cn.com/problems/valid-parentheses/)**

```markdown
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
```

**翻译**：

```markdown
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
```

**样例:**

```markdown
输入: "()"
输出: true

输入: "()[]{}"
输出: true

输入: "(]"
输出: false

输入: "([)]"
输出: false

输入: "{[]}"
输出: true
```

## 20.1 python解决	

​        简单题，用堆栈的数据结构，先入先出，可以很轻松解决，如果这个题有问题的话，那么说明你需要回去补一下数据结构的知识了。

**代码及注释如下：**

```python
class Solution():
    def isValid(self, s):
        if len(s) % 2 == 1:#首先判断是不是单数字符串
            return False
        
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []
        for ch in s:#遍历字符串
            if ch in pairs:#遇到后括号执行if
                if not stack or stack[-1] != pairs[ch]:
                #如果这个时候stack为空，说明第一个遇到的是后括号，不符合题意，返回false；如果stack中最后一个与这个后括号对应的前括号不相同，说明顺序有问题，不符合题意，返回false。
                    return False
                stack.pop()#如果这个后括号满足题意，把之前添加的这个后括号对应的前括号从最后一位删掉
            else:
                stack.append(ch)#每次遍历遇到前括号的时候加在stack的最后面
        
        return not stack
```

**提交结果：**

- 91/91 cases passed (16 ms)
- Your runtime beats 93.71% of python submissions
- Your memory usage beats 43.21% of python submissions (12.6 MB)

**自己的体会：**

没什么难的，很简单的一道题，不知不觉已经做了20个了，继续加油。。。。今天的这个思想很像第一道题，可以回去看一下复习一下。
