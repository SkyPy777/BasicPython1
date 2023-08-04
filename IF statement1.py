
age_0 = 21
age_1 = 15
age_2 = 18
if age_0 >= 24 and age_2>=20: 
    print('age_0 is greater and age_2 is smaller')
if age_0>20 and age_1<20:
    print('True')    
else:
    print('false')    


lst=[ 1, 6, 3, 5, 3, 4 ]
i = 7
if i in lst:
	print("exist")
else:
	print("not exist")
        

requested_topping = ['mushroom','onion','pineapple',]
requested = 'pepperoni'
if requested in requested_topping:
      print(True)
else:
      print(False)
requested = 'mushroom'
if requested in requested_topping:
      print(True)
else:
      print(False)


Class_attendance = ['Rahul','Sky','Raj','Boy','Girl']
Present = 'Sky'
if Present in Class_attendance:
      print('present')
else:
      print('absent')
present = 'Ram'
if present in Class_attendance:
      print('Ram is present today')
else:
      print('Ram is absent today')        


banned_user = ['andrew','carolina','david']
user = 'mike'
if user not in banned_user:
      print(user.title()+ ' you can submit your response'+'.' )
else:
      print('you are banned')      


car = 'audi'
print("car=='audi' I predict it true.")
print(car=='audi')
print("car=='benz' I predict it true.")
print(car=='benz')
print("car=='audi' I predict it true.")
print(car=='audi')
print("car=='audi' I predict it true.")
print(car=='audi')
print("car=='swift' I predict it true.")
print(car=='swift')
print("car=='audi' I predict it true.")
print(car=='audi')

#Equality
letters= ['a','b','c']
letter = ['a','b','c']
if letters == letter:
      print('This is equal')
else:
      print('Not equal')

#Inequality
letters= ['a','b','c']
letter = ['z','b','g']
if letter == letters:
      print('This is not equa')
else:
      print('This is not equal')

#lower function
letters = 'a'
letter = 'A'
if letters == letter.lower():
      print('Both variables are lower')
else:
      print('Not lower')   


#Numerical equality
A = '30'
B = '30'
if A == B:
      print('A and B are equal')
else:
      print('A and B are not equal')

#Numerical inequality
A = '30'
B = '25'
if A != B:
      print('A and B are not equal')
else:
      print('Not equal')   

#greater
A = '30'
B = '25'
if A >= B:
      print('A is greater then B') 


#Less 
A = '30'
B = '25'
if A <= B:
      print('A is less then B')
else:
      print('A is greater then B')  


#AND keyword
x = 10
y = 12

if x > 9 and y < 50:
      print('Both the condititns are true')
else:
      print('atlest one condition is true')      

if x > 20 or y < 5:
      print('Both the conditins are true')  
else:
      print('atlest one condition is true')     


letters = ['A','B','C']         
letter = 'B'
if letter in letters:
      print('Yes the b letter is in the list')
else:
      print('No b is not in the list')           
letter = 'Z'
if letter not in letters:
      print('Z is not in the list')
else:
      print('Z is in the list')      
