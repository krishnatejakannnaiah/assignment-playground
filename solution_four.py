# Qnance
# 4. Given two string s1 and s2. Determine if s2 has all the character
# present in s1.

# Example 1:
# S1 = “aabccd”
# S2 = “abcd”

# Output = true

# Example 2:
# S1 = “aabbw”
# S2 = “abc”

# Output = false

def has_all_characters(s1, s2):
    set_s1 = set(s1)
    set_s2 = set(s2)
    
    return set_s1.issubset(set_s2)

# solution for Example 1
S1_1 = "aabccd"
S2_1 = "abcd"
print(has_all_characters(S1_1, S2_1))

# solution for Example 2
S1_2 = "aabbw"
S2_2 = "abc"
print(has_all_characters(S1_2, S2_2))


# custom test solution
S1_3 = "aaabbwdad"
S2_3 = "aabbwdd"
print(has_all_characters(S1_3, S2_3))

