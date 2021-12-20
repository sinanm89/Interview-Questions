
def find_max_delta(input_array):
    max_delta = 0
    front = 0
    back = len(input_array) - 1
    while front < back:
        f_delta = abs(input_array[front] - input_array[front+1])
        b_delta = abs(input_array[back] - input_array[back-1])

        if f_delta > max_delta:
            max_delta = f_delta
        if b_delta > max_delta:
            max_delta = b_delta

        front += 1
        back -= 1
    return max_delta


def main():
    input_array = [1, 2, 32, 452, 6, -200, 10, 0]
    output = find_max_delta(input_array)
    print output
