from typing import List
from collections import defaultdict
import string


def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    paragraph_table = paragraph.maketrans(string.punctuation, ' ' * len(string.punctuation))

    paragraph = paragraph.translate(paragraph_table) 

    word_list = [word.lower() for word in paragraph.split()]

    count_dict = defaultdict(int)

    for word in word_list:
        if word not in banned: 
            count_dict[word] += 1

    return sorted(count_dict.items(), key=lambda item: item[1], reverse=True)[0][0]
    

paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]

print(mostCommonWord(paragraph, banned))