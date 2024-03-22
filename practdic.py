a = [[2,3,4,7,5], [9,8,7,1,4,0], [2,5,8,6,1]]
b = [2,1]

for c in a:
    if all(e in c for e in b):
        a.remove(c)
print(a)