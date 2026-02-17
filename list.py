empyty_list=[]
numbers = [1,2,3,4,0,8,3]
mixeddata = [1,"hello",True, 6.67,1]
nested= [[1,2],[3,4]]

#accessing
print(mixeddata[1])
print(mixeddata[2])

#modifying
mixeddata[4]=6
print(mixeddata)

#modifying the lists
mixeddata.insert(5,10)
print(mixeddata)

#append
mixeddata.append("John")
print(mixeddata)

#remove
mixeddata.remove("hello")
print(mixeddata)
mixeddata.pop()
print(mixeddata)
mixeddata.pop(1)
print(mixeddata)

#list methods
numbers.sort()#ascen
print(numbers)
numbers.reverse()
print(numbers.count(3))
print(numbers.index(3))
print(numbers.clear())


#new
fruits = ["orange","cherry","kiwi"]
for item in fruits:
    print(item)

for i,fruit in enumerate(fruits):
    print(i, fruit)

#slicing
my_list = ['p','q','r','s','t','u']
print("my_list=", my_list)

#get the list
print(my_list[2:5])

#omit
print(my_list[5:])

#from first to last
print(my_list[:])

#extend
numbers = [1,3,5]
even_numbers = [2,4,6]
#adding
numbers.extend(even_numbers)
print(numbers)


#lab HW largest number from list
numbers = input("Enter numbers separated by spaces: ")

num_list = list(map(int, numbers.split()))

largest = num_list[0]
for num in num_list:
    if num > largest:
        largest = num

print("Largest number:", largest)

#remove even number
numbers = input("Enter numbers separated by spaces: ")
num_list = list(map(int, numbers.split()))

odd_numbers = [num for num in num_list if num % 2 != 0]
print("List after removing even numbers:", odd_numbers)

#multiply list itself
numbers = input("Enter numbers separated by spaces: ")
num_list = list(map(int, numbers.split()))

product = 1
for n in num_list:
    product *= n

print(product)








