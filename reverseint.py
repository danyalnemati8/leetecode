class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        reversed_x = 0
        sign = 1 if x >= 0 else -1  # Determine the sign, including 0
        
        x = abs(x)  # Make x positive for processing
        
        while x != 0:
            # Check for overflow/underflow before updating reversed_x
            if reversed_x > INT_MAX // 10 or reversed_x < INT_MIN // 10:
                return 0
            
            digit = x % 10
            x //= 10
            reversed_x = reversed_x * 10 + digit
        
        reversed_x *= sign  # Restore the original sign
        
        if reversed_x > INT_MAX or reversed_x < INT_MIN:
            return 0  # Overflow or underflow
        
        return reversed_x
