def Division(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return "Numbers can not divided by 0"
