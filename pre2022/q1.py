input_string = '{A:{B:[1,2,{C:"D"}]},"E":"F"}'
# imported from settings file
delimiters = ['"', ',', ':', '[', ']', '{', '}']


def complete_line(tab_count):
    return '\n' + '\t' * tab_count


def check_delimiter_char_cases(input_char, output, i, str_open, tab_count):
    if input_char == ',':
        output += input_char + complete_line(tab_count)
    elif input_char == '[':
        tab_count += 1
        output += input_char + complete_line(tab_count)
    elif input_char == ']':
        tab_count -= 1
        output += input_char + complete_line(tab_count)
    elif input_char == '{':
        tab_count += 1
        output += input_char + complete_line(tab_count)
    elif input_char == '}':
        tab_count -= 1
        output += input_char + complete_line(tab_count)
    elif input_char == ':':
        if (
            str_open or
            input_string[i + 1] == '"' or
            input_string[i + 1].isdigit()
        ):
            output += output
            return output, str_open, tab_count
        tab_count += 1
        output += input_char + complete_line(tab_count)
    elif input_char == '"':
        str_open = not str_open
        output += input_char
    return output, str_open, tab_count


def main():
    tab_count = 0
    str_open = False
    output = ''
    for i in range(0, len(input_string)):
        input_char = input_string[i]

        if input_char in delimiters:
            output, str_open, tab_count = check_delimiter_char_cases(
                input_char, output, i, str_open, tab_count)
        else:
            output += input_char
    print output

if __name__ == '__main__':
    main()
