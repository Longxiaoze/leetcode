# 17. leetcode第十七题

**欢迎来到[leetcode第十七题](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number)**

```markdown
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
```

**翻译**：

```markdown
   给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
   给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
```

![17_telephone_keypad](https://assets.leetcode-cn.com/aliyun-lc-upload/original_images/17_telephone_keypad.png)

**样例:**

```markdown
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序

Constraints:
  0 <= digits.length <= 4
  digits[i] is a digit in the range ['2', '9'].
```

## 17.1 python解决	

**代码及注释如下[官方题解](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/solution/dian-hua-hao-ma-de-zi-mu-zu-he-by-leetcode-solutio/)：**

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list()
        
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index: int):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        combination = list()
        combinations = list()
        backtrack(0)
        return combinations
 '''  
 #官方给的精简版，看一下就行了，个人觉得代码还是可读性高一点比较好
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list()
        
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        groups = (phoneMap[digit] for digit in digits)
        return ["".join(combination) for combination in itertools.product(*groups)]
'''   
```
