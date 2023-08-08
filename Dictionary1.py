#Python dictionaries
Info = {'name': 'Karan', 'age': 20, 'eligible': True}
print(Info)

year = {'Month': 4, 'Day': 'Tuesday', 'Days': 365}
print(year)

#Accessing single values
marks = {'English': 45, 'Maths': 23, 'social': 'fail'}
print(marks['Maths'])
print(marks.get('social'))

Info = {'Name': 'Sky', 'Age': '20', 'eligible': True}
print(Info)
print(Info['Name'])
print(Info.get('Name'))

#Accessing multiple values
Fruits = {'Apple': 24, ' Mango': 34, 34:'orange'}
print(Fruits)
print(Fruits.values())

Stationary = {'Pen': 10, 'Box': 30, 'pencil': 13, 56: 'Bag'}
print(Stationary)
print(Stationary.values())

#Accessing multiple keys
Fruits = {'Apple':24, 'Mango':34, 34:'orange'}
print(Fruits)
print(Fruits.keys())

Marathon = {'Rahul': 1, 'Mike':3, 'Sohil':2}
print(Marathon)
print(Marathon.keys())

#Accessing key-value pairs
Stationary = {'Pen': 10, 'Box': 30, 'pencil': 13, 56: 'Bag'}
print(Stationary)
print(Stationary.items())

marks = {'Maths': 34, 'Science':56, 'Gk':21}
print(marks)
print(marks.items())

#Adding new key and assigning a value to it
info = {'Name': 'sky', 'Age': 21, 'Eligible': 'True'}
print(info)
info['student'] = 'True'
print(info)

Books = {'History': 1, 'Social': 2, 'Maths':3}
print(Books)
Books['Gk'] = 3
print(Books)

#updating the dictionary
info = {'Name':'Mike', 'Age':23, 'Eligible':'True'}
print(info)
info.update({'Age':25})
info.update({'Name':'Smith'})
print(info)

#Removing the items from dictionary
info = {'Name': 'Subhash', 'Age': 24,'eligible':'True', 'Student':True}
print(info)
info.clear()
print(info)

months = {'January': 28, 'March': 31, 'April': 31}
print(months)
months.clear()
print(months)

#Removing the key-value pair
months = {'January': 30, 'March': 31, 'April':29}
print(months)
months.pop('March')
print(months)

marks = {'English': 45, 'Maths': 23, 'social': 'fail'}
print(marks)
marks.pop('social')
print(marks)

#Remove last key-value using popitem()
months = {'January': 30, 'March': 31, 'April':29}
print(months)
months.popitem()
print(months)

info = {'Name':'Mike', 'Age':23, 'Eligible':'True'}
print(info)
info.popitem()
print(info)

#Delete the key-value using del() keyword
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
print(info)
del info['age']
print(info)

Books = {'History': 1, 'Social': 2, 'Maths':3}
print(Books)
del Books['Social']
print(Books)

#If key is not provided then entire dictionary will be deleted
#Books = {'History': 1, 'Social': 2, 'Maths': 2}
#print(Books)
#del Books
#print(Books)     

#print error that 'Books' is not defined.


#Copy dictionarie
info = {'Name':'Mike', 'Age':23, 'Eligible':'True'}
print(info)
New_Dictionaries = info.copy()
print(New_Dictionaries)

info = {'Name':'Mike', 'Age':23, 'Eligible':'True'}
print(info)
New_Dictionaries = dict(info)
print(New_Dictionaries)
