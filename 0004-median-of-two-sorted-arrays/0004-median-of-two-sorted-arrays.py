class Solution:
    def merge(self, nums1, nums2, i, j, ans):
        if i == len(nums1): 
            ans.extend(nums2[j:]) 
            return
        if j == len(nums2):
            ans.extend(nums1[i:])
            return
        if nums1[i] <= nums2[j]: 
            ans.append(nums1[i])
            self.merge(nums1, nums2, i + 1, j, ans)
        else:
            ans.append(nums2[j])
            self.merge(nums1, nums2, i, j + 1, ans)

    def findMedianSortedArrays(self, nums1, nums2):
        ans = []
        self.merge(nums1, nums2, 0, 0, ans)
        n = len(ans)
        if n % 2 : 
            return ans[n // 2] 
        return (ans[n // 2 - 1] + ans[n // 2]) / 2.0

        
       
    # def findMedianSortedArrays(self, nums1, nums2):
    #     ans = []
    #     self.merge(nums1, nums2, 0, 0, ans)

    #     print("ANS =", ans)   # DEBUG
    #     n = len(ans)
    #     print("N =", n)       # DEBUG
    #     if n % 2:
    #       return ans[n // 2]
        # return (ans[n // 2 - 1] + ans[n // 2]) / 2.0
