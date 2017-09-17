"""
Reverse the order of the strings.

bill gates

gates bill

setag llib
"""


# def reverse_string(input_string, delimiter):
#     input_string = [i for i in input_string]
#     output_string = ''
#     temp_word = ''
#     while len(input_string) >= 1:
#         last_char = input_string.pop()
#         if last_char:
#             output_string += last_char
#     return output_string

# def main(input_string='sinan midillili'):
#     pp = reverse_string(input_string, ' ')

# if __name__ == "__main__":
#     main()


input_string = 'bill gates'
output = ''
while len(input_string):
    letter = input_string.pop(-1)
    output += letter

[input_string.pop() for letter in input_string]
