class Solution(object):
    def myPow(self, x, n):   
        if n == 0:
            return 1
        # Handle negative powers
        if n < 0:
            x = 1 / x
            n = -n
        # Recursive call
        half = self.myPow(x, n // 2)  
        # If n is even
        if n % 2 == 0: 
            return half * half       
        # If n is odd
        else: 
            return half * half * x 
