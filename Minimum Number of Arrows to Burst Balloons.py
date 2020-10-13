class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points)==0:
            return 0
        points=sorted(points)
        arrows=0
        minPos=points[0][0]
        maxPos=points[0][1]
        for i in points[1:]:
            if i[0]<=maxPos:
                maxPos=min(maxPos,i[1])
                continue
            else:
                arrows+=1
                minPos=i[0]
                maxPos=i[1]
        return arrows+1
