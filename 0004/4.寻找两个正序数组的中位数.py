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
