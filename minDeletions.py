class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        countletters = {}
        
        # Count the frequency of each letter in the string
        for letter in s:
            if letter in countletters:
                countletters[letter] += 1
            else: 
                countletters[letter] = 1

        freq_set = set()
        numdelete = 0

        for letter, freq in countletters.items():
            while freq in freq_set:
                freq -= 1
                numdelete += 1
            if freq > 0:
                freq_set.add(freq)

        return numdelete
