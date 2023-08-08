
#A simple dictionary
alien_0 = {'color': 'green', 'points': '5'}
print(alien_0['color'])
print(alien_0['points'])

fruits  = {
    'Apple': 5,
    'Banana': 4,
    'Orange': 3
}
print(fruits['Apple'])

#Accessing values in dictionary
alien_0 = {
    'color': 'green',
    'point': 5
}
new_point=(alien_0['point'])
print('You just earned ' + str(new_point) + ' point' + '!')

#Adding new value in dictionary
alien_0 = {
    'color': 'green',
    'points': 5,
}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

fruits = {
    'apple': 6,
    'banana': 4,
    'orange': 2
}
print(fruits)
fruits['mango'] = 6
fruits['kiwi'] = 4
print(fruits)

#starting with an empty dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['point'] = 5
print(alien_0)

#modifying valuse in a dictionary
alien_0 = {'color': 'green'}
print('The alien color is '+ alien_0['color'] + '.')

alien_0['color'] = 'yellow'
print('The alien color is now '+alien_0['color'] + '.')


person = {
 'first_name': 'eric',
 'last_name': 'matthes',
 'age': 43,
 'city': 'sitka',
 }
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])


favorite_numbers = {
 'mandy': 42,
 'micah': 23,
 'gus': 7,
 'hank': 1000_000,
 'maggie': 0,
 }
num = favorite_numbers['mandy']
print(f"Mandy's favorite number is {num}.")
num = favorite_numbers['micah']
print(f"Micah's favorite number is {num}.")
num = favorite_numbers['gus']
print(f"Gus's favorite number is {num}.")
num = favorite_numbers['hank']
print(f"Hank's favorite number is {num}.")
num = favorite_numbers['maggie']
print(f"Maggie's favorite number is {num}.")


glossary = {
 'string': 'A series of characters.',
 'comment': 'A note in a program that the Python interpreter ignores.',
 'list': 'A collection of items in a particular order.',
 'loop': 'Work through a collection of items, one at a time.',
 'dictionary': "A collection of key-value pairs.",
 }
word = 'string'
print(f"\n{word.title()}: {glossary[word]}")
word = 'comment'
print(f"\n{word.title()}: {glossary[word]}")
word = 'list'
print(f"\n{word.title()}: {glossary[word]}")
word = 'loop'
print(f"\n{word.title()}: {glossary[word]}")
word = 'dictionary'
print(f"\n{word.title()}: {glossary[word]}")


glossary = {
 'string': 'A series of characters.',
 'comment': 'A note in a program that the Python interpreter ignores.',
 'list': 'A collection of items in a particular order.',
 'loop': 'Work through a collection of items, one at a time.',
 'dictionary': "A collection of key-value pairs.",
 'key': 'The first item in a key-value pair in a dictionary.',
 'value': 'An item associated with a key in a dictionary.',
 'conditional test': 'A comparison between two values.',
 'float': 'A numerical value with a decimal component.',
 'boolean expression': 'An expression that evaluates to True or False.',
 }
for word, definition in glossary.items():
 print(f"\n{word.title()}: {definition}")


 rivers = {
 'nile': 'egypt',
 'mississippi': 'united states',
 'fraser': 'canada',
 'kuskokwim': 'alaska',
 'yangtze': 'china',
 }
for river, country in rivers.items():
 print(f"The {river.title()} flows through {country.title()}.")
print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
 print(f"- {river.title()}")
print("\nThe following countries are included in this data set:")
for country in rivers.values():
 print(f"- {country.title()}")


 favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for name, language in favorite_languages.items():
 print(f"{name.title()}'s favorite language is {language.title()}.")
print("\n")
coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']
for coder in coders:
 if coder in favorite_languages.keys():
  print(f"Thank you for taking the poll, {coder.title()}!")
else:
 print(f"{coder.title()}, what's your favorite programming language?")


 # Make an empty list to store people in.
people = []
# Define some people, and add them to the list.
person = {
 'first_name': 'eric',
 'last_name': 'matthes',
 'age': 46,
 'city': 'sitka',
 }
people.append(person)
person = {
 'first_name': 'lemmy',
 'last_name': 'matthes',
 'age': 2,
 'city': 'sitka',
}
people.append(person)
person = {
 'first_name': 'willie',
 'last_name': 'matthes',
 'age': 11,
 'city': 'sitka',
 }
people.append(person)
# Display all of the information in the dictionary.
for person in people:
 name = f"{person['first_name'].title()} {person['last_name'].title()}"
 age = person['age']
 city = person['city'].title()
 
 print(f"{name}, of {city}, is {age} years old.")
 