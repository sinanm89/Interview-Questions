# def palindrome(pal_list):
#     for item in pal_list:
#         # pal_list = pal_list.pop(item)
#         # pop "l"  ['v','e', 'l','e']
#         length_list=len(pal_list)
#         tolerance_count=0

#         if length_list%2==0:
#             if item in pal_list && pal_list.count(item)%2 == 0:
#                 continue
#             else:
#                 return False

#         elif length_list%2==1:
#             if item in pal_lis && pal_list.count(item)%2==0:
#                 continue
#             else:
#                 if tolerance_count > 0:
#                     return False
#                 else:
#                     tolerance_count += 1
#         return True


# INPUT  [a b a c d c]

# OUTPUT False

# Given a list of characters, can you build a palindrome with those? You have to use all the characters.


# Examples:
# IN: [ 'l', 'v', 'e', 'l', 'e' ] # you can build 'level' or 'elvle' with these chars.
# OUT: true

# IN: [ 'a', 'b', 'c', 'd', 'e' ] # no possible palindrome can be build
# OUT: false


# [1, 2, 4, 56, 1, 2]

def find_palindrome(input_string):

# 1,1,2,2,3,3,4
# only one singular letter is allowed if len(input_string) % 2 == 1

has_remainder = len(input_string) % 2
if has_remainder:
    lookup_index -= 1
else:
    lookup_index += 1

middle_count = 0
if has_remainder:
    middle_count = 1


if input_string[i] != input_string[lookup_index]:
    middle_elem += 1

if middle_count && middle_elem > 1:
    return false


def main(input_string):

    # sort array (mergesort/timsort -comparison sort - nlogn)

    # divide the sorted array from the middle and search/compare the pairs

    # nlogn always


























