def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if int(str_number[0]) != 0:
        first = int(str_number[0])
    else:
        first =1
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first
result = get_multiplied_digits(4020)
print(result)
