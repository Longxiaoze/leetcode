# 10. leetcode第十题

**欢迎来到[leetcode第十题](https://leetcode-cn.com/problems/regular-expression-matching/)**

```markdown
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).
```

**翻译**：

```markdown
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素

所谓匹配，是要涵盖整个字符串s的，而不是部分字符串。

说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
```

**样例:**

```markdown
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
```

## 10.1 python解决	

​        这道题属于典型的那种拿到题直接做的问题--动手实现一个简单的正则匹配算法。不过为了降低难度，这里需要匹配的只有两个特殊符号，一个符号是'.'，表示可以匹配任意的单个字 符。还有一个特殊符号是'*'，它表示它前面的符号可以是任意个，可以是0个。

​        题目要求是输入一个母串和一个模式串，请问是否能够达成匹配。这题要求的是完全匹配，而不是包含匹配。也就是说s串匹配完 p 串之后不能有剩余，比如刚好完全匹配才行。所以，题目中的匹配是一个「逐步匹配」的过程：我们每次从字符串 p 中取出一个字符或者「字符 + 星号」的组合，并在 s 中进行匹配。对于 p 中一个字符而言，它只能在 s 中匹配一个字符，匹配的方法具有唯一性；而对于 p 中字符 + 星号的组合而言，它可以在 s 中匹配任意自然数个字符，并不具有唯一性。（官方题解）

​       介绍一下动态规划吧，[官方题解](https://leetcode-cn.com/problems/regular-expression-matching/solution/zheng-ze-biao-da-shi-pi-pei-by-leetcode-solution/)介绍的很不错，大家可以看一下，下面介绍一下我的理解：

**代码及注释如下[（官方题解）](https://leetcode-cn.com/problems/regular-expression-matching/solution/zheng-ze-biao-da-shi-pi-pei-by-leetcode-solution/)：**

```python
class Solution:
    def isMatch(self, s, p):
        m, n = len(s), len(p)

        def matches(i, j):
        #匹配i，j是否相同
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]

```

**[官方题解评论区用户的例子详解：](https://leetcode-cn.com/problems/regular-expression-matching/solution/zheng-ze-biao-da-shi-pi-pei-by-leetcode-solution/)**用户：[newhar](https://leetcode-cn.com/u/newhar/)

```
以一个例子详解动态规划转移方程：
S = abbbbc
P = ab*d*c
1. 当 i, j 指向的字符均为字母（或 '.' 可以看成一个特殊的字母）时，
   只需判断对应位置的字符即可，
   若相等，只需判断 i,j 之前的字符串是否匹配即可，转化为子问题 f[i-1][j-1].
   若不等，则当前的 i,j 肯定不能匹配，为 false.
   
       f[i-1][j-1]   i
            |        |
   S [a  b  b  b  b][c] 
   
   P [a  b  *  d  *][c]
                     |
                     j
   

2. 如果当前 j 指向的字符为 '*'，则不妨把类似 'a*', 'b*' 等的当成整体看待。
   看下面的例子

            i
            |
   S  a  b [b] b  b  c  
   
   P  a [b  *] d  *  c
            |
            j
   
   注意到当 'b*' 匹配完 'b' 之后，它仍然可以继续发挥作用。
   因此可以只把 i 前移一位，而不丢弃 'b*', 转化为子问题 f[i-1][j]:
   
         i
         | <--
   S  a [b] b  b  b  c  
   
   P  a [b  *] d  *  c
            |
            j
   
   另外，也可以选择让 'b*' 不再进行匹配，把 'b*' 丢弃。
   转化为子问题 f[i][j-2]:

            i
            |
   S  a  b [b] b  b  c  
    
   P [a] b  *  d  *  c
      |
      j <--

3. 冗余的状态转移不会影响答案，
   因为当 j 指向 'b*' 中的 'b' 时, 这个状态对于答案是没有用的,
   原因参见评论区 稳中求胜 的解释, 当 j 指向 '*' 时,
   dp[i][j]只与dp[i][j-2]有关, 跳过了 dp[i][j-1].
```

**提交结果：**

- 449/449 cases passed (64 ms)
- Your runtime beats **56.43 %** of python submissions
- Your memory usage beats **44.52 %** of python submissions (12.5 MB)

**自己的体会：**

​	难题，第一次接触动态规划，找了一些博客大佬写的教程，最后结合代码理解了。。。浏览官方题解的评论有人说一杯酒，一包烟，一道困难题写一天~，真是。。。太真实了，一个人，一电脑，一茶一题搞一天，哈哈，这几天补一下国庆的进度，写的可能有些简略，后期整理的时候再补一些内容吧。继续加油学习！！！
