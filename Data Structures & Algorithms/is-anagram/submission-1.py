class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        words={}
        for word in s:
            words[word]=words.get(word,0)+1
        for word in t:
            if word in words:
                words[word]-=1
                if words[word]==0:
                    words.pop(word)
        
        if len(words)==0:
            return True
        else:
            return False

        