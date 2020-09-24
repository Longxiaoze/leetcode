# 3. leetcode第三题

**欢迎来到[leetcode第三题](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)**

```markdown
  Given a string, find the length of the longest substring without repeating characters.
```

**翻译**：

```markdown
   给定一个字符串，要求返回不包含重复字符的最长子串的长度。
```

**样例:**

```markdown
Input:"abcabcbb"
Output:3
Explanation:The answer is "abc",with the length of 3.
Input:"bbbbb"
Output:1
Explanation:The answer is "b", with the length of 1.
```

## 3.1 python解决	

​        最简单的思路依旧是枚举，我们可以遍历出这个字符串里面的所有的子串，然后判断这些子串当中有没有出现重复的元素，如果没有重复元素我们就更新答案，例如“abb”的子串为“a”，“b”，“c”，“ab”，“bb”，“abb”，然后分别判断这些子串里面有没有重复的字符，不过随便想想，显然时间复杂度O(n^3)太大了。

​        上述的时间复杂度显然我们是没办法接受的，所以我们进行第一个优化：事实上我们没必要枚举所有的子串举个例子来说吧，例如字符串“abcabcdbbb”，我们从第一位开始，直到第四位才出现a，所以显然“abc”是目前为止最长的字符串长度为3，然后我们从第四位开始，“abcd”之后才出现a，所以到目前为止最长的长度是4，然后是“b”，长度为1，以此类推，这样的时间复杂度是O(n^2)，其实到这里基本就是我们思维的极限了，不过一般来说这样的时间复杂度基本都不是最优解。让我们继续优化。

​        在这里我们先看一下[尺取法](https://blog.csdn.net/kingmax54212008/article/details/103531887?utm_medium=distribute.pc_relevant.none-task-blog-title-2&spm=1001.2101.3001.4242)，在一些课本当中也被称为two pointer算法或者是两指针算法，也叫滑动窗口算法。这个的时间复杂度可以减少到O(n)。

**代码及注释如下（继续膜拜大佬）：**

```python
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0#start为起始位置，maxLength为最大无重复字符的字符串长度
        usedChar = {}#定义一个字典用来储存判断
        #开始滑动窗口：这个循环主要是先从start开始扩充滑动窗口的大小，并将窗口内的每一个元素添加到字典usedChar中，当窗口准备扩充的元素已经存在于字典usedChar中时，start往后挪一位，依次遍历一遍即可得到maxLength
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
            #后面判断是深邃，需要细品，不加后面的限制条件的话，判断“tmmzuxt”会报错
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            usedChar[s[i]] = i
        return maxLength
```

**流程实例化演示（这里等于不是赋值，就是演示用）**

```markdown
num = [2,7,11,15],tar = 9
dic={}
i = 0时：判断num[0] = 2不在字典中，则将9-2:0添加到字典中
dic={7:0}
i = 1时：判断num[1] = 7,在字典中，则返回dic[num[i]] = dic[num[1]] = dic[7] = 0和i = 1。
函数结束。
```

**提交结果：**

- 987/987 cases passed (48 ms)
- Your runtime beats **89.24 %** of python3 submissions
- Your memory usage beats **33.66 %** of python3 submissions (13.4 MB)

**自己的体会：**

​	本题依旧膜拜大佬算法，不过滑动窗口在程序中用的挺多的，我在后面也会总结所有可以用到滑动窗口的题，做到再返回头看吧。

## 3.2 c++解决

​	  依旧膜拜大佬，来自vscode最多投票数。

```c++
class Solution {
public:

int lengthOfLongestSubstring(string s) {
        vector<int> dict(256, -1);
        int maxLen = 0, start = -1;
        for (int i = 0; i != s.length(); i++) {
            if (dict[s[i]] > start)
                start = dict[s[i]];
            dict[s[i]] = i;
            maxLen = max(maxLen, i - start);
        }
        return maxLen;
    }
};
```

**提交结果：**

- 987/987 cases passed (8 ms)
- Your runtime beats **98.14 %** of cpp submissions
- Your memory usage beats **65.78 %** of cpp submissions (8.3 MB)

## 1.3总结

​	**首先我只是想分享我在学习中的一些想法和学习过程，如有侵权请联系我，保证侵权必删。**不多说，又是膜拜大佬的一天，好奇大佬的大脑构成，也可能确实自己太菜了，哈哈。。。。。。。
