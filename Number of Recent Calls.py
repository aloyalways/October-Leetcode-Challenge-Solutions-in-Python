class RecentCounter:

    def __init__(self):
        self.count=[]

    def ping(self, t: int) -> int:
        self.count.append(t)
        ans=0
        for i in range(len(self.count)-1,-1,-1):
            if t-3000<=self.count[i]<=t:
                ans+=1
            else:
                break
        return ans


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
