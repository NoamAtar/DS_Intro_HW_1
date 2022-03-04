def my_func(x1, x2, x3):
    denominator = (x1 + x2 + x3)
    if type(x1) != float or type(x2) != float or type(x3) != float:
        return ('Error: parameters should be float')
    if (denominator == 0):
        return ('Not a number – denominator equals zero')

    result = ((x1 + x2 + x3) * (x2 + x3) * x3) / denominator
    return (result)


print(my_func(10.0, -2.0, 1.0))


# B
def convert(hours, minutes=0):
    try:
        hours = float(hours)
        minutes = float(minutes)
    except:
        return ('Input error!')
    if (hours < 0 or minutes < 0):
        return ('Input error!')

    x = int(hours * 3600 + minutes * 60)
    return (x)


print(convert(1, 3))
print(convert(1.75))
