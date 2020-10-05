from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count=Counter(nums)
        
        ans=0
        for i in count:
            if k==0:
                if count[i]>1:
                    ans+=1
            else:
                if count[i-k]:
                    ans+=1
                if count[i+k]:
                    ans+=1
        if k==0:
            return ans
        return ans//2
