class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def helper(i,summ,arr):
            if summ==target:
                ans.append(tuple(arr))
                return 
            if i>=len(candidates) or summ>target:
                return
            helper(i+1,summ,arr)
            helper(i+1,summ+candidates[i],arr+[candidates[i]])
            helper(i,summ+candidates[i],arr+[candidates[i]])
            
        helper(0,0,[])
        return list(set(ans))
