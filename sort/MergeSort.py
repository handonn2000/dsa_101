class MergeSort:
    def _mergeSort(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []
        p1 = 0
        p2 = 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] <= nums2[p2]:
                ans.append(nums1[p1])
                p1 += 1
            else:
                ans.append(nums2[p2])
                p2 += 1
        
        while p1 < len(nums1):
            ans.append(nums1[p1])
            p1 += 1

        while p2 < len(nums2):
            ans.append(nums2[p2])
            p2 += 1

        return ans
    
    def sort(self, nums: list[int]) -> list[int]:
        if len(nums) == 1:
            return nums
        
        mid = len(nums)//2

        nums1 = self.sort(nums[:mid])
        nums2 = self.sort(nums[mid:])

        return self._mergeSort(nums1, nums2)

assert MergeSort().sort([3,7,2,-4,9]) == [-4,2,3,7,9]
assert MergeSort().sort([5,4,3,2,1]) == [1,2,3,4,5]
assert MergeSort().sort([3,7,2,4,9]) == [2,3,4,7,9]
assert MergeSort().sort([3,7,2,2,9]) == [2,2,3,7,9]
assert MergeSort().sort([1,2,3,4,5]) == [1,2,3,4,5]
assert MergeSort().sort([2,1]) == [1,2]
assert MergeSort().sort([1]) == [1]


print("All tests passed")