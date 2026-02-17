#dictionary item- key values
#simlar to lists and tuples
#for a integers, tuples and strings - keys must be immutable
#list cannot be used in the key for the dict as it is mutable in nature

country={"India":"Delhi",
         "Canada":"Ottawa",
         "England":"London"}

print(country)

#access the values with keys
print(country["India"])

#add elements
country["Italy"]="Rome"
print(country)

#remove elements
del country["England"]
print(country)

#for a integers, tuples and strings - keys must be immutable
#integer as a key
my_dict= {1:"one",2:"Two",3:"Three"}
print(my_dict)

my_dict= {1:"four",2:"Two",3:"Three",1:"one"}
print(my_dict)

#tuple as a key
my_dict= {(1,2):"one two",3:"Three"}
print(my_dict)

my_dict= {(1,2):"one two",3:"Three",3:"Four"}
print(my_dict)

#length of dictionary
print(len(country))
print(country.keys())
print(country.values())


my_dict ={1:"one", 2:"two",3:"three", 1:"four"}
print(my_dict)

employees=[
    {"id":1,"name":"Surya","role":"QA"},
    {"id":2,"name":"Teja","role":"Developer"},
    {"id":3,"name":"Raju","role":"Testor"}
]
print(employees[0])
print(employees[0]["name"])

for emp in employees:
    print(emp["name"],emp["role"])

employees.append({"id":4,"name":"sita","role":"tester"})
print(employees)

employees.pop(0)
print(employees)




