#looping
user = {
    'Name': 'Sky',
    'Age' : '23',
    'City': 'Bangalore'

}

for key, value in user.items():
    print('\nkey:' + key)
    print('Value:' + value)


Dict = {
    'A' : 12,
    'B' : 10,
    'C' : 29,
    'D' : 30,
}    
for key in Dict.keys():
    print(key)
for value in Dict.values():
    print(value)
for key,value in Dict.items():
    print('\nkey:' + key)
    print('value:' + str(value))


#Favourite language
Favourite_languages = {
    'Mike' : 'Python',
    'Soni' : 'C',
    'Steve' : 'C++',
    'John' : 'Java',
}    

for Names , Languages in Favourite_languages.items():
    print(Names.title()+ "'s Favourite languages is " + Languages.title() + '.')


#Looping keys in dictionary
Favourite_languages = {
    'Mike' : 'Python',
    'Soni' : 'C',
    'Steve' : 'C++',
    'John' : 'Java',
}    

for name in Favourite_languages.keys():
    print(name)

#Looping through all the keys in dictionary   
Favourite_languages = {
    'Mike' : 'Python',
    'Soni' : 'C',
    'Steve' : 'C++',
    'John' : 'Java', 
}
friends = ['Soni', 'John']
for friends in Favourite_languages.keys():
    print(friends.title())

    if friends in friends:
        print('  Hi, ' + friends.title() + 'I see your Favourite languages is ' + Languages.title() )

#Keys in  order #Sorted()
Favourite_languages = {
    'Mike' : 'Python',
    'Soni' : 'C',
    'Steve' : 'C++',
    'John' : 'Java',
}
for name in sorted(Favourite_languages.keys()):
    if name in Favourite_languages:
        print(name.title() + ', thankyou for taking the pool' +'.')


Glossary = {
    'String': 'A series of characters.',
    'Comment': 'A note in a program that the Python interpreter ignores.',
    'List': 'A collection of items in a particular order.',
    'Loop': 'Work through a collection of items, one at a time.',
    'Dictionary': "A collection of key-value pairs.",
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.',
  }

for words, meaning in Glossary.items():
    print(f"\n{words.title()}: {meaning}")



rivers = {
 'nile': 'egypt',
 'mississippi': 'united states',
 'fraser': 'canada',
 'kuskokwim': 'alaska',
 'yangtze': 'china',
 }

for river , country in rivers.items():
    print(f"{river.title()}  flows through  {country.title()}" +'.')

print('The set of rivers are: ')
for river in rivers.keys():
    print(river.title())

print('The set of country are: ')
for country in rivers.values():
    print(country.title())    



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

    
