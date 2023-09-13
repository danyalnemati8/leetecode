class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(e for e in s if e.isalnum()).lower()
        f,e = 0, len(s)-1
        while f < e:
            if s[f] != s[e]:
                return False
            else:
                f += 1
                e -= 1
        return True