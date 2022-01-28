def multiply_with_loop_bad_function(x, y):
    return sum(y for _ in range(x))

def multiply_with_loop_better_function(x, y):
    if (x > 0 and y > 0) or (x < 0 and y < 0):
        return sum(abs(y) for _ in range(abs(x)))
    elif x < 0 and y > 0:
        return sum(x for _ in range(y))
    elif y < 0 and x > 0:
        return sum(y for _ in range(x))
    else:
        return 0