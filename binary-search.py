from typing import List

class Solution:
    def findIndex(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1 #set low and high array index
        while low <= high:
            mid = (low + high) //2 #set index for mid of array
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1 #if value in mid of array is higher than target - move mid of array to lower number
            else:
                low = mid + 1 #if value in mid of array is lower than target - move mid of array to higher number
        return -1
        
    def displayOutput(self, result): #function to display results
        if result == -1: #Custom message if there is no numbers
            print("No element found")
        else:
            print("Element found at the:", result+1, "(index", result,") position.")
            print(" ")


x = Solution()

nums1 = [2, 3, 5, 7, 9]
target1 = 7
x.displayOutput(x.findIndex(nums1, target1))

nums2 = [1, 2, 3, 4, 4, 5, 6, 7]
target2 = 4
x.displayOutput(x.findIndex(nums2, target2))

nums3 = [1, 4, 5, 8, 9]
target3 = 2
x.displayOutput(x.findIndex(nums3, target3))