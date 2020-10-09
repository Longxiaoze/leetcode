# 18. leetcode第十八题

**欢迎来到[leetcode第十八题](https://leetcode-cn.com/problems/4sum)**

```markdown
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.
```

**翻译**：

```markdown
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：
答案中不可以包含重复的四元组。
```

**样例:**

```markdown
给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
```

## 18.1 python解决	

​        好了，之前欠下的进度昨天补完了，今天继续详解思路和代码，今天的题目是四数之和，可以将之前的[第一题两数之和](https://leetcode-cn.com/problems/add-two-numbers/)（[题解](https://github.com/Longxiaoze/leetcode/tree/master/0001)）和[第十五题三数之和](https://leetcode-cn.com/problems/3sum)（[题解](https://github.com/Longxiaoze/leetcode/tree/master/00015)）放在一起看一下，其实这个题是这上周的三数之和的进化版，说实话挺没意思的，不过我们还是把这些题放在一起总结一遍吧。

​		两数之和思路：使用map/字典

​		三数之和思路：排序+双指针，思路也不难，先把给定数组排个序，然后使用双指针，先枚举一个数，然后通过双指针去寻找另外两个数字。这里也解释了为什么我们要先排序，因为不排序的话我们很难去决定双指针的移动策略，如果排序的话就可以按大小进行左右移动了。这里需要注意一下我们要避免重复结果，所以移动的时候就需要判断指针移动前后元素是否相同。将之前枚举的数字枚举完一遍就可以得到结果了。时间复杂度o(n^2)

​		四数之和思路：有了三数之和的经验之后，我们很容易就可以想到利用三数之和的代码，只不过多加一层for循环罢了，比如双重循环分别枚举排序后的前两个数字，然后用双指针寻找剩下的两个数字。时间复杂度o(n^3)，看官方代码吧，最多也就做到这里了。

**代码及注释如下[官方代码](https://leetcode-cn.com/problems/4sum/solution/si-shu-zhi-he-by-leetcode-solution/)：**

```python
class Solution:
    def fourSum(self, nums, target):
        quadruplets = list()
        length = len(nums)#求nums的长度
        if not nums or length < 4:#如果列表nums长度小于4或者nums为空，直接返回空列表
            return quadruplets
        
        nums.sort()#给列表排序，为了双指针操作移动有依据
        
        for i in range(length - 3):#第一重循环
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break#这里判断前四个数字是否大于给的数字，因为已经排序，所以最小的四个数字大于target的话，说明没有数字可以满足，因此直接可以提前结束
            if nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target:
                continue#这里判断最后的四个数字是否小于给的数字，因为已经排序，所以不符合的话说明最大的几个数字都无法达到target值，所以直接可以提前结束
            for j in range(i + 1, length - 2):#第二重循环，双指针操作
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target:
                    continue
                left, right = j + 1, length - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        
        return quadruplets
```

**trick（不容易注意到的点）：**

​		有一些小的优化，可以提前退出循环，详情见代码注释。

**提交结果：**

- 283/283 cases passed (44 ms)
- Your runtime beats 97.36 % of python submissions
- Your memory usage beats 48.48 % of python submissions (12.4 MB)

**自己的体会：**

​	有了前面的基础，这个题其实不难，如果没看过前几个题的话，可以去看一下，又是进步的一天！
