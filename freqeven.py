class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        max_count = 0
        most_frequent_even = None

        for num in nums:
            if num % 2 == 0:
                if num in count:
                    count[num] += 1
                else:
                    count[num] = 1

                if count[num] > max_count:
                    max_count = count[num]
                    most_frequent_even = num
                elif count[num] == max_count and num < most_frequent_even:
                    most_frequent_even = num

        if most_frequent_even is not None:
            return most_frequent_even
        else:
            # If there are no even numbers in the list, return -1 as expected
            return -1
