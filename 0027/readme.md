# 27. leetcode第二十七题

**欢迎来到[leetcode第二十七题](https://leetcode-cn.com/problems/remove-element/)**

```markdown
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.
```

**翻译**：

```markdown
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
```

**样例:**

```markdown
给定 nums = [3,2,2,3], val = 3,
函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
你不需要考虑数组中超出新长度后面的元素。

给定 nums = [0,1,2,2,3,0,4,2], val = 2,
函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
注意这五个元素可为任意顺序。
你不需要考虑数组中超出新长度后面的元素。
```

## 27.1 python解决	

看一下题目要求：原地移除，不要使用额外的数组空间，不需要考虑数组中超出新长度后面的元素，题目要求我们原地删除所有等于 val 的元素，不能使用额外空间，且不用考虑删除后超出新数组长度后面的元素。也就是说，如果原数组 nums 长度为 x，要删除的 val 元素个数为 y，那么我们只要把这 n 个要删除的元素所在位置用其他有效元素覆盖掉，然后返回最终的数组长度 x - y。题目并非让我们真的删除数组的元素，而是要改写相关元素的值。

不过很显然python中有删除列表元素的函数，下面是用法。

**代码及注释如下：**

```python
class Solution(object):
    def removeElement(self, nums, val):
        if nums!=None:
            for i in range(nums.count(val)):
                nums.remove(val)
            return len(nums)
        else:
            return len(nums)
```

但是显然这道题原意是让我们操作数组，下面看一下[双指针解法](https://leetcode-cn.com/problems/remove-element/solution/san-chong-shi-xian-tu-jie-27yi-chu-yuan-su-by-wang/)。

**代码及注释如下：**

```python
class Solution(object):
    def removeElement(self, nums, val):
        if not nums:
            return 0
        i = 0
        n = len(nums)
        while i<n:
            if nums[i]==val:
                nums[i] = nums[n-1]
                n -= 1
            else:
                i += 1
        return i
'''
作者：wang_ni_ma
链接：https://leetcode-cn.com/problems/remove-element/solution/san-chong-shi-xian-tu-jie-27yi-chu-yuan-su-by-wang/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''
```

**提交结果：**

调python列表函数remove()和使用双指针运行存在很大不确定性，就不对比了，大家都学习一下吧

**自己的体会：**

不难，学习学习。。。。
