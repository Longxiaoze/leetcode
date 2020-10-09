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
