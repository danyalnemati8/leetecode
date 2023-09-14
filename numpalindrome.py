class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Convert the integer to a list of its digits
        digits_list = [int(digit) for digit in str(abs(x))]

        # Include the negative sign if it's a negative number
        if x < 0:
            digits_list.insert(0, -1)
        f,e = 0, len(digits_list)-1
        while f < e:
            if digits_list[f] != digits_list[e]:
                return False
            else:
                f += 1
                e -= 1
        return True