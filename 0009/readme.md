# 8. leetcode第九题

**欢迎来到[leetcode第九题](https://leetcode-cn.com/problems/palindrome-number/)**

```markdown
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
```

**翻译**：

```markdown
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
```

**样例:**

```markdown
输入: 121
输出: true

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。


```

## 8.1 python解决	

​        很简单的思路，由于之前已经做过求最长回文子串，所以这里直接就用最简单的思路：将数字转化为字符串，然后用python的字符串反转，对比反转前后是否相同即可。

**代码及注释如下：**

```python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)#转化为字符串
        if x[0] == "-":#判断是不是负数
            return False
        elif x == x[::-1]:#判断字符串反转前后是否相同
            return True
        else:
            return False
```

**提交结果：**

- 11509/11509 cases passed (124 ms)
- Your runtime beats **83.03 %** of python submissions
- Your memory usage beats **53.34 %** of python submissions (12.4 MB)

**自己的体会：**

​	没什么难的。。。。在做过之前那个求最长回文子串的题之后，感觉现在做简单题已经开始有点得心应手了哈哈。

​    明天国庆节+中秋节。。。国庆和中秋都在一起了，我还是单身。。。。。。。。。。。。。。。。。。。。
