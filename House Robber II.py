class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        def helper(nums,i):
            if i>=len(nums):
                return 0
            if dp[i]!=-1:
                return dp[i]
            dp[i]=max(nums[i]+helper(nums,i+2), helper(nums,i+1))
            return dp[i]
            
        dp=[-1]*(len(nums)+1)
        a=helper(nums[:-1],0)
        
        dp=[-1]*(len(nums)+1)
        b=helper(nums[1:],0)
        
        return max(a,b)
