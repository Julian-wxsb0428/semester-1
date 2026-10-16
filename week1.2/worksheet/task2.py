# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers
print("Enter some numbers, separated by spaces:")
numbers=read_numbers()
if len(numbers)==0:
    sys.exit("Error: No numbers provided")
minimum=min(numbers)
maximum=max(numbers)
mean=sum(numbers)/len(numbers)

numbers.sort()
n=len(numbers)
middle=n//2
if n%2==1:
    median=numbers[middle]
else:
    median=(numbers[middle-1]+numbers[middle])/2
print(f"Minimum= {minimum}")
print(f"Maximum= {maximum}")
print(f"Mean= {mean}")
print(f"Median= {median}")
