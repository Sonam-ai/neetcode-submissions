class Solution:
    def isPalindrome(self, s: str) -> bool:
        start=0
        end=len(s)-1
        lower_s=s.lower()
        while start<end:
            if not lower_s[start].isalnum():
                start+=1
            elif not lower_s[end].isalnum():
                end-=1
            else:
                if lower_s[start]!=lower_s[end]:
                    return False
                start+=1
                end-=1
        return True


        