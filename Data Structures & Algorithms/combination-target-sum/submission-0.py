class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def helper(i,arr,curr_sum):
            if curr_sum>target:
                return
            if curr_sum==target:
                res.append(arr[:])
                return
            for j in range(i,len(nums)):
                arr.append(nums[j])
                helper(j,arr,curr_sum+nums[j])
                arr.pop()

        helper(0,[],0)
        return res
        
        