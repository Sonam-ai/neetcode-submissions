class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def backtrack(i,arr):
            if i==len(nums):
                result.append(arr[:])
                return
            #include
            arr.append(nums[i])
            backtrack(i+1,arr)
            arr.pop()

            #exclude
            backtrack(i+1,arr)

        backtrack(0,[])
        return result
         
        