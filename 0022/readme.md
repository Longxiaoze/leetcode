# 22. leetcode第二十二题

**欢迎来到[leetcode第二十二题](https://leetcode-cn.com/problems/generate-parentheses/)**

```markdown
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
```

**翻译**：

```markdown
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
```

**样例:**

```markdown
输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
```

## 22.1 python解决	

​        需要注意这道题要求是有效括号，大家可以看一下[官方题解](https://leetcode-cn.com/problems/generate-parentheses/solution/gua-hao-sheng-cheng-by-leetcode-solution/)，主要可以研究一下时间复杂度和空间复杂度怎么来的。

**代码及注释如下：**

```python
class Solution:
    def generateParenthesis(self,n):
        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans
```

**提交结果：**

- 8/8 cases passed (16 ms)
- Your runtime beats 91.01% of python submissions
- Your memory usage beats 69.06% of python submissions (12.5 MB)

**自己的体会：**

自己看一下官方题解吧，讲得很清晰，自己还思考了一下插值的方法，就是无论怎么排列，必然有一对()是连着的，然后通过n的个数往两边插值，不过今天作业多，等闲下来再好好思考一下这个思路吧。
