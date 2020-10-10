class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarysearch(i,j):
            if i>j:
                return -1
            mid=(i+j)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                return binarysearch(mid+1,j)
            else:
                return binarysearch(i,mid-1)
        return binarysearch(0,len(nums)-1)
