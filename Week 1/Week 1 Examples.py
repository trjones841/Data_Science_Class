# The Python Programming Language: Functions

# add_numbers is a function that takes two numbers and adds them together.
def add_numbers(x, y):
    return x + y

print(add_numbers(1, 2))

# add_numbers updated to take an optional 3rd parameter. Using print allows printing of
# multiple expressions within a single cell.
def add_numbers(x, y, z=None):
    if (z == None):
        return x + y
    else:
        return x + y + z

print(add_numbers(1, 2))
print(add_numbers(1, 2, 3))


# add_numbers updated to take an optional flag parameter.
def add_numbers(x, y, z=None, flag=False):
    if (flag):
        print('Flag is true!')
    if (z == None):
        return x + y
    else:
        return x + y + z

print(add_numbers(1, 2, flag=True))

# Assign function add_numbers to variable a.
def add_numbers(x, y):
    return x + y

a = add_numbers
a(1, 2)

# The Python Programming Language: Types and Sequences

# Use type to return the object's type.

type('This is a string')
type(None)
type(1)
type(1.0)
type(add_numbers)

# Tuples are an immutable data structure (cannot be altered).
x = (1, 'a', 2, 'b')
type(x)

# Lists are a mutable data structure.
x = [1, 'a', 2, 'b']
type(x)

# Use append to append an object to a list.
x.append(3.3)
print(x)

# This is an example of how to loop through each item in the list.
for item in x:
    print(item)

# Or using the indexing operator:
i = 0
while (i != len(x)):
    print(x[i])
    i = i + 1

# Use + to concatenate lists.
[1, 2] + [3, 4]

# Use * to repeat lists.
[1] * 3

# Use the in operator to check if something is inside a list.
1 in [1, 2, 3]

# Now let's look at strings. Use bracket notation to slice a string.
x = 'This is a string'
print(x[0])  # first character
print(x[0:1])  # first character, but we have explicitly set the end character
print(x[0:2])  # first two characters

# This will return the last element of the string.
print(x[-1])

# This will return the slice starting from the 4th element from the end and stopping
# before the 2nd element from the end.
print(x[-4:-2])

# This is a slice from the beginning of the string and stopping before the 3rd element.
print(x[:3])

# And this is a slice starting from the 4th element of the string and going all the way to the end
print(x[3:])
firstname = 'Christopher'
lastname = 'Brooks'

print(firstname + ' ' + lastname)
print(firstname * 3)
print('Chris' in firstname)

# split returns a list of all the words in a string, or a list split on a specific character.
firstname = 'Christopher Arthur Hansen Brooks'.split(' ')[0]  # [0] selects the first element of the list
lastname = 'Christopher Arthur Hansen Brooks'.split(' ')[-1]  # [-1] selects the last element of the list
print(firstname)
print(lastname)

# Make sure you convert objects to strings before concatenating.
# print('Chris' + 2) #errors for str + int
print('Chris' + str(2))

# Dictionaries associate keys with values.
x = {'Christopher Brooks': 'brooksch@umich.edu', 'Bill Gates': 'billg@microsoft.com'}
x['Christopher Brooks']  # Retrieve a value by using the indexing operator
x['Kevyn Collins-Thompson'] = None
x['Kevyn Collins-Thompson']

# Iterate over all of the keys:
for name in x:
    print(x[name])

# Iterate over all of the values:
for email in x.values():
    print(email)

# Iterate over all of the items in the list:
for name, email in x.items():
    print(name)
    print(email)

# You can unpack a sequence into different variables:
x = ('Christopher', 'Brooks', 'brooksch@umich.edu')
fname, lname, email = x
print(fname)
print(lname)

# Make sure the number of values you are unpacking matches the number of variables being assigned.
x = ('Christopher', 'Brooks', 'brooksch@umich.edu', 'Ann Arbor')
fname, lname, email = x

# The Python Programming Language: More on Strings
print('Chris' + 2)
print('Chris' + str(2))

# Python has a built in method for convenient string formatting.
sales_record = {
    'price': 3.24,
    'num_items': 4,
    'person': 'Chris'}

sales_statement = '{} bought {} item(s) at a price of {} each for a total of {}'

print(sales_statement.format(sales_record['person'],
                             sales_record['num_items'],
                             sales_record['price'],
                             sales_record['num_items'] * sales_record['price']))

# Reading and Writing CSV files

# Let's import our datafile mpg.csv, which contains fuel economy data for 234 cars.
# mpg : miles per gallon
# class : car classification
# cty : city mpg
# cyl : # of cylinders
# displ : engine displacement in liters
# drv : f = front-wheel drive, r = rear wheel drive, 4 = 4wd
# fl : fuel (e = ethanol E85, d = diesel, r = regular, p = premium, c = CNG)
# hwy : highway mpg
# manufacturer : automobile manufacturer
# model : model of car
# trans : type of transmission
# year : model year

import csv

