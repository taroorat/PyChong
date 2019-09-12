# a=(i*2 for i in range(10))
# print(next(a))
# print(next(a))
# print(next(a))
# print(a.__next__())
def Fun(n):
    a=0
    b=1
    while(n> 0):
        n=n-1
        a, b=b,b+a
        yield a
        # print(a)
a=Fun(100)
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
