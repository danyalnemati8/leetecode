class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        # Sort the dictionary items by frequency in descending order
        sorted_items = sorted(count.items(), key=lambda item: item[1], reverse=True)

        # Extract the top K frequent elements
        result = [item[0] for item in sorted_items[:k]]

        return result


            
        