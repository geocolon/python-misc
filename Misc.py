message = "Hello, World!"
print(message)

nums = [2, 7, 11, 15]
target = 9

for x in range(len(nums)):
    for y in range(x + 1, len(nums)):
        if nums[x] + nums[y] == target:
            print([x, y])
print("Problem 1: Two Sum (LeetCode #1)**")
# Given an array of integers nums and an integer target, return the indices of the two numbers that add up to target.
# You may assume each input has exactly one solution, and you can't use the same element twice.
# Example:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: nums[0] + nums[1] = 2 + 7 = 9
# Before you write any code, tell me:

# How would you describe this problem in your own words?
# What approach are you thinking about?

# Then write your solution. Go.

#Problem 2: Valid Anagram (LeetCode #242)**

# Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, `False` otherwise.
# ```
# Example 1: s = "anagram", t = "nagaram" -> True
# Example 2: s = "rat", t = "car" -> False