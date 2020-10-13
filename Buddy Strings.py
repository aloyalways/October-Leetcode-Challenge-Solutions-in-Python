from collections import Counter
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A)!=len(B):
            return False
        swap=[]
        for i in range(len(A)):
            if A[i]!=B[i]:
                swap.append(i)
        if len(swap)==0:
            t=Counter(A)
            for i in t:
                if t[i]>1:
                    return True
        if len(swap)==2:
            if A[swap[0]]==B[swap[1]] and A[swap[1]]==B[swap[0]]:
                return True
        return False
