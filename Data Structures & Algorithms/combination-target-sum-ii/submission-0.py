class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def helper(i,arr,curr_sum):
            if curr_sum>target:
                return
            if curr_sum==target:
                res.append(arr[:])
                return
            hash={}
            for j in range(i,len(candidates)):
                if candidates[j] not in hash:
                    hash[candidates[j]]=True
                    arr.append(candidates[j])
                    helper(j+1,arr,curr_sum+candidates[j])
                    arr.pop()
        helper(0,[],0)
        return res
        