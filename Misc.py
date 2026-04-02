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


# Optimal: O(n) time, O(1) space (26 letters max)
def is_anagram_optimal(s, t):
    if len(s) != len(t):
        return False
    from collections import Counter
    return Counter(s) == Counter(t)

# Tests
print(is_anagram("anagram", "nagaram"))  # True
print(is_anagram("rat", "car"))          # False
print(is_anagram("", ""))                # True (edge case)
print(is_anagram("a", "ab"))             # False (different lengths)


print("Problem 2: Is Anagram (LeetCode #2)**")
print("----************************----")
print("----************************----")


# I am looking at time/intervals that overlap. 
# With the last merged one,extend it, if not,
# add the curremt interval as a new entry
# 
# I want to compair with a stored interval once I see 
# they overlap I will ad the ends and removed the start
# 
# #/
# Example = [[1,3],[2,6],[8,10],[15,18]]

# def merge_intervals(timelist):
#     New_Arry = []
#     for i in range(len(timelist)):
#         timelist[i] : New_Arry[i]

# print(Merge_Intervals(Example))

def merge_intervals(intervals):
    # Step 1: Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    result = []
    
    for interval in intervals:
        # If result is empty OR no overlap with last merged interval
        if not result or interval[0] > result[-1][1]:
            # Add as new entry
            result.append(interval)
        else:
            # They overlap — extend the end of the last entry
            result[-1][1] = max(result[-1][1], interval[1])
    
    return result

print(merge_intervals([[1,4],[4,5]]))        # [[1,5]] — touching edges merge
print(merge_intervals([[1,4],[2,3]]))        # [[1,4]] — one fully inside another
print(merge_intervals([]))                    # []      — empty input
print(merge_intervals([[5,7],[1,3],[2,6]]))  # [[1,7]] — unsorted input

print("Problem 3: Imerge intervals (LeetCode #3)**")
print("----************************----")
print("----************************----")

# Given an integer array `nums`, return an array where `answer[i]` is the product of all elements in `nums` except `nums[i]`.

# You must solve it **without using division**.
# ```
# Example: [1, 2, 3, 4] -> [24, 12, 8, 6]

# Explanation:
# answer[0] = 2 * 3 * 4 = 24
# answer[1] = 1 * 3 * 4 = 12
# answer[2] = 1 * 2 * 4 = 8
# answer[3] = 1 * 2 * 3 = 6
nums_array = [1, 2, 3, 4]

# def product_array(nums):
#     result = []
#     for num in range(len(nums)):
#         result.append((nums[--num] * nums[++num]) * nums[++num])    
#     return result
# print(product_array(nums_array))

def product_except_self(nums):
    n = len(nums)
    result = [1] * n
    
    # Left pass: build up product from the left
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]  # accumulate for the NEXT index
    
    # Right pass: multiply in product from the right
    right_product = 1
    for i in range(n - 1, -1, -1):  # loop backwards
        result[i] *= right_product
        right_product *= nums[i]
    
    return result
print(product_except_self(nums_array))
print("**Problem 4: Product of Array Except Self (LeetCode #238)**")
print("----************************----")
print("----************************----")