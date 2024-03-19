# Qnance
# 1. Given a positive integer N and a digit D, find out the number of
# occurrences of D from 1 to N.
# Constraints: 1 <= N <= 1e18 0 <= D <= 9

def count_digit_occurrences(N, D):
    count = 0
    for i in range(1, N + 1):
        count += str(i).count(str(D))
    return count

# Input from the user
N = int(input("Enter the value of N: "))
D = int(input("Enter the value of D: "))

print(count_digit_occurrences(N, D))
