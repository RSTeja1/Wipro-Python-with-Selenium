#3)
colors = ['red', 'green', 'blue']

for index, value in enumerate(colors, start=1):
    print(index, value)

#5)
nums = [10, 20, 30, 40, 50, 60]

for index, value in enumerate(nums):
    if value == 50:
        print(index)

#8)
items = ['a', 'b', 'c']
for i in enumerate(items):
    print(i)

#2)
for i, v in enumerate([10, 20, 30]):
    print(i, v)

#1)
result = list(enumerate(['a', 'b', 'c']))
print(result)

#4)
result = list(enumerate("PYTHON", start=1))
print(result)

#6
for i, n in enumerate(range(10, 60, 10)):
    print(i, n)

#10)
for i, v in enumerate([100, 200, 300], start=-1):
    print(i, v)

#11)       7 and 12 pending
for i, v in enumerate(['x', 'y', 'z']):
    print(i)





