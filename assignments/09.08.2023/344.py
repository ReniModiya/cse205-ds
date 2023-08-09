class Solution:
    def reverseString(self, s: List[str]) -> None:
        
          def new(left, right):
            if left >= right:
                return s
            
            s[left], s[right] = s[right], s[left]
            new(left + 1, right - 1)
            
          new(0, len(s) - 1)
        