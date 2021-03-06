# 88. Merge Sorted Array

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1 = nums1 + nums2
        print (nums1)

        fill = m + n -1
        i = m - 1
        j = n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[fill] = nums1[i]
                i -= 1
            else:
                nums1[fill] = nums2[j]
                j -= 1 
            fill -= 1

        while j >= 0:
            nums1[fill] = nums2[j]
            j -= 1
            fill -= 1
        print (nums1)

        return

class Solution2:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        if n == 0:
            return 

        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]

            return
        
        l = len(nums1)
        for i in range(m):
            nums1[l - 1 - i] = nums1[m - 1 - i]

        i = 0 
        j = 0
        p1 = 0
        while i < m and j < n:
            if nums1[l - m + i] < nums2[j]:
                nums1[p1] = nums1[l - m + i]
                p1 += 1
                i += 1
            else:
                nums1[p1] = nums2[j]
                p1 += 1
                j += 1

        if i < m:
            while i < m:
                nums1[p1] = nums1[l - m + i]
                p1 += 1
                i += 1
        else:
            while j < n:
                nums1[p1] = nums2[j]
                p1 += 1
                j += 1

        return

if __name__=='__main__':

    a = [0,2,4]
    b = [1,3,5]
    so = Solution()

    so.merge(a,len(a),b,len(b))

    print (a) 
