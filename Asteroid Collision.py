class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans=[]
        for i in range(len(asteroids)):
            if asteroids[i]>0:
                ans.append(asteroids[i])
                continue
                
            if len(ans)==0 or ans[-1]<0:
                ans.append(asteroids[i])
                continue
            
            add=True
            while len(ans)>0:
                if ans[-1]<0:
                    break
                elif abs(asteroids[i])>ans[-1]:
                    ans.pop(-1)
                elif abs(asteroids[i])==ans[-1]:
                    ans.pop(-1)
                    add=False
                    break
                else:
                    break
            
            if len(ans)==0 or ans[-1]<0:
                if add:
                    ans.append(asteroids[i])
                continue
        
        return ans
