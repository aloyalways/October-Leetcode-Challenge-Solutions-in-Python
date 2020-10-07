class Solution:
    def bitwiseComplement(self, N: int) -> int:
        num=bin(N)[2:]
        ans=""
        for i in num:
            if i=="0":
                ans+="1"
            else:
                ans+="0"
        return int(ans,2)
