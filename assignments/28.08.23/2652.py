class Solution:
    def sumOfMultiples(self, n: int) -> int:
        addition = 0
        for num in range(0,n+1):
            if num % 3 == 0 or num % 5 == 0 or num % 7 ==0 :
                # print(num) 
                addition+= num
        return addition

