def flatten(l):
    for e in l:
        if hasattr(e,"__iter__"):
            yield from flatten(e)
        else:
            yield e

l = [1,2,3,[4,5,6],8,9]
k = flatten(l)
s = []
for i in k:
    s.append(i)
print(s)




