# Qnance
# 2. Provided a list consisting of string S, group the string on basis of
# anagram. Two strings are considered Anagram if rearranging the letters
# of one string will result into the other string typically using all the
# original letters exactly once.

# Constraints:
# 1. Length of the input strings will be in range [1, 10]
# 2. Sum of length of all strings will not exceed 10000 for any test case.

from collections import defaultdict

def group_anagrams(S):
    total_length = sum(len(string) for string in S)
    if total_length > 10000:
        print("Sum of lengths of all strings exceeds 10000") # Sum of length of all strings will not exceed 10000 for any test case.
        return []

    for string in S:
        if len(string) > 10:
            print(f"Length of string '{string}' exceeds the length 10") # Length of the input strings will be in range [1, 10]
            return []

    anagram_groups = defaultdict(list)
    
    for string in S:
        char_count = [0] * 26
        for char in string:
            char_count[ord(char) - ord('a')] += 1
        key = tuple(char_count)
        anagram_groups[key].append(string)
    
    return list(anagram_groups.values())

# Change input here
S = ["eat", "tea", "tan", "ate", "nat", "bat", ]
print(group_anagrams(S))