# %precision 2

with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))

mpg[:3]  # The first three dictionaries in our list.

# csv.Dictreader has read in each row of our csv file as a dictionary. len shows that our
# list is comprised of 234 dictionaries.
len(mpg)

# keys gives us the column names of our csv.
mpg[0].keys()

# This is how to find the average cty fuel economy across all cars. All values in the
# dictionaries are strings, so we need to convert to float.
sum(float(d['cty']) for d in mpg) / len(mpg)

# Similarly this is how to find the average hwy fuel economy across all cars.
sum(float(d['hwy']) for d in mpg) / len(mpg)

# Use set to return the unique values for the number of cylinders the cars in our dataset have.
cylinders = set(d['cyl'] for d in mpg)
cylinders

# Here's a more complex example where we are grouping the cars by number of cylinder, and
# finding the average cty mpg for each group.
CtyMpgByCyl = []

for c in cylinders:  # iterate over all the cylinder levels
    summpg = 0
    cyltypecount = 0
    for d in mpg:  # iterate over all dictionaries
        if d['cyl'] == c:  # if the cylinder level type matches,
            summpg += float(d['cty'])  # add the cty mpg
            cyltypecount += 1  # increment the count
    CtyMpgByCyl.append((c, summpg / cyltypecount))  # append the tuple ('cylinder', 'avg mpg')

CtyMpgByCyl.sort(key=lambda x: x[0])
CtyMpgByCyl

# Use set to return the unique values for the class types in our dataset.
vehicleclass = set(d['class'] for d in mpg)  # what are the class types
vehicleclass

# And here's an example of how to find the average hwy mpg for each class of vehicle in our dataset.
HwyMpgByClass = []

for t in vehicleclass:  # iterate over all the vehicle classes
    summpg = 0
    vclasscount = 0
    for d in mpg:  # iterate over all dictionaries
        if d['class'] == t:  # if the cylinder amount type matches,
            summpg += float(d['hwy'])  # add the hwy mpg
            vclasscount += 1  # increment the count
    HwyMpgByClass.append((t, summpg / vclasscount))  # append the tuple ('class', 'avg mpg')

HwyMpgByClass.sort(key=lambda x: x[1])
HwyMpgByClass

# The Python Programming Language: Dates and Times
import datetime as dt
import time as tm

# time returns the current time in seconds since the Epoch. (January 1st, 1970)
tm.time()

# Convert the timestamp to datetime.
dtnow = dt.datetime.fromtimestamp(tm.time())
dtnow

# Handy datetime attributes:
dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second  # get year, month, day, etc.from a datetime

# timedelta is a duration expressing the difference between two dates.
delta = dt.timedelta(days=100)  # create a timedelta of 100 days
delta

# date.today returns the current local date.
today = dt.date.today()
today - delta  # the date 100 days ago
today > today - delta  # compare dates


# The Python Programming Language: Objects and map()

# An example of a class in python:
class Person:
    department = 'School of Information'  # a class variable



def set_name(self, new_name):  # a method
    self.name = new_name


def set_location(self, new_location):
    self.location = new_location


person = Person()
person.set_name('Christopher Brooks')
person.set_location('Ann Arbor, MI, USA')
print('{} live in {} and works in the department {}'.format(person.name, person.location, person.department))

# Here's an example of mapping the min function between two lists.
store1 = [10.00, 11.00, 12.34, 2.34]
store2 = [9.00, 11.10, 12.34, 2.01]
cheapest = map(min, store1, store2)
cheapest

# Now let's iterate through the map object to see the values.
for item in cheapest:
    print(item)

# The Python Programming Language: Lambda and List Comprehensions

# Here's an example of lambda that takes in three parameters and adds the first two.
my_function = lambda a, b, c: a + b
my_function(1, 2, 3)

# Let's iterate from 0 to 999 and return the even numbers.
my_list = []
for number in range(0, 1000):
    if number % 2 == 0:
        my_list.append(number)
my_list

# Now the same thing but with list comprehension.
my_list = [number for number in range(0, 1000) if number % 2 == 0]
my_list

# The Python Programming Language: Numerical Python (NumPy)

import numpy as np

# Creating Arrays
# Create a list and convert it to a numpy array
mylist = [1, 2, 3]
x = np.array(mylist)
print(x)

# Or just pass in a list directly
y = np.array([4, 5, 6])
print(y)

# Pass in a list of lists to create a multidimensional array.
m = np.array([[7, 8, 9], [10, 11, 12]])
print(m)

# Use the shape method to find the dimensions of the array. (rows, columns)
print(m.shape)

# arange returns evenly spaced values within a given interval.
n = np.arange(0, 30, 2)  # start at 0 count up by 2, stop before 30
print(n)

# reshape returns an array with the same data with a new shape.
n = n.reshape(3, 5) # reshape array to be 3x5
print(n)

