#lambda functions - anonyms (nameless)functions, one line, simple operations
from functools import reduce


#syntax lambda arguments: expressions
#it can have any number of arguments
#must have only one expression
#the expression is automatically returned
#function - function name,arguments,return type, code

#normal function add 2 numbers

def add(a,b):
    return a+b

print(add(5,3))

#lambda function

add=lambda a,b:a+b
print(add(5,3))

#square of number
square = lambda x:x*x
print(square(5))

#check odd or even
even = lambda x: x % 2


#find the maximum of 2 numbers
max= lambda a,b: a if a>b else b
print(max(10,30))

#filter, map and reduce in built in functions in lambda
#filter
#map
#reduce

numbers=[1,2,3,4,5,6]

evens = list(filter(lambda x:x%2 == 0, numbers))
print(evens)

#filter the failed
status=['Pass','Fail','Pass','Fail']

failed = list(filter(lambda s:s == 'Fail',status))
print(failed)

#positive
nums = [-5, 10, -3, 7, 0, 2]
positive_nums = list(filter(lambda x: x > 0, nums))
print(positive_nums)

#non empty
data = ["hello", "", "world", "", "python"]
non_empty = list(filter(lambda x: x != "", data))
print(non_empty)

#reduce

num =[10,20,30,40]
print(reduce(lambda x ,y: x+y,num))

#multiply,max,min
#multiply
print(reduce(lambda x ,y: x*y,num))
#max
print(reduce(lambda x, y: x if x > y else y, num))
#min
print(reduce(lambda x, y: x if x < y else y, num))
#squares
nums=[10,20,30,40]
squares = list (map(lambda x : x*x, nums))
print(squares)

#sorting in lambda
data = [(1,3),(4,1),(2,2)]
sorteddata = sorted(data, key=lambda x:x[1])
print(sorteddata)

marks = {"A":75,"B":90,"C":60}
sorted_marks = dict(sorted(marks.items(), key=lambda x: x[1]))
print(sorted_marks)









