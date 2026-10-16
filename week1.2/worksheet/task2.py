# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers
numbers=read_numbers()
if len(numbers)==0:
    sys.exit("Error:no number provided")
minimuim=min(numbers)
maximum=max(numbers)
mean=sum(numbers)/len(numbers)

numbers.sort()
n=len(numbers)
middle=n//2
if n%2==1:
    median=numbers[middle]
else:
    median=(numbers[middle-1]+numbers[middle])/2
print(f"Minimum: {minimuim}")
print(f"Maximum: {maximum}")
print(f"Mean: {mean}")
print(f"Median: {median}")
