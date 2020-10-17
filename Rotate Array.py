class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k=n-(k%n)
        for i in range(k):
            t=nums.pop(0)
            nums.append(t)
