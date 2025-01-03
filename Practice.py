# Palindromic Substrings

# Given a string s, return the number of substrings within s that are palindromes.
# A palindrome is a string that reads the same forward and backward.

# Example 1:

# Input: s = "abc"
# Output: 3

# Explanation: "a", "b", "c".

# Example 2:
# Input: s = "aaa"

# Output: 6

# Explanation: "a", "a", "a", "aa", "aa", "aaa". Note that different substrings are counted as different palindromes even if the string contents are the same.

# Constraints:

# 1 <= s.length <= 1000
# s consists of lowercase English letters.

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                l, r = i, j
                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1
                res += (l >= r)
                
        return res


# Contains Duplicate

# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]
# Output: true

# Example 2:

# Input: nums = [1, 2, 3, 4]
# Output: false

class Solution:
    def hasDuplicate(self, nums: list) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False

# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"
# Output: true

# Example 2:

# Input: s = "jar", t = "jam"
# Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Example 1:

# Input: 
# nums = [3,4,5,6], target = 7

# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

# Example 2:

# Input: nums = [4,5,6], target = 10

# Output: [0,2]
# Example 3:

# Input: nums = [5,5], target = 10

# Output: [0,1]

class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        dict = {}

        for index,num in enumerate(nums):
            complement = target - num

            if complement in dict:
                return [dict[complement], index]

            dict[num] = index       