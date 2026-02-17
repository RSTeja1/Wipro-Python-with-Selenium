#first even numbers

nums = [1,2,3,4,5,6]
even_nums = [x for x in nums if x % 2 == 0]
print(even_nums)

#square
squared_nums = list(map(lambda x: x ** 2, nums))
print(squared_nums)

#sum
from functools import reduce

total = reduce(lambda x, y: x + y, nums)
print(total)

#2
salaries = [25000, 40000, 32000, 18000]
high_salaries = list(filter(lambda x: x > 30000, salaries))
print(high_salaries)

#10% hike
hiked_salaries = list(
    map(lambda x: x * 1.10,
        filter(lambda x: x > 30000, salaries))
)

print(hiked_salaries)

#total payout
total_payout = sum(hiked_salaries)
print("Total payout:", total_payout)

#lab 06/01
data = [(1, 3), (4, 1), (2, 2), (5, 0)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)

from datetime import datetime

now = datetime.now()

get_year  = lambda x: x.year
get_month = lambda x: x.month
get_date  = lambda x: x.day
get_time  = lambda x: x.time()

print("Year :", get_year(now))
print("Month:", get_month(now))
print("Date :", get_date(now))
print("Time :", get_time(now))


















