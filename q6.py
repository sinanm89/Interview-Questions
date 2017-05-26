inp_arr =  [1,2,3,-4,5,-6]
inp_arr =  [-2,1,3,5]
front = 0
back = len(inp_arr) - 1
output = []
while front <= back:
    f_sqrt = inp_arr[front] * inp_arr[front]
    b_sqrt = inp_arr[back] * inp_arr[back]

    if f_sqrt <= b_sqrt:
        output.insert(0, b_sqrt)
        back -= 1
    else:
        output.insert(0, f_sqrt)
        front += 1

print output
