class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # counter
        charCounter = collections.Counter(chars)
        
        res = 0
        # is good
        for word in words:
            if self.isGood(word, charCounter.copy()):
                res += len(word)
                
        return res
    
    def isGood(self, word: str, counter) -> bool:
        for i in range(len(word)):
            if word[i] not in counter:
                return False
            
            counter[word[i]] -= 1
            if counter[word[i]] < 0:
                return False
            
        return True
