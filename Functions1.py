#Returning a simple value
def get_formatted(First_name, Last_name):
    full_name = First_name + Last_name
    print(full_name)

get_formatted("Steve", "Smith")

def get_formatted(First_name,middle_name, Last_name):
    full_name = First_name + middle_name + Last_name
    print(full_name)

get_formatted("Steve ", "S" , " Smith")

def get_formatted(First_name,Last_name,Middle_name=""):
    if Middle_name: 
     full_name = First_name + Last_name + Middle_name
     print(full_name)
    else:
        full_name=full_name = First_name + Last_name
        print(full_name)
get_formatted("Subhash ", "Kumar ")
get_formatted("Subhash", " Kumar", " Yadav")

 
#Returning a dictionary
def build_person(first_name, last_name):
 person = {'first': first_name, 'last': last_name}
 return person
musician = build_person('jimi', 'hendrix')
print(musician)


def build_person(first_name, last_name, age=""):
   person = {"first": first_name , "last": last_name}
   if age:
      person['age'] = age
   return person
   
person = build_person("Subhash", "Yadav", age=25)
print(person)

def language(First,Second):
   program = {'First': First, "Second": Second}
   return program
coders = language("Python", "Java")
print(coders)
 
def language(first_language,second_language):
   program = {"First": first_language, "second_language": second_language}
   return program
coder = language("Python","Java")
print(coder) 

#Function with a while loop
def get_formated_name(First_name, Last_name):
   full_name = First_name.title() + ' ' + Last_name.title()
   return full_name
while True:
   print("\nPlease enter your name:")
   print("Enter 'Q' at any time to quit")
   f_name = input(" First_name: ")
   if f_name == 'Q':
      break
   l_name = input(" Last_name:")
   if l_name == 'Q': 
      break
   formated_name = get_formated_name(f_name,l_name)
   print("\nHello, " + formated_name + ".")


def city_country(City, Country):
   return  f"{City.title()}, {Country.title()}"

city = city_country("India", "Bangalore")
print(city)
city = city_country("America", "New york")
print(city)
city = city_country("England", "London")
print(city)
city = city_country("Austraila", "Sydeny")
print(city)


def music_album(Artist, Title):
   album = {
      Artist.title(),
      Title.title(),
   }
   return album
Album = music_album("Mettalic", "Sydeny")
print(Album)

Album = music_album("Do not start", "Obbssed")
print(Album)

Album = music_album("GOAT", "Born to shine")
print(Album)

album = music_album("Artist", "Title")
print(album)


