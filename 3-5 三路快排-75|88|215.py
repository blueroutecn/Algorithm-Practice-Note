# leetcode-75. Sort Colors

nums = [2,0,2,1,1,0]
a = -1
b = len(nums)
i = 0
while(i < b):
    if nums[i] == 0:
        a+=1
        nums[a], nums[i] = nums[i], nums[a]
        i+=1
        
    elif nums[i] == 2:
        b-=1
        nums[b], nums[i] = nums[i], nums[b]
    else:
        assert(nums[i] == 1)
        i+=1
print(nums)


# leetcode-88. Merge Sorted Array
# method1 创建一个额外的数组存放元素
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        a = [0]*(m+n)
        i = 0
        j = 0
        k = 0
        while(i<m and j < n):
            if (nums1[i] <= nums2[j]):
                a[k] = nums1[i]
                i+=1
                k+=1
            else:
                a[k] = nums2[j]
                j+=1
                k+=1

        if i<=m:
            for _ in range(i, m):
                a[k] = nums1[_]
                k+=1

        if j<=n:
            for _ in range(j, n):
                a[k] = nums2[_]
                k+=1
                
        for i in range(len(a)):
            nums1[i] = a[i]
            
            
# method2 从末尾开始比较

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        k = len(nums1)
        while(m>0 and n>0):
            if nums1[m-1] >= nums2[n-1]:
                nums1[k-1], nums1[m-1] = nums1[m-1], nums1[k-1]
                m-=1
                k-=1
            else:
                nums1[k-1] = nums2[n-1]
                n-=1
                k-=1
        print(nums1)
        print(nums2)

        if m<=0:
            for i in range(0, n):
                nums1[i] = nums2[i]
