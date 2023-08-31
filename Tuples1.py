#Change tuple value
fruits = ("Apple", "Mango", "Orange", "Grapes")
print(fruits)
change = list(fruits)
change[1] = "Kiwi"
fruits = tuple(change)
print(fruits)

#Add items
info = ("Name", "Age", "City", "Gender")
print(info)
Detail = list(info)
Detail.append("Location")
info = tuple(Detail)
print(info)

#Add tuple to tuples
Books1 = ("Book1", "Book2", "Book3", "Book4")
print(Books1)
Book2 = ("Book5", "Book6")
Book3 = Books1 + Book2
print(Book3)

#Remove items in tuple
info = ("Steve", 23, "Student", "Bangalore")
print(info)
Info1 = list(info)
Info1.remove("Steve")
print(Info1)

#Delete tuples
City = ("Bangalore", "Mumbai", "Delhi", "UP")
print(City)
del(City)
#print(City)  #This will raise an error

#Packing tuples
tuples = ("Words", "Letters", "Numbers")
print(tuples)

#Unpacking tuples
tuples = ("Words", "Letters", "Numbers")
(Item1 , Item2 , Item3) = tuples
print(Item1)
print(Item2)
print(Item3)

#Using Asterisk*
Place = ("Bangalore", "Mumbai", "Delhi", "UP", "Noida")
(place1, *place2, place3) = Place
print(place1)
print(place2)
print(place3)

#join tuple
tuple1 = ("a", "b", "c", "d")
tuple2 = (2,4,1,3)
tuple3 = tuple1 + tuple2
print(tuple3)

#Multiply tuples
tuples = ("Words", "Letter", "Numbers")
tuples = tuples*2
print(tuples)

#Modifying tuples
dimensions = (200, 50)
print("This is original dimensions.")
for dimension in dimensions:
    print(dimension)

dimensions = (100, 20)
print("This is modified dimensions.")
for dimension in dimensions:
    print(dimension)     


buffet = ("Cake", "Icecream", "Dal", "Rice", "Chappti")
print("You can choose the items form the buffet.")
for items in buffet:
    print(items)    


buffet = ("Cake", "Icecream", "Dal", "Sambar", "Sabji")
print("\nNew items have been added.")
print("You can now choose new items.")
for items in  buffet:
    print(items)


        
