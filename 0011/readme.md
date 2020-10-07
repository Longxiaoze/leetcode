# 11. leetcode第十一题

**欢迎来到[leetcode第十一题](https://leetcode-cn.com/problems/container-with-most-water/)**

```markdown
   Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.
```

**翻译**：

```markdown
   给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
   说明：你不能倾斜容器，且 n 的值至少为 2。
```

**样例:**

**![question_11](https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/07/25/question_11.jpg)**

```markdown
输入：[1,8,6,2,5,4,8,3,7]
输出：49
```

## 7.1 python解决	

​        双指针问题，个人感觉还可以，依旧是官方题解，官方题解，最为致命，发现每次官方题解讲的都很不错**（在这里表示一下，个人主要是以学习为主，每次那道题自己也会想一想，但是大部分的题还是寻找最好的解决方法，然后把它弄懂了，由于时间精力有限，我找到差不多我个人认为比较好的就拿来给大家介绍学习了,一般都会附上原作者或者来源的，写博客也主要是为了记录一下自己的学习过程，如果你看了我的博客，欢迎一起探讨学习，大家一起努力进步。）**

**代码及注释如下[（官方题解）](https://leetcode-cn.com/problems/container-with-most-water/solution/sheng-zui-duo-shui-de-rong-qi-by-leetcode-solution/)：**

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans
```

**提交结果：**

- 56/56 cases passed (32 ms)
- Your runtime beats **86.77 %** of python submissions
- Your memory usage beats **5.02 %** of python submissions (12.4 MB)

**自己的体会：**

​	双指针解决很方便，这几天补一下国庆欠下的题，一天两道，补完以后再一天一道详解吧。后期继续完善。
