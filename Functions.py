#Defining a functions
def greet_user():
    print("Hello")
greet_user()    

def my_function():
    print("Hello from a function")
my_function()

def fun():
    print("Welcome to python")
fun()        

def name(fname):
    print("Hello,",fname)
name("sam") 
name("Sky")

def greet_user(Name):
    print("Hello", Name)
greet_user("Sam")    

def info(Name,Age,City):
    print("Name:", Name)
    print("Age:" ,Age)
    print("City:" , City)
info("Sky",23,"Bangalore")    
info("Steve",25,"Delhi")

#Passing information to the function      
def message(Username):
    print("Hello, " + Username.upper() + ".")    
message("Jessi")   

def info(Name, Age, City, Occupation):
    print("Hello, my name is " + Name + " and my age is " + str(Age) + " i leave in " + City + " and my occupation is " + Occupation + '.')
info("Subhash", 22, "Bangalore", "Student")
info('Sky',23,"bangalorer","student")

def display_message():
    message = "I am learning to store code in function."
    print(message)
display_message()  

def favorite_book(Title):
    message = "One of my favourite book is alice in wonderland."
    print(message)
favorite_book("Alice in wonderland")    

def favorite_book(title):
    print(title + " is one of my favorite_book.")
favorite_book('Alice in wonderland')   

def favorite_book(Title):
    print(Title + " is my favourite book.")
favorite_book("Caption cool")    


def message( August):
    date = ("What is on August 15th : "+ August)
    print(date)
message("Independace day")    

def information(Name,Age,Course,City):
    message = ("This is my profile.")
    print(message)
    print("Name:", Name)
    print("Age :", Age)
    print("Course :" , Course)
    print("City: ", City)
information("Subhash", 12, 'BCA', 'Bangalore')    


def info (Birthday):
    message = ("My birthday is on" + Birthday)
    print(message)
info(" 1Oth March.")    
    

def disply_message():
    message = 'I am learning python.'
    print(message)
display_message()    

def favourite_book(title):
    print(title + "s my favourite book.")
favorite_book("Alice in the wonderland,")       

#Positional Arguments
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + '.')
    print("My " + animal_type + "'s name is " + pet_name + '.')
describe_pet('Horse', "Jazz")   


def cities_visited(India,America):
    print("Cities visited most of times.")
    print(India + " is the silicon vally\n" + America + " is the silicon vally.")
    print("India:", India)
    print("America:", America)
cities_visited("Bangalore", "Time square")    

#Multiple functions calls
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + '.')
    print("My " + animal_type + "'s name is " + pet_name + '.')
describe_pet('Horse', "Jazz")   
describe_pet('Dog','Harrish') 
describe_pet('Cat', 'Meow')


def information(Name,Age,City,Occupation):
    print("\nMy name is " , Name + "," , "and i am " , Age , "year old" +".")
    print("I live in " + City + " and i am " + Occupation+ ".")
information("Subhash", 23, "Bangalore","Student")    

#Order matters in positional arguments
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + '.')
    print("My " + animal_type + "'s name is " + pet_name + '.')
describe_pet('Jazz', "Horse")

#Keyword arguments
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + '.')
    print("My " + animal_type + "'s name is " + pet_name + '.')
describe_pet(animal_type='Horse',pet_name= "Jazz")

def states(Bangalore,Tamil_nadu):
    print("\nBangalore capital is :" + Bangalore + '.')
    print("Tamil nadu capital is : " + Tamil_nadu + '.')
states(Bangalore= "Karnataka", Tamil_nadu= "Chennai")   


#Default values
def describe_pet(animal_type, pet_name="jazz"):
    print("\nI have a " + animal_type + '.')
    print("My " + animal_type + "'s name is " + pet_name + '.')
describe_pet(animal_type='Horse')


#Exercise
def make_shirt(Size, Text):
    print("\nThe shirt you have selected, the size is ", Size , '.')
    print("Message: " + Text + ".")
make_shirt(45, " Belive yourself")
make_shirt(Size = "Large", Text= "Belive yourself")


def make_shirt(Size ="Small", Text = "I love python"):
    print("\nI am going to make it " + Size + '.')
    print("It will say: " + Text + '.' )
make_shirt()
make_shirt("Large", "Belive yourself")
make_shirt(Size = "Medium") 

def describe_city(city, country='chile'):
 msg = (city.title()) +" is in " +(country.title()) +"."
 print(msg)
describe_city('santiago')
describe_city('reykjavik', 'iceland')
describe_city('punta arenas')
                
    
