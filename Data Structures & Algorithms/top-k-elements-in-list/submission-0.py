class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        result=[]
        for _ in range(k):
            max_key=(max(freq,key=freq.get))
            result.append(max_key)
            freq.pop(max_key)
        return result




        