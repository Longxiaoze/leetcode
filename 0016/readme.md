# 16. leetcode第十六题

**欢迎来到[leetcode第十六题](https://leetcode-cn.com/problems/3sum-closest)**

```markdown
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
```

**翻译**：

```markdown
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
```

**样例:**

```markdown
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

Constraints:
  3 <= nums.length <= 10^3
  -10^3 <= nums[i] <= 10^3
  -10^4 <= target <= 10^4

```

## 16.1 python解决	

**代码及注释如下[官方题解](https://leetcode-cn.com/problems/3sum-closest/solution/zui-jie-jin-de-san-shu-zhi-he-by-leetcode-solution/)：**

```python
##python3环境提交，nonlocal best在python环境不通过
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = 10**7
        
        # 根据差值的绝对值来更新答案
        def update(cur):
            nonlocal best
            if abs(cur - target) < abs(best - target):
                best = cur
        
        # 枚举 a
        for i in range(n):
            # 保证和上一次枚举的元素不相等
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 使用双指针枚举 b 和 c
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                # 如果和为 target 直接返回答案
                if s == target:
                    return target
                update(s)
                if s > target:
                    # 如果和大于 target，移动 c 对应的指针
                    k0 = k - 1
                    # 移动到下一个不相等的元素
                    while j < k0 and nums[k0] == nums[k]:
                        k0 -= 1
                    k = k0
                else:
                    # 如果和小于 target，移动 b 对应的指针
                    j0 = j + 1
                    # 移动到下一个不相等的元素
                    while j0 < k and nums[j0] == nums[j]:
                        j0 += 1
                    j = j0

        return best
```

**代码及注释如下[python题解](https://leetcode-cn.com/problems/3sum-closest/solution/pythonshuang-zhi-zhen-you-hua-ji-bai-999-by-hardca/)：**

```python
class Solution:
    def threeSumClosest(self, nums, target):
        n = len(nums)
        nums.sort()         # 排序
        ans = float('inf') 

        for first in range(n-2):        # 枚举第一个元素
            if first > 0 and nums[first] == nums[first-1]: continue     # 保证first不会有重复

            second, third = first + 1, n - 1
            max_sum = nums[first] + nums[-2] + nums[-1]
            min_sum = nums[first] + nums[first + 1] + nums[first + 2]
            if max_sum <= target:    # 最大的数
                if abs(max_sum - target) < abs(ans - target):
                    ans = max_sum
                continue              
            elif min_sum >= target:  # 最小的数
                if abs(min_sum - target) < abs(ans - target):
                    ans = min_sum      
                break   
                      
            while second < third:
                two_sum_target = target - nums[first]
                s = nums[second] + nums[third]
                if abs(s + nums[first] - target) < abs(ans - target):
                    ans = s + nums[first]
                if s > two_sum_target:  # 当前数值太大 右指针左移
                    third -= 1
                    while third > second and nums[third] == nums[third + 1]:
                        third -= 1
                elif s < two_sum_target:  # 当前数值太小 左指针右移
                    second += 1
                    while third > second and nums[second] == nums[second - 1]:
                        second += 1 
                else:                   # 刚好等于 直接返回target即可
                    return target 

        return ans
'''
作者：HardCandy
链接：https://leetcode-cn.com/problems/3sum-closest/solution/pythonshuang-zhi-zhen-you-hua-ji-bai-999-by-hardca/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''
```

**提交结果（2）：**

- 131/131 cases passed (20 ms)
- Your runtime beats 100.00 % of python submissions
- Your memory usage beats 13.82 % of python submissions (12.6 MB)

**自己的体会：**

​	第二个真大佬解题，建议细品。。。百分百是我没想到的。。。。
