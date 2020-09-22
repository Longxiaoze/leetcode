# 1. leetcode第一题

**欢迎来到[leetcode第一题](https://leetcode-cn.com/problems/two-sum/)**

```markdown
  Given an array of integers, return indices of the two numbers such that they add up to a specific target.
  You may assume that each input would have exactly one solution, and you may not use the same element twice.
```

**翻译**：

```markdown
   给定一个全是int的数组和一个整数target，要求返回两个下标，使得数组当中这两个下标对 应的和等于target。你可以假设一定值存在一个答案，并且一个元素不能使用两次。
```

## 1.1 python解决	

如果你没有接触过leetcode的话，拿到这道题的第一个反应就是暴力枚举，两个for循环搞定，这样做毫无疑问是正确的，但是如果你这么做了，那么一定不会通过，这是一个呢n^2的算法，消耗太多的时间，一般来说，leetcode中*O*(*n*2) 都不是最好的算法。

**代码及注释如下：**

```python
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dic = {}#定义一个字典用来存放键值对
        for i in range(len(num)):#遍历给定的数组
            if num[i] not in dic:#判断元素在不在字典中，不在的话扩充target-原数组的数到字典中
                dic[target - num[i]] = i
                #键值对格式为：键：要求的target-原数组的数；值：原数组的数在数组的位置
            else:
                return dic[num[i]], i#判断当该数字存在的话，说明这就是其中之一的那个数，那么返回之前的值的位置和当前的位置
        return -1, -1#如果循环没有返回，则返回-1，-1
```

**流程实例化演示（这里等于不是赋值，就是演示用）**

```markdown
num = [2,7,11,15],tar = 9
dic={}
i = 0时：判断num[0] = 2不在字典中，则将9-2:0添加到字典中
dic={7:0}
i = 1时：判断num[1] = 7,在字典中，则返回dic[num[i]] = dic[num[1]] = dic[7] = 0和i = 1。
函数结束。
```

**trick（不容易注意到的点）：**

​	自己写代码需要注意当num = [3,3],target = 6时，如果你用删除或者其他一些操作的话，无法返回正常答案[0,1]，只会返回一个值或者报错，我自己感觉这也是leetcode给所有新手包括我第一次做这个题的一个坑。这个也告诉我们做题要想详细了。

```markdown
num = [3,3],tar = 6
dic={}
i = 0时：判断num[0] = 3不在字典中，则将6-3:0添加到字典中
dic={3:0}
i = 1时：判断num[1] = 3,在字典中，则返回dic[num[i]] = dic[num[1]] = dic[7] = 0和i = 1
函数结束。
```

​	这样就不会产生**trick**中的问题。

**提交结果：**

- 29/29 cases passed (40 ms)
- Your runtime beats **98.02 %** of python3 submissions
- Your memory usage beats **14.69 %** of python3 submissions (14.9 MB)

**自己的体会：**

​	本题我为了将时间复杂度降低使用了字典，但是实际上如果所搜索的数组比较大的时候，字典所产生的内容就会特别多，占用内存就会特别特别的大。

## 1.2 c++解决

​	上述已经介绍了很多东西了，在这里借鉴字典的思想，引入c++的[map](https://leetcode-cn.com/problems/two-sum/solution/1-liang-shu-zhi-he-mapzai-ha-xi-fa-zhong-de-jing-d/)思路于python解决类似，这里只放代码就不多解释了，作者精力有限，主要以python讲解为主。

```c++
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map <int,int> map;
        for(int i = 0; i < nums.size(); i++) {
            auto iter = map.find(target - nums[i]);
            if(iter != map.end()) {
                return {iter->second, i};
            }
            map.insert(pair<int, int>(nums[i], i));
        }
        return {};
    }
};
// 作者：carlsun-2
// 链接：https://leetcode-cn.com/problems/two-sum/solution/1-liang-shu-zhi-he-mapzai-ha-xi-fa-zhong-de-jing-d/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

**提交结果：**

- 29/29 cases passed (12 ms)
- Your runtime beats **90.15 %** of cpp submissions
- Your memory usage beats **14.4 %** of cpp submissions (9.9 MB)

**自己的体会：**

​	同样的，我认为内存占用过高的原因是本题的作者为了将时间复杂度降低使用了map，但是实际上如果所搜索的数组比较大的时候，map所产生的内容就会特别多，占用内存就会特别特别的大。

## 1.3总结

​	**首先我只是想分享我在学习中的一些想法和学习过程，如有侵权请联系我，保证侵权必删。**leetcode作为当前互联网公司面试必考的题库，我觉得作为一个工科生，应该多做一些算法题，就算不为了功利心也应该开阔自己的思路，其实算法题在生活中也应用很多。而且对于新手我建议不必太在意语言，主要是做题思路，发散思路，如果没有编程经验的同学也可以尝试学习使用python，确实上手比较快。作者也主要以python解决为主，毕竟精力有限，还得准备考试什么的。。。。。
