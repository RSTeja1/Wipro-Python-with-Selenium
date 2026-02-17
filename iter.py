#iter() method - built in method
# create a iterator from a iterable

#iterations - looping the collection of items

a=[10,20,30,40,50] #iterable value

#convert the list into a iterator

iterator= iter(a)

#allow the user to access the elements

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

#convert the string to a iterator
s = "hello"
iterator=iter(s)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

d = {'a':1,'b':2,'c':3}
iterator=iter(d)
print(next(iterator))
print(next(iterator))
print(next(iterator))

#for loop iterator

for key in iterator:
    print(key)


d = {'a':1,'b':2,'c':3}
for key, value in d.items():
    print(key,"->",value)

#iter (callable,sentimel)

it = iter(input, "quit")

for value in it:
    print("you entered",value)






