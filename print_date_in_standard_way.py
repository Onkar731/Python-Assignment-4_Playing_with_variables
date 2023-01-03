"""
Create three variables and assign current date to them, first variable contains day number,
second variable contains month number, and third number contains year
Write a python script to display date in standard way e.g (29/12/2022)
"""

# creating varibles and initailizing them with current date
day, month, year = 29, 12, 2022

# printing date in standard way 
# We can use keyword argument - sep="/"
print(day, month, year, sep="/")

# either we can use format specifiers
print("%d/%d/%d" %(day, month, year))