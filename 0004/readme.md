# 4. leetcode第四题

**欢迎来到[leetcode第四题](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/)**

```markdown
   Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

   Follow up: The overall run time complexity should be O(log (m+n)).
```

**翻译**：

```markdown
   给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

   请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

   你可以假设 nums1 和 nums2 不会同时为空。
```

**样例:**

```markdown
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0

nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5
```

## 4.1 python解决	

**思路如下：**

​        首先题目给的是正序数组，那么就不需要我们为数组排序，然后我们要注意这道题要求算法复杂度，一般时间复杂度带log的差不多都是二分法。

​        然后我们先来想想注意事项，两个数组中元素不确定，有可能是奇数也有可能是偶数，所对应的中位数就带来了是否需要除2的问题，还有可能存在一个为空数组的情况，这些我们都要考虑进去，那么我们接下来看代码吧。

**代码及注释如下：**

```python
class Solution(object):
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.kth(A, B, l // 2)
        else:
            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.   
        
    def kth(self, a, b, k):
      '''######################
      #输入：数组a，b，和整数k
      #     (k输入为ab之和//2或者ab之和//2-1，即中位数的位置或者中位数的前后位置)
      #返回：a，b所有元素排序后的第k位
      #注意，这里使用了递归嵌套，所以在本题中最后返回的是中位数的位置或者中位数的前后位置
      '''#########################
      
      #判断是否为空数组（最后的函数结束在这里）当有一个被切片切成空数组时，就返回最后的结果
        if not a:
            return b[k]
        if not b:
            return a[k]
          
        ia, ib = len(a) // 2 , len(b) // 2
        ma, mb = a[ia], b[ib]#得到a的中间元素或者中位数后面的那个元素的位置
        
        #如果a，b中元素个数都为奇数，和是偶数个的时候，ia+ib<k成立，在这种情况下继续向下判断
        if ia + ib < k:
            if ma > mb: # 执行在这里说明a和b都是奇数数组，如果a的中位数大于b的中位数，那么b中包括中位数在内的前一半的元素都没有比a的中位数大的元素了
                return self.kth(a, b[ib + 1:], k - ib - 1)#那么利用python数组切片进行操作，这里需要注意b切走的是偶数个，所以切完的b还是奇数个元素，利用二分法查找
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        else:
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)
```

**提交结果：**

- 2091/2091 cases passed (48 ms)
- Your runtime beats **67.23 %** of python3 submissions
- Your memory usage beats **48.66 %** of python3 submissions (14.9 MB)

**自己的体会：**

​	这题主要用的是python数组切片进行二分法查找，具体的还需要大家自行写两个数组过一遍流程。事实上我是在大一自学的python，那会还没学习c，c++，java语言，所以后来很多思想都是拿python的往里面套，后来我就发现，有的可以类比着学，有的确实类比着学不了，这也从另一方面说明了每种语言都有他独自的特性，比如c，c++的指针，python就没有，还比如我学完python学的c，发现python的列表元祖字典确实可以涵盖绝大部分的数据结构，或者说有这些足够使了，再加上python本身比较简单，也曾有一部分时间觉得其他语言都不如python好使，后来学的多了发现每种语言都有优缺点，这也告诉了我这个世上没有啥十全十美的事情，任何事物有好有坏，只不过在于你怎么看待它。写着写着扯远了。。。不过，还是那句忠告，数据结构和算法是程序员的很基础很基础的东西，具体怎么实现可能不同语言有不同语言的方法，但是重点是你能想得到哪部分题用哪种算法有哪些效果，这是很重要的。今天身体有点不舒服，c++代码我就不写了，断更c++一天哈，明天继续加油！

