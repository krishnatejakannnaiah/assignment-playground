# Qnance
# 3. Given a List of characters “R”, “G” and “B”. sort them in such a way
# that all “R”, “G” and “B” will be together, List need to be sorted in
# place.

# Example 1:
# Input = [“R”, “B”, “R”, “G”, “G”, “B”]
# Output = [“R”, “R”, “G”, “G”, “B”, “B”]

# Example 2:
# Input = [“R”, “B”, “R”, “G”]
# Output = [“R”, “R”, “G”, “B”]

def sort_colors(colors):
    red_pointer = 0
    green_pointer = 0
    blue_pointer = len(colors) - 1

    while green_pointer <= blue_pointer:
        if colors[green_pointer] == 'R':
            colors[green_pointer], colors[red_pointer] = colors[red_pointer], colors[green_pointer]
            red_pointer += 1
            green_pointer += 1
        elif colors[green_pointer] == 'G':
            green_pointer += 1
        else:
            colors[green_pointer], colors[blue_pointer] = colors[blue_pointer], colors[green_pointer]
            blue_pointer -= 1
    
    return colors

# solution for Example 1
input1 = ["R", "B", "R", "G", "G", "B"]
print(sort_colors(input1))

# solution for Example 2
input2 = ["R", "B", "R", "G"]
print(sort_colors(input2)) 

# custom test solutions
input3 = ["G", "B", "R", "G"]
print(sort_colors(input3)) 

input4 = [ "B",  "B", "G", "B", "R", "G"]
print(sort_colors(input4)) 