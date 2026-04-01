message = "Hello, World!"
print(message)

def two_sum(nums, target):
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] + nums[y] == target:
                return [x, y]
    return None
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))
# for x in range(len(nums)):
#     for y in range(x + 1, len(nums)):
#         if nums[x] + nums[y] == target:
#             print([x, y])
print("Problem 1: Two Sum (LeetCode #1)**")
print("----************************----")
print("----************************----")
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

#/
# First, what is an Anagram? An anagram is a word or phrase formed by
# rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once. For example, 
# "listen" and "silent" are anagrams of each other.
# 
# I need to find a way to check if two strings are anagrams of each other.
# One approach is to sort the characters in both strings and compare them.
# If they are equal after sorting, then they are anagrams.
# 
# Let's implement this approach. 

# def is_anagram(s, t):
#     return sorted(s) == sorted(t)
def is_anagram(s, t):
    return sorted(s) == sorted(t) 

s = "anagram"
t = "nagaram" #-> True
x = "rat"
y = "car" #-> False
print(is_anagram(s, t))
print("Problem 2: Is Anagram (LeetCode #2)**")
print("----************************----")
print("----************************----")