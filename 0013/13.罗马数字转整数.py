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
