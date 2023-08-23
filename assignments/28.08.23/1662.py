class Solution:
    def  arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        stringA = ''.join(word1)
        stringB = ''.join(word2)
        

        if stringA == stringB:
            return True
        else:
            return False