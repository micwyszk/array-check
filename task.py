from typing import List

class Solution:
    def findIndex(self, nums: List[int], target: int) -> int:
        counter = 0 # counter for array index
        position = [] # array index holder
        for number in nums:
            if number > target: #provided numbers are sorted, so if target is lower than number, there will be no occurences 
                break
            elif number == target:
                position.append(counter) #add target index to array
                counter = counter + 1
            else:
                counter = counter + 1
        if not position:
            position.append(-1) #insert -1 value if there is no target occurences
        return position
        
    def displayOutput(self, nums: List[int]): #function to display results
        if -1 in nums: #Custom message if there is no numbers
            print("No element found")
        else:
            print("Element found at the: ")
            for num in nums:
                print(num+1, "(index", num,")")
            if len(nums) == 1: #if there is one element, use singular form
                print("position")
            else:
                print("positions")
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