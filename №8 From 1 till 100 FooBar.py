def sto():
    for i in range(1, 101):
        if (i % 3) == 0:
            i = 'Foo'
        elif (i % 5) == 0:
            i = 'Bar'
        elif (i % 3) == 0 and (i % 5) == 0:
            i = 'FooBar'
        print(i)


sto()
