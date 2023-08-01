#lists
Bicycles = ['trek', 'cannondale', 'redline', 'Hero', 'Hercules']
print(Bicycles)

#Accessing element in a list
Bicycles = ['trek', 'cannondale', 'redline', 'Hero', 'Hercules']
print(Bicycles[0])

Cars = ['bmw', 'audi', 'benz', 'tata', 'mahindra']
print(Cars)
print(Cars[2])

#Using title() method
Cars = ['bmw', 'audi', 'benz', 'tata', 'mahindra']
print(Cars[2].title())
print(Cars[0].upper())

#Posititons
Languages = ['java','python','c++','c','javascript']
print(Languages[1])
print(Languages[3])

Languages = ['java', 'python','c++','c','javascript']
print(Languages[-1])
print(Languages[-2])
print(Languages[-3])

Languages = ['java', 'python','c++','c','javascript']
message = 'my first programming language was ' + Languages[-4] + '.'
message = '\nmy first programming language was ' + Languages[1] +'.'
print(message + message)

names = ['Rohan', 'Mukesh', 'Rahul', 'Raj']
print(names)
print(names[0])
print(names[1])
print(names[2])
print(names[3])

names = ['Rohan', 'Mukesh', 'Rahul', 'Raj']
message = '\nHello, how are you ' + names[0] +'.'
print(message)
message = 'Hello, how are you ' + names[1] +'.'
print(message)
message = 'Hello, how are you ' + names[2] +'.'
print(message)
message = 'Hello, how are you ' + names[3] +'.'
print(message)

Transportation = ['car','bike','cycle','bus']
print(Transportation)
print('\nI would like to own ' + Transportation[1] + '.')

#changing, adding and removing
countries = ['India','America','China','Russia']  #Changing element
print(countries)
countries[0] = 'Bharat'
print(countries)

#Adding elements
countries = ['India','America','China','Russia']
print(countries)
countries.append('Pakistan')
print(countries)

#Starting with empty list and adding elements
letters = []
letters.append('A')
letters.append('B')
letters.append('C')
print(letters)

#Insert elements
City = ['Bangalore','Delhi','Mumbai','Hyderabad']
print(City)
City.insert(1,'Noida')
print(City)

#Removing an item
laptops = ['Dell','Asus','hp','Lenovo']
print(laptops)
laptops.remove('Asus')
print(laptops)

#Deleting item
Numbers = ['1','3','2','5']
print(Numbers)
del Numbers[3]
print(Numbers)

motorcycle = ['honda','yamaha','suzuki','ducati']
print(motorcycle)
too_expensive = 'ducati'
motorcycle.remove(too_expensive)
print(motorcycle)
print('A '+ too_expensive.title() + ' is to expensive for me' + '.')

guest = ['Rahul', 'Mike', 'Roy']
print(guest)
message = 'Hi '+ guest[0] + ' you are invited for the dinner tonight' + '.'
print(message)
message = 'Hi ' + guest[1] + ' you are invited for the dinner tonight'+ '.'
print(message)
message = 'Hi ' + guest[2] + '  you are invited for the dinner tonight' + '.'
print(message)
print('Sorry, but ' + guest[1] + ' will not attend the dinner tonight'+ '.' )
guest.remove('Mike')
print(guest)
guest.append('Smith')
print(guest)
print('Insted of Mike ' ", " + guest[1] + ' will join the dinner tonight'+ '.' )
print(guest)
print("Hello, there is a big announcement that today's dinner table going to be bigger dinner table"+'.')
guest.insert(0,'Sam')
print(guest)
guest.insert(1,'Steve')
print(guest)
guest.append('Jason')
print(guest)
message = 'Hi '+ guest[0] + ' you are invited for the dinner tonight' + '.'
print(message)
message = 'Hi ' + guest[1] + ' you are invited for the dinner tonight'+ '.'
print(message)
message = 'Hi ' + guest[2] + '  you are invited for the dinner tonight' + '.'
print(message)
message = 'Hi '+ guest[3] + ' you are invited for the dinner tonight' + '.'
print(message)
message = 'Hi ' + guest[4] + ' you are invited for the dinner tonight'+ '.'
print(message)
message = 'Hi ' + guest[5] + ' you are invited for the dinner tonight'+ '.'
print(message)
