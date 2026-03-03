class Solution(object):
    def maxArea(self, height):
        maxWater = 0 
        left = 0 
        right = len(height) - 1
        while (left < right):
            w = right - left 
            ht = min(height[right], height[left])
            current_Water = w * ht
            maxWater = max( maxWater , current_Water)
            if height[left] < height [right]:
                left +=1 
            else :
                right -=1
        return maxWater
        