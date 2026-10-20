class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        index=[]
        result=[0]*len(temperatures)
        n=len(temperatures)-1
        for i in range(n,-1,-1):
            while index and temperatures[i]>=temperatures[index[-1]]:
                index.pop()

            if index:
                result[i]=index[-1]-i

            index.append(i)

        return result
            
        