students = {
    101: "Arun",
    102: "Bala",
    103: "Charan",
    104: "Deepak"
}

print(students)

#5key value pairs
student = {}

for i in range(5):
    key = input("Enter key: ")
    value = input("Enter value: ")
    student[key] = value

print("Dictionary:", student)

#access
student = {
    101: "Arun",
    102: "Bala",
    103: "Charan"
}

# Accessing a key that exists
print("Roll 101:", student[101])

# Accessing a key that does NOT exist (will cause error)
# print(student[105])

# Safe way to access a key that does NOT exist
print("Roll 105:", student.get(105))
print("Roll 106:", student.get(106, "Key not found"))

#update
student.update({103: "Charan Kumar"})
print(student)

#delete
del student[102]
print(student)

#pop
student.pop(103)
print(student)

# Print only keys
print("Keys:")
for key in student.keys():
    print(key)

# Print only values
print("\nValues:")
for value in student.values():
    print(value)

# Print key–value pairs
print("\nKey–Value pairs:")
for key, value in student.items():
    print(key, ":", value)

#labsession 06/02
dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}
result = {**dict1, **dict2, **dict3}
print(result)





