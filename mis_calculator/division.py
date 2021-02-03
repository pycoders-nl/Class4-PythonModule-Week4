def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "entry can not be 0"
