""" contiguous sequence of elements 
        - strings
        - arrays
        - linked list
    problems involving finding 
        - min
        - max
        - longest
        - shortest
        - contains

    types of problems
    1. fixed length
        max sum subarray of a fixed size k
    2. dynamic variant
        smallest subarray whose sum is >= s
    3. dynamic variant with auxillary data structure
        longest substring with k distinct characters
"""


""" 1. Find the max sum subarray of a fixed size k

    Example input:
    arr = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
    k = 3

    Example output:
    16
"""
from typing import List

def maxSumSubArray(arr: List[int], k: int) -> int:
    maxValue = -1
    currentRunningSum = 0

    for i in range(len(arr)):
        currentRunningSum += arr[i]
        if i >= k - 1:
            maxValue = max(maxValue, currentRunningSum)
            currentRunningSum -= arr[i - (k - 1)]
    
    return maxValue


""" 2. Find the smallest subarray whose sum is >= s

    Example input:
    arr = [4, 2, 2, 7, 8, 1, 2, 8, 10]
    targetSum = 8

    Example output:
    1
"""
def smallestSubarray(arr: List[int], targetSum: int) -> int:
    minWindowSize = len(arr)
    currentWindowSum = 0
    windowStart = 0

    for windowEnd in range(len(arr)):
        currentWindowSum += arr[windowEnd]

        while currentWindowSum >= targetSum:
            minWindowSize = min(minWindowSize, windowEnd - windowStart + 1)
            currentWindowSum -= arr[windowStart]
            windowStart += 1
    
    return minWindowSize


""" 3. longest substring with k distinct characters

    Example input:
    arr = ['A', 'A', 'A', 'H', 'H', 'I', 'B', 'C']
    k = 2

    Example output:
    5
"""
from collections import defaultdict

def longestSubstringKDistinct(arr: List[int], k: int) -> int:
    hashmap = defaultdict(int)
    maxLength = 0
    windowStart = 0

    for windowEnd in range(len(arr)):
        rightChar = arr[windowEnd]
        hashmap[rightChar] += 1

        while len(hashmap) > k:
            leftChart = arr[windowStart]
            hashmap[leftChart] -= 1
            if hashmap[leftChart] == 0:
                hashmap.pop(leftChart)

            windowStart += 1

        maxLength = max(maxLength, windowEnd - windowStart + 1)
    
    return maxLength

