#Tuples
Tuples_1 = (5,6,3,6,2)
Tuples_2 = ('Name', 'age', 'height')
print(Tuples_1)
print(Tuples_2)

Info = ('Sam', 21, 'city', 'number', 342)
print(Info)

fruits = ('Apple', 'Banana', 'Mango')
print(fruits)

#Tuples allows duplicate values
info = ('Name', 'Age', 24, 'steve', 'age')
print(info)

#Tuples allow len() function
words = ('String', 'Set', 'tuples', 4)
print(len(words))

# Creating Tuple with one item
language = ("Python",)
print(type(language))  #This is tuple

language = ("Python")
print(type(language))  #This is not tuple


#Tuples items of different data types
type1 = ('True', 'False')
type2 = (1,2,5,4)
type3 = ("python", "java" , 'c')
print(type(type1))
print(type(type2))
print(type(type3))

name = 'python'
print(len(name))

name = ('python',)
print(len(name))


words = tuple(('name','height', 'age', 32,3 ,'true'))
print(type(words))

#Tuples indexing

#positive indexing
Country = ("Spain", 'India','America','Germany')
print(Country[0])
print(Country[3])

info = ('Sama', 23, 'Bangalore', 2001, 'student')
print(info[2])
print(info[0])
print(info[4])

#Negative indexing
country = ('Spain', 'India', 'America', 'Germany')
print(Country[-1])
print(Country[-3])
print(Country[-2])

info = ('Sama', 23, 'Bangalore', 2001, 'student')
print(info[-2])
print(info[-1])
print(info[-4])

#Check item present in tuple
languages = ("Python", "java", "c", "javascript")
print(languages)
print(len(languages))
if "C++" in languages:
    print("C++ is present in languages.")
else:
    print("C++ is not present in languages.")    


Names = ("Sam", 'Rahul',"Steve",'Ram')
if "sky" in Names:
    print("sky is present.")
else:
    print("sky is not present.")  


#Range in tuples
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")          
print(animals[0:5])
print(animals[4:])
print(animals[:-4])
print(animals[-5:])
print(animals[-1:-5])

#manipulating tuples
countries = ("India", "England", "USA", "China", "Russia")
print(countries)
temp = list(countries)
temp.append ("South Africa")
temp.pop(3)
temp[1] = "Pakistan"
countries = tuple(temp)
print(countries)

#Concatinating two tuples
countries1 = ("India", "England", "USA", "China", "Russia")
countries2 = ("Pakistan", "sri lanka", "Austraila")
countries3 = countries1+countries2
print(countries3)


#Unpack tuples
information = ("Steve", 23, "Bangalore")
(name, age, city) = information
print("Name:", name )
print("Age:", age)
print("City:", city)

fauna = ("parrot","dog", "cat", "pig", "horse", "salmon")
(bird, *animal, fish) = fauna
print("Animals:", animals)
print("Bird:", bird)
print("Fish:" , fish)


numbers = (1,3,4,5,6,7,8,9,10,2)
(first,*rest,last) = numbers
print("First:", first)
print("Last:" ,last)
print("Rest:" ,rest)


