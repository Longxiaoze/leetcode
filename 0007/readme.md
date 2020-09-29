# 7. leetcode第七题

**欢迎来到[leetcode第七题](https://leetcode-cn.com/problems/reverse-integer/)**

```markdown
Given a 32-bit signed integer, reverse digits of an integer.
**Note:**
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
```

**翻译**：

```markdown
   给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
**注意:**
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
```

**样例:**

```markdown
输入: 123
输出: 321
```

## 7.1 python解决	

​        又是一道简单的题目放松，下面直接看代码吧。给大家找了一个很简短的代码。

**代码及注释如下：**

```python
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = cmp(x, 0)#cmp(x,y) 函数用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。
        r = int(str(s*x)[::-1])#变成字符串类型翻转
        return s*r * (r < 2**31)#这里直接判断note中的范围了，如果超范围的话(r < 2**31)就会成为0，符合题目要求


```

**trick（不容易注意到的点）：**

第一个陷阱是负号的问题，如果我们直接将数字转换成字符串，再反向输出字符串就会遇见 这个问题。因为负数的翻转是忽略符号的，也就是说我们要把符号单独拿出来，翻转之后再 加回去。就比如样例-123翻转之后的结果是-321。

第二个陷阱是前导零的问题，合法的数字当中是不允许0开头的，但是允许0结尾。也就是说 如果存在一个0结尾的数，我们翻转了就会出现0开头，但是0翻转之后的结果还是0。

前面两个陷阱还算是比较明显，我们稍稍注意就能发现，第三个陷阱藏得就比较深了，一不 小心很容易中招。这个陷阱是int的取值范围。题目当中限定了是32位的int类型的数字，对 于Python来说不存在int32和int64的差别，只要是数字类型都能存的下。但是对于C++和 Java这样的语言来说，int32的类型是固定的，就是 $-2^{31}~2^{31}-1$ 。大约是21亿左右， 这就带来一个问题，一个数在翻转之前是合法的，但是翻转之后的结果就超过界限了。

**提交结果：**

- 1032/1032 cases passed (28 ms)
- Your runtime beats 75.35 % of python submissions
- Your memory usage beats 61.8 % of python submissions (12.4 MB)

**自己的体会：**

​	本题很简单，看一下就好了，自己过一遍代码就可以看懂。有点简单，就不写c++代码了，想写的同学是这些一下就好了，挺简单的。由于很简单，提交结果每次提交会变化，这道题不用注意结果，能跑通就好了
