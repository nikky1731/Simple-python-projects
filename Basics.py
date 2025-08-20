import sys

#printing a string
print("Hello world") 

#taking input in python
name = input("Enter your name: ")
print("Hello,", name, "! Welcome!")

#printing variables
s = "raj"
print(s)

#printing multiple variables
s = "raj"
y = "lakshmi"
place = "hyderabad"
print(s, y, place)

#to checknsystem version
print(sys.version)

#making variable global
x = "awesome"
def myfunc():
    global x
    x = "fantastic"
myfunc()
print(x)

#format string
z = 9
print(f'hi {z:.2f}')


[print(x) for x in ['apple', 'banana', 'cherry']]

#looping through dictionary 
xx = {'type' : 'fruit', 'name' : 'apple'}
for yy in xx.keys():
  print(yy)

for yy in xx.items():
  print(yy)


#to copy a tuple 
yx = xx.copy()
print(yx)