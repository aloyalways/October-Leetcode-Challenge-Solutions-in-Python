class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        if m==0:
            return False
        n=len(matrix[0])
        if n==0:
            return False
        
        point=-1
        for i in range(m):
            if matrix[i][0]<=target<=matrix[i][-1]:
                point=i
        if point==-1:
            return False
        
        i,j=0,n-1
        while i<=j:
            mid=(i+j+1)//2
            if matrix[point][mid]==target:
                return True
            elif matrix[point][mid]>target:
                j=mid-1
            else:
                i=mid+1
        return False
