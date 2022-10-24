from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    dict = {}

    for i, num in enumerate(nums):
        diff = target - num

        if num in dict:
            return [dict[num], i]
        else:
            dict[diff] = i
      

nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))