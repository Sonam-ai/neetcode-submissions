class Solution:
    def trap(self, height: List[int]) -> int:
        max_l=[]
        max_r=[]
        max_val_l=0
        max_val_r=0
        for num in height:
            max_val_l=max(max_val_l,num)
            max_l.append(max_val_l)
        for num in reversed(height):
            max_val_r=max(max_val_r,num)
            max_r.append(max_val_r)
        max_r.reverse()
        result=0
        for i in range(len(height)):
            result+=min(max_l[i],max_r[i])-height[i]
        return result

        