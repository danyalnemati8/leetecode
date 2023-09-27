class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height)-1
        marea = 0
        while r > l:
            h = min(height[l], height[r])
            w = r - l
            area = h * w
            marea = max(marea, area)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return marea