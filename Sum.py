class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        i = 0
        x = True
        while x:
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    print([i,j])
                    x = False
            i += 1

solution = Solution()
solution.twoSum([2,7,11,15],9)  

