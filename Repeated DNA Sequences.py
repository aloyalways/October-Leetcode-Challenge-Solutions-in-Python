from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n=len(s)-10
        store=defaultdict(lambda:0)
        
        ans=[]
        for i in range(n+1):
            if store[s[i:i+10]]==1:
                ans.append(s[i:i+10])
            store[s[i:i+10]]+=1
        return ans
