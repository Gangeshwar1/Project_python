def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
x = input ("Enter a number ")
x = int(x)
print(mydoubler(x))