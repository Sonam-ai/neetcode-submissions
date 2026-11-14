class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def helper(index):
            if index==len(nums)-1:
                res.append(nums[:])
                return
            for j in range(index,len(nums)):
                nums[index],nums[j]=nums[j],nums[index]
                helper(index+1)
                nums[index],nums[j]=nums[j],nums[index]

        helper(0)
        return res
        