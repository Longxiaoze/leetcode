# 14. leetcode第十四题

**欢迎来到[leetcode第十四题](https://leetcode-cn.com/problems/longest-common-prefix/)**

```markdown
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
```

**翻译**：

```markdown
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
```

**样例:**

```markdown
输入: ["flower","flow","flight"]
输出: "fl"

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。
```

## 14.1 python解决	

​        简单题，今天三节课，下午回来睡了一觉，起来没啥事，我补一下之前的进度吧，速度补一下，明天开始详细写思考过程和思路，后期有时间补一下这几个题，我看的还是官方题解官方题解

**代码及注释如下[官方题解-1横向扫描](https://leetcode-cn.com/problems/longest-common-prefix/solution/zui-chang-gong-gong-qian-zhui-by-leetcode-solution/)：**

```python
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break
        
        return prefix

    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]

```

**代码及注释如下[官方题解-2纵向扫描](https://leetcode-cn.com/problems/longest-common-prefix/solution/zui-chang-gong-gong-qian-zhui-by-leetcode-solution/)：**

```python
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
                return strs[0][:i]
        
        return strs[0]

```

**代码及注释如下[官方题解-3分治](https://leetcode-cn.com/problems/longest-common-prefix/solution/zui-chang-gong-gong-qian-zhui-by-leetcode-solution/)：**

```python
class Solution:
    def longestCommonPrefix(self, strs):
        def lcp(start, end):
            if start == end:
                return strs[start]

            mid = (start + end) // 2
            lcpLeft, lcpRight = lcp(start, mid), lcp(mid + 1, end)
            minLength = min(len(lcpLeft), len(lcpRight))
            for i in range(minLength):
                if lcpLeft[i] != lcpRight[i]:
                    return lcpLeft[:i]

            return lcpLeft[:minLength]

        return "" if not strs else lcp(0, len(strs) - 1)

```

**代码及注释如下[官方题解-4二分查找](https://leetcode-cn.com/problems/longest-common-prefix/solution/zui-chang-gong-gong-qian-zhui-by-leetcode-solution/)：**

```python
class Solution:
    def longestCommonPrefix(self, strs):
        def isCommonPrefix(length):
            str0, count = strs[0][:length], len(strs)
            return all(strs[i][:length] == str0 for i in range(1, count))

        if not strs:
            return ""

        minLength = min(len(s) for s in strs)
        low, high = 0, minLength
        while low < high:
            mid = (high - low + 1) // 2 + low
            if isCommonPrefix(mid):
                low = mid
            else:
                high = mid - 1

        return strs[0][:low]

```

**自己的体会：**

​	不写用时了，过了一遍代码，然后把代码提交了一下没啥问题，我还是这样速速的补一下吧，正好今天没啥事情，明天开始就写详细过程了，不然拖的时间太久了，给大家一个建议，有啥东西或者计划欠下的时候，一定要早点补完，然后继续按计划走，哪怕补的很粗糙，这还是我之前看樊登读书的时候学到的方法，原意是你计划锻炼身体一年，不管多忙，哪怕你忙的时候走路都个十几分钟都可以算作锻炼，有的时候做了就已经很不错了，做的完美那都是极极极少数人才干的事情。。。。下几道题的体会我就都写在这里了，速速的补完，明天又是新的一天，很期待，哈哈，加油加油！！！
