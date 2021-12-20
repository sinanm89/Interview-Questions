# 1234
# one thousand two hunderd thirty four

def write_numbers(inp_n):
    if not str(inp_n).isnumeric():
        return False

    numbers_dict = {
        '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
        '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten',
        '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen',
        '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen',
        '19': 'nineteen', '20': 'twenty',
       '30': 'thirty', '40': 'forty', '50': 'fifty', '60': 'sixty',
        '70': 'seventy', '80': 'eighty', '90': 'ninety',
        '100': 'hundred', '1000': 'thousand',
        '1000000': 'million', '1000000000': 'billion'
    }
    input_str = str(inp_n)
    index_n = 0
    output = ''
    while index_n < len(input_str):
        char = input_str[index_n]
        p_multiplier = len(input_str) - index_n
        place_value = 10 ** (p_multiplier - 1)

        if numbers_dict.get(char):
            if place_value > 10:
                if p_multiplier % 6 == 5 or p_multiplier % 6 == 2:

                    p_val = numbers_dict.get(input_str[index_n :index_n +2])
                    if p_val:
                        output += ' ' + p_val + (numbers_dict.get(str(place_value)) or '')
                        # eleven
                        place_value = 10 ** (p_multiplier - 2)
                        output += ' ' + numbers_dict.get(str(place_value))
                        # thousand
                        index_n += 2
                        continue

                output += ' ' + numbers_dict.get(char)
                if p_multiplier % 3 == 0:
                    output += ' hundred'
                else:
                    output += ' ' + (numbers_dict.get(str(place_value)) or '')

            elif place_value == 10:
                if numbers_dict.get(char + input_str[index_n+1]):
                    output += ' ' + numbers_dict.get(char + input_str[index_n+1])
                    break
                else:
                    output += ' ' + numbers_dict.get(char+'0')
            elif place_value < 10:
                output += ' ' + numbers_dict.get(char)

        index_n += 1
    return output



print(write_numbers(1234))
print(write_numbers(10000))

print(write_numbers(1010))
print(write_numbers(1011))
print(write_numbers(1034))
print(write_numbers(1410310234))


# 12million 330 112

# 11 444
