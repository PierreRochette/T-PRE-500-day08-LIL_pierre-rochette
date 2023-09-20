import matplotlib.pyplot as plt

arr = [[0,1], [1, 2], [2, 4]]
x = []
y = []

for sublist in arr : 
    x.append(sublist[0])
    y.append(sublist[1])


print(arr)
print(x)
print(y)


arr2 = [(0,1),(1, 2),(2, 4),(4,6)]
x2 = []
y2 = []

for tup in arr2 : 
    x2.append(tup[0])
    y2.append(tup[1])

print(arr2)
print(x2)
print(y2)
