from collections import defaultdict
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        numbers=defaultdict(set)
        n=len(A)
        for i in range(n):
            numbers[A[i]].add(i)
            numbers[B[i]].add(i)
        
        temp=[]
        for i in numbers:
            if len(numbers[i])==n:
                temp.append(i)
                break
        else:
            return -1
        
        ans=float('inf')
        for i in temp:
            rot=n
            for j in A:
                if i==j:
                    rot-=1
            ans=min(ans,rot)
            
        for i in temp:
            rot=n
            for j in B:
                if i==j:
                    rot-=1
            ans=min(ans,rot)
        return ans
