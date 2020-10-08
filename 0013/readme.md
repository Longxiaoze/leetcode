# 13. leetcode第十三题

**欢迎来到[leetcode第十三题](https://leetcode-cn.com/problems/roman-to-integer/)**

```markdown
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
```

**翻译**：

```markdown
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
```

**样例:**

```markdown
输入: "III"
输出: 3

输入: "IV"
输出: 4

输入: "IX"
输出: 9

输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.

输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.

注意：
题目所给测试用例皆符合罗马数字书写规则，不会出现跨位等情况。
IC 和 IM 这样的例子并不符合题目要求，49 应该写作 XLIX，999 应该写作 CMXCIX 。
```

## 13.1 python解决

​        本题不难，还是需要注意罗马数字的特点，只有在遇到特殊情况时，两个字符中左边的字符小于右边的字符，且等于右边的字符代表的数减左边字符代表的数。 比如 CM 等于 1000 - 1001000−100，XC 等于 100 - 10100−10...

**代码及注释如下[（参考）](https://leetcode-cn.com/problems/roman-to-integer/solution/qing-xi-tu-jie-python3-by-ml-zimingmeng/)：**

```python
class Solution:
    def romanToInt(self, s):
        Roman2Int = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}#构建一个字典用来保存转换方式，数据结构是哈希表，python中用字典来实现，也可以用其他的像上一道题的列表或者列表+元组来实现。
        Int = 0
        n = len(s)

        for index in range(n - 1):#遍历n-1次（最后一位不需要比较之后的位置）
            if Roman2Int[s[index]] < Roman2Int[s[index + 1]]:#判断当前罗马数字字符和后面位置罗马字符对应的数字的大小关系
                Int -= Roman2Int[s[index]]
            else:
                Int += Roman2Int[s[index]]

        return Int + Roman2Int[s[-1]]#最后把不需要比较的最后一位加上

'''
作者：z1m
链接：https://leetcode-cn.com/problems/roman-to-integer/solution/qing-xi-tu-jie-python3-by-ml-zimingmeng/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''
```

**trick（不容易注意到的点）：**

主要是罗马数字本身的一些注意事项

**提交结果：**

- 3999/3999 cases passed (28 ms)
- Your runtime beats 91.63 % of python submissions
- Your memory usage beats 91.63 % of python submissions (12.5 MB)

**自己的体会：**

​	对比上一题看一下就好了，没什么难的。明天继续加油。
