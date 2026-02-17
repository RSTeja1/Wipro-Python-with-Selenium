#1
import re

s = "12345"
print(bool(re.fullmatch(r"\d+", s)))

#2
pattern = r"\d{10}"

num = "9876543210"
print(bool(re.fullmatch(pattern, num)))

#3
s = "Hello Python World"
print(re.findall(r"[a-z]", s))

#4
s = "Hello everyone"
print(bool(re.match(r"^Hello", s)))

#5
s = "Hello everyone"
print(bool(re.match(r"^Hello", s)))

#6
s = "Hello world"
print(bool(re.search(r"world$", s)))

#7
s = "Python is very easy"
print(re.findall(r"\w+", s))

#8
pattern = r"^.{5}$"

s = "Hello"
print(bool(re.match(pattern, s)))

#9
s = "python Python python"
print(re.findall(r"python", s))

#10
s = "Python is very easy"
result = re.sub(r"\s+", "_", s)
print(result)






