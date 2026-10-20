class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_count=0
        for num in num_set:
            count=0
            if num-1 not in num_set:
                count+=1
                current = num
                while current+1 in num_set:
                    count+=1
                    current+=1
            max_count=max(max_count,count)
        return max_count