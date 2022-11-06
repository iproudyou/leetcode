from typing import List
from collections import defaultdict

def partitionLabels(s: str) -> List[int]:
    charIndices = defaultdict(list)

    # build the hashmap of character indices
    for i in range(len(s)):
        charIndices[s[i]].append(i)

    # partition the string
    prev = -1
    upper_bound = 0
    result = []

    for i in range(len(s)):
        char = s[i]
        char_max = max(charIndices[char])
        upper_bound = max(upper_bound, char_max)

        if i == upper_bound:
            result.append(upper_bound - prev)
            prev = upper_bound

    return result
