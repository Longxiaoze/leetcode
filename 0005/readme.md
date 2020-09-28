# 5. leetcode第五题

**欢迎来到[leetcode第五题](https://leetcode-cn.com/problems/longest-palindromic-substring/)**

```markdown
  Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
```

**翻译**：

```markdown
   给定一个字符串s，要求它当中的最长回文子串。可以假设s串的长度最大是1000
```

**样例:**

```markdown
Input:"babad"
Output:"bab"
Note:"aba"is also a valid answer.

Input:"cbbd"
Output:"bb"
```

## 5.1 python解决	

​        首先看题目，回文子串可以看上述例子，就是从前和从后是一样的字符串。

​        最简单的思想，因为是回文字符串所以我们可以以每一个字符为中心分别向两边扩充，分为奇数字符串和偶数字符串分别讨论即可，时间复杂度为o(n^2)，不过还是老话，一般这样的时间复杂度都不是最优解。

​        让我们来看看**[算法导论](https://blog.csdn.net/hrn1216/article/details/51534607?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.channel_param)**中**[动态规划](https://blog.csdn.net/weixin_40673608/article/details/84262695#%E5%85%AC%E5%85%B1%E5%AD%90%E5%BA%8F%E5%88%97%E5%AE%9A%E4%B9%89%EF%BC%9A)**方法求解：如果判断回文子串，如果对于一个字符串，我们对它前后翻转一下，那么回文子串是不会变化的，我们对原字符串和反转字符串求它们的最长公共子序列，得到的结果就是我们要求的最长回文子串。不过时间复杂度依旧是o(n^2)，这么看来似乎双循环也还不错。

​        分析到了这里，也差不多了，下面我们直接参考大佬的想法进入正题，这题的最佳解法， *O*(*n*) 时间内获 取最大回文子串的曼彻斯特算法。在介绍我们的算法前，让我来介绍一个处理回文字符串的trick，对于回文字符串，会分成奇数和偶数来讨论，对于奇数我们通常比较好处理，那么对于偶数，我们可以在每一个空位置加上一个相同的字符，比如**aabb**变成**#a#a#b#b#**就从4个变成9个了，对于奇数，我们使用相同的方法，**aba**变成**#a#b#a#**，之前之后还是奇数，所以我们使用插入字符的操作，就可以减少一种讨论的情况。

​        下面介绍**马拉车算法**，也就是题解区所提到的**Manacher 算法**，依旧是膜拜大佬的一天，这个算法是专门处理最长回文子串问题的算法，在中心扩展的基础上，减少大部分扩展的时间，具体的原理可以看[链接](https://mp.weixin.qq.com/s?__biz=MzIzMTE1ODkyNQ==&mid=2649410225&idx=1&sn=ed045e8edc3c49a436a328e5f0f37a55&chksm=f0b60f53c7c18645b4c04a69ad314723cce94ed56994d6f963c2275a2db8d85f973f15f508e4&mpshare=1&scene=23&srcid=1001JCsBlpxgUWjgixasChNQ#rd)，这是我看了很多帖子觉得讲的最详细的一个，好评好评，这里我就不多介绍了，这个帖子讲的很好。

**代码及注释如下（[来自leetcode官方题解](https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zui-chang-hui-wen-zi-chuan-by-leetcode-solution/)）：**

```python
class Solution:
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 2) // 2

    def longestPalindrome(self, s):
        end, start = -1, 0
        s = '#' + '#'.join(list(s)) + '#'
        arm_len = []
        right = -1
        j = -1
        for i in range(len(s)):
            if right >= i:
                i_sym = 2 * j - i
                min_arm_len = min(arm_len[i_sym], right - i)
                cur_arm_len = self.expand(s, i - min_arm_len, i + min_arm_len)
            else:
                cur_arm_len = self.expand(s, i, i)
            arm_len.append(cur_arm_len)
            if i + cur_arm_len > right:
                j = i
                right = i + cur_arm_len
            if 2 * cur_arm_len + 1 > end - start:
                start = i - cur_arm_len
                end = i + cur_arm_len
        return s[start+1:end+1:2]

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zui-chang-hui-wen-zi-chuan-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

**提交结果：**

- 103/103 cases passed (88 ms)
- Your runtime beats **94.59 %** of python submissions
- Your memory usage beats **48.99 %** of python submissions (12.7 MB)

**自己的体会：**

​	本题虽然官方标的是中等难度，但是事实上很难，如果没有学过的话，是很难想到马拉车算法的，这道题作者也是前前后后看了很长时间才弄明白的，希望大家细品一下，最后会有一种豁然开朗的感觉，哈哈，又是膜拜大佬的一天。。。。，依旧不写c++代码了，有兴趣的同学可以看一下官方题解的网站给的代码哈。

