# 6. leetcode第六题

**欢迎来到[leetcode第六题](https://leetcode-cn.com/problems/zigzag-conversion/)**

```markdown
  
   The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
```

**翻译**：

```markdown
   给定一个字符串，将它变成蛇形输出。这个蛇形的概念比较抽象，我们需要结合样例才能理解。
```

**样例:**

```markdown
给定字符串：PAYPALISHIRING和行数3
蛇形输出：
P   A   H   N
A P L S I I G
Y   I   R
最终输出：PAHNAPLSIIGYIR
```

## 6.1 python解决	

​        虽然LeetCode上给这题的难度是Medium，但实际上它还是比较简单的。

​        这题会告诉我们字符串以及行数，我们需要根据用到的行数，将字符串排成蛇形。

​        这个蛇形的排列也很简单，因为我们只要输出最后的按行连接的结果。所以我们完全可以忽略列的位置信息，只用关注摆放的行就好了。因为行数是有限的，对于每一行，我们可以用 一个字符串记录当前行目前为止摆放的字符串，最后按照行的顺序将所有行的结果连接到一 起就好了。通过观察，我们很容易发现，摆放的行是有周期规律的。下面直接看代码吧。

**代码及注释如下：**

```python
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        #判断如果行数等于一或者给的行数大于字符串本身的长度，就直接返回原字符串，因为读出来和原字符串相同
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        #主要思路如下：创建的L内部的元素数量和给定的行数相等，判断原字符串的每个元素，分别加入到第一个位置，第二个位置，第三个位置，第二个位置后，第一个位置后，第二个位置后。。。。以此往后，最终返回拼接好的字符串。
        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)
```

**trick（不容易注意到的点）：**

​	本题无trick，很简单，最开始的if语句可以减少一些时间。

**提交结果：**

- 1158/1158 cases passed (40 ms)
- Your runtime beats **97.07 %** of python submissions
- Your memory usage beats **90.91 %** of python submissions (12.3 MB)

**自己的体会：**

​	本题很简单，看一下就好了，自己过一遍代码就可以看懂。有点简单，就不写c++代码了，想写的同学是这些一下就好了，挺简单的。
