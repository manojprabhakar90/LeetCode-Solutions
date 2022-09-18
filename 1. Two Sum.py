Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Approach: 
    1. Initialize a hashmap
    2. Rather than iterating through each and every combination of array, start with difference between target and each value. 
    3. If both the values are available in hashset, return the index of the value. 
    4. Else add the index of the new number to the hashset
    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset={}
        for i,a in enumerate(nums):
            diff = target-a
            if diff in hashset:
                return (hashset[diff],i)
            hashset[a]=i
        return hashset

Time Complexity  - O(n)
Space Complexity - O(n) since we are creating a hashmap. 
