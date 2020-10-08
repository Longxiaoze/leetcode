# 12. leetcode第十二题

**欢迎来到[leetcode第十二题](https://leetcode-cn.com/problems/integer-to-roman/)**

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
Given an integer, convert it to a roman numeral.

```

**翻译**：

```markdown
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

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
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。
```

**样例:**

```markdown
输入: 3
输出: "III"

输入: 4
输出: "IV"

输入: 9
输出: "IX"

输入: 58
输出: "LVIII"
解释: L = 50, V = 5, III = 3.

输入: 1994
输出: "MCMXCIV"
解释: M = 1000, CM = 900, XC = 90, IV = 4.
```

## 12.1 python解决	

​        难度不大，主要需要了解一下罗马数字，罗马数字总是取最大的符号。具体可以搜索一下，解决方法还是看官方题解吧。

**代码及注释如下[官方题解1贪心算法](https://leetcode-cn.com/problems/integer-to-roman/solution/zheng-shu-zhuan-luo-ma-shu-zi-by-leetcode/)：**

```python
class Solution(object):
  def intToRoman(self, num):
      digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
      roman_digits = []#创建一个空列表来储存罗马数字字符
      # Loop through each symbol.
      for value, symbol in digits:
          # We don't want to continue looping if we're done.
          if num == 0: break#考虑到了数字为零的情况
          count, num = divmod(num, value)#divmod()为取整和取余数的函数，返回整数部分和余数部分
          # Append "count" copies of "symbol" to roman_digits.
          roman_digits.append(symbol * count)#将整数部分结合罗马数字字符扩充到roman_digits中
      return "".join(roman_digits)#拼接列表中字符串的方法，在每一个位置加入空字符，并拼接。
```

**代码及注释如下[官方题解1硬编码数字](https://leetcode-cn.com/problems/integer-to-roman/solution/zheng-shu-zhuan-luo-ma-shu-zi-by-leetcode/)：**

```python
class Solution(object):
    def intToRoman(self, num):
        thousands = ["", "M", "MM", "MMM"]#4000以内的所有情况
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]#百位数的所有情况
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]#十位数的所有情况
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]#个位数的所有情况
        return thousands[num // 1000] + hundreds[num % 1000 // 100] + tens[num % 100 // 10] + ones[num % 10]#分别计算千百十个位数的值，得到所对应的字符串情况拼接返回结果
```

**提交结果：**

**（1）**

- 3999/3999 cases passed (56 ms)
- Your runtime beats 74.47 % of python submissions
- Your memory usage beats 5.66 % of python submissions (12.4 MB)

**（2）**

- 3999/3999 cases passed (56 ms)
- Your runtime beats 84.91% % of python submissions
- Your memory usage beats 90.09 % of python submissions (12.3 MB)

**自己的体会：**

​	本题不难，看一遍就懂了，运行结果偏差很大，大家掌握就好了。