# linspace returns evenly spaced numbers over a specified interval.
o = np.linspace(0, 4, 9) # return 9 evenly spaced values from 0 to 4
print(o)

# resize changes the shape and size of array in-place.
o.resize(3, 3)
print(o)

# ones returns a new array of given shape and type, filled with ones.
np.ones((3, 2))

# zeros returns a new array of given shape and type, filled with zeros.
np.zeros((2, 3))

# eye returns a 2-D array with ones on the diagonal and zeros elsewhere.
np.eye(3)

# diag extracts a diagonal or constructs a diagonal array.
np.diag(y)

# Create an array using repeating list (or see np.tile)
np.array([1, 2, 3] * 3)

# Repeat elements of an array using repeat.
np.repeat([1, 2, 3], 3)

# Combining Arrays
p = np.ones([2, 3], int)
print(p)

# Use vstack to stack arrays in sequence vertically (row wise).
np.vstack([p, 2 * p])

# Use hstack to stack arrays in sequence horizontally (column wise).
np.hstack([p, 2 * p])

# Operations
# Use +, -, *, / and ** to perform element wise addition, subtraction, multiplication, division and power.
print(x + y)  # elementwise addition     [1 2 3] + [4 5 6] = [5  7  9]
print(x - y)  # elementwise subtraction  [1 2 3] - [4 5 6] = [-3 -3 -3]
print(x * y)  # elementwise multiplication  [1 2 3] * [4 5 6] = [4  10  18]
print(x / y)  # elementwise divison         [1 2 3] / [4 5 6] = [0.25  0.4  0.5]
print(x ** 2)  # elementwise power  [1 2 3] ^2 =  [1 4 9]

# Dot Product:

# dot product   (X1Y1 + X2Y2 + X3 Y3)
x.dot(y)
z = np.array([y, y ** 2])
print(len(z))  # number of rows of array

# Let's look at transposing arrays. Transposing permutes the dimensions of the array.
z = np.array([y, y ** 2])
z

# The shape of array z is (2,3) before transposing.
z.shape

# Use .T to get the transpose.
z.T

# The number of rows has swapped with the number of columns.
z.T.shape

# Use .dtype to see the data type of the elements in the array.
z.dtype

# Use .astype to cast to a specific type.
z = z.astype('f')
z.dtype

# Math Functions
# Numpy has many built in math functions that can be performed on arrays.
a = np.array([-4, -2, 1, 3, 5])
print(a.sum())
print(a.max())
print(a.min())
print(a.mean())
print(a.std())

# argmax and argmin return the index of the maximum and minimum values in the array.
print(a.argmax())
print(a.argmin())

# Indexing / Slicing
s = np.arange(13) ** 2
print(s)

# Use bracket notation to get the value at a specific index. Remember that indexing starts at 0.
s[0], s[4], s[-1]

# Use : to indicate a range. array[start:stop]

# Leaving start or stop empty will default to the beginning/end of the array.
print(s[1:5])

# Use negatives to count from the back.
print(s[-4:])

# A second : can be used to indicate step-size. array[start:stop:stepsize]

# Here we are starting 5th element from the end, and counting backwards by 2 until the beginning of the array is reached.
print(s[-5::-2])

# Let's look at a multidimensional array.
r = np.arange(36)
r.resize((6, 6))
print(r)

# Use bracket notation to slice: array[row, column]
print(r[2, 2])

# And use : to select a range of rows or columns
print(r[3, 3:6])

# Here we are selecting all the rows up to (and not including) row 2, and all the columns
# the columns up to (and not including) the last column.
print(r[:2, :-1])

# This is a slice of the last row, and only every other element.
print(r[-1, ::2])

# We can also perform conditional indexing. Here we are selecting values from the array
# that are greater than 30. (Also see np.where)
print(r[r > 30])

# Here we are assigning all values in the array that are greater than 30 to the value of 30.
r[r > 30] = 30
print(r)

# Copying Data
# Be careful with copying and modifying arrays in NumPy!
# r2 is a slice of r
r2 = r[:3, :3]
print(r2)

# Set this slice's values to zero ([:] selects the entire array)
r2[:] = 0
print(r2)

# r has also been changed!
print(r)

# To avoid this, use r.copy to create a copy that will not affect the original array
r_copy = r.copy()
print(r_copy)

# Now when r_copy is modified, r will not be changed.
r_copy[:] = 10
print(r_copy, '\n')
print(r)

# Iterating Over Arrays
# Let's create a new 4 by 3 array of random numbers 0-9.
test = np.random.randint(0, 10, (4, 3))
print(test)

# Iterate by row:
for row in test:
    print(row)

# Iterate by index:
for i in range(len(test)):
    print(test[i])

# Iterate by row and index:
for i, row in enumerate(test):
    print('row', i, 'is', row)

# Use zip to iterate over multiple iterables.
test2 = test ** 2
print(test2)

for i, j in zip(test, test2):
    print(i, '+', j, '=', i + j)
