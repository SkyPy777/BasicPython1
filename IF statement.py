cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
  if car == 'bmw':
    print(car.upper())
  else:
    print(car.title()) 

numbers = ['1','4','6','0']
if numbers == '5':
    print('5 is present')
else:
    print('5 is not present')   


x = 10
if x > 5:
    print('x is greater than 5')
else:
    print('x is not greater than 5')        


    x = 50
if x > 100:
    print('x is greater than 100')
else:
    print('x is not greater than 100')        

#check for equality

a = 'Alice'
b = 'Bob'
if a == b:
   print('both a and b are same')
else:
   print('both a and b are different')


list1 = [1, 2, 3]
list1 = [1, 2, 3]

if list1 is list1:
    print("Both lists are the same object")
else:
    print("The lists are different objects")


string1 = "Hello"
string2 = "hello"

if string1.lower() == string2.lower():
    print("The strings are equal, ignoring case")
else:
    print("The strings are not equal")


string1 = "Café"
string2 = "café"

if string1.casefold() == string2.casefold():
    print("The strings are equal, ignoring case")
else:
    print("The strings are not equal")



name1 = 'Roy'
name2 = 'roy'
if name1.lower()==name2.lower():
    print('the strings are equal')
else:
    print('the strings are not equal ')    


requested_toppings = ' Mushroom'
if requested_toppings != 'Capsicum':
    print('hold the capsicum')


#numarical comparison
x = 10
y = 5

if x > y:
    print("x is greater than y")
else:
    print("y is less then x")    

if x < y:
    print("x is less than y")
else:
    print("x is greater then y")    

if x >= y:
    print("x is greater than or equal to y")


if x <= y:
    print("x is less than or equal to y")

if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")

if x != y:
    print("x is not equal to y")


a = 15
b = 20
c = 10

if a > b and a > c:
    print("a is the greatest")

if b > a or b > c:
    print("b is greater than at least one of the other two")
