def fib_generator(keep=None):
    a = 1
    b = 1
    c = 2
    keep.append(1)
    yield 1
    keep.append(1)
    yield 1
    keep.append(2)
    yield 2
    while True:
        a = b
        b = c
        c = a + b
        keep.append(c)
        yield c

i = 1
for n in fib_generator():
    if len(str(n)) == 1000:
        print(i)
        break
    i = i + 1
