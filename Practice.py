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

