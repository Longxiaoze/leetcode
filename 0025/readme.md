# 26. leetcode第二十六题

**欢迎来到[leetcode第二十六题](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)**

```markdown
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.
```

**翻译**：

```markdown
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
```

**样例:**

```markdown
给定数组 nums = [1,1,2], 

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 

你不需要考虑数组中超出新长度后面的元素。

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。
```

## 24.1 python解决	

第一眼看到这个题，我的第一反应是用Python将list转化为集合，因为集合可以将重复项去掉，然后报错。。。看题目：为什么返回数值是整数，但输出的答案是数组呢?

这是因为，传入的是引用，mian函数给removeDuplicates传递了一个引用
removeDuplicates函数修改了数组中的值，等函数执行完后，mian函数就可以感知函数的变化了
函数返回值为2
那么mian函数中，可以根据返回的2，来遍历这段范围内的所有元素，比如：

```python
int len = removeDuplicates(nums);
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```

所以如果转化为集合，最后打印的还是原数组的位置，因为数组并未改变。

**代码及注释如下：**

```python
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        j = 0
        for i in xrange(len(nums)):
            if nums[i]!=nums[j]:
                j += 1
                nums[j] = nums[i]
        return j+1

# 作者：wang_ni_ma
# 链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/solution/duo-tu-yan-shi-26shan-chu-pai-xu-shu-zu-zhong-de-z/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

**提交结果：**

- 161/161 cases passed (16 ms)
- Your runtime beats 71.11% of python submissions
- Your memory usage beats 25.22% of python submissions (14.2 MB)

**自己的体会：**

看来简单题也得好好做啊。。。。。
