s = 'AABAAB'
# answer : 0,3 so 2 deletions


def alternatingCharacters(s):
    # Write your code here
    prev_char = None
    del_chars = []
    for count, char in enumerate(s):
        if char == prev_char:
            del_chars += [count-1]
        else:
            prev_char = char
    return len(del_chars)

print(alternatingCharacters(s))


# You are given a string containing characters and

# only. Your task is to change it into a string such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.

# Your task is to find the minimum number of required deletions.
