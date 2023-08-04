#simple if statement

age = 19
if age>= 18:
    print('You are eligible to vote.')
    print('Have you registered to vote yet?')

#if else statement
age = 17
if age>= 18:
    print('You are eligible to vote')
    print('Have you registered for the voting') 
else:
    print('Sorry, you are not eligble for vote.')
    print('Please register to vote as soon as you turn above 18.')      


#if elif else statement

age = 17
if age <= 4:
    print('Your admission cost is 0.')
elif age <= 18:
    print('Your admission cost is 5.')
else:
    print('Your admission cost is 10.')    


age = 20
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10     

print('Your admission cost is $' + str(price)+'.')  

#using multiple elif block

marks_scored = 82

if marks_scored >=90:
    grade = 'A'
elif marks_scored >=80:
    grade = 'B'
elif marks_scored >=70:
    grade = 'C'
elif marks_scored >=60:
    grade = 'D'
elif marks_scored >=50:
    grade = 'E'
else:
    grade = 'F'

print('You have scored ' + str(marks_scored) + ' which has the ' + (grade)+ ' grade' +'.')

requested_toppings = ['mushroom','extra cheese']
if 'mushroom' in requested_toppings: 
 print('Adding mushroom')

if 'pepperoni' in requested_toppings: 
 print('Adding pepperoni')

if 'extra cheese' in requested_toppings: 
 print('Adding extra cheese')

print("\nFinished making your pizza!") 

#Try your self

alien_color = 'green'
if alien_color == 'green':
    print('You just earned 5 points')

alien_color = 'red'
if alien_color == 'green':
    print('You just earned 5 point.')

alien_color = 'yellow'
if alien_color == 'yellow':
    print('You just earned 5 point.')    


alien_color = 'green'
if alien_color == 'green':
    print('You just earned 5 point.') 
else:
    print('You just earned 10 points.')    

alien_color = 'green'
if alien_color == 'red':
    print('You just earned 5 point.') 
else:
    print('You just earned 10 points.')    


alien_color = 'green'
if alien_color == 'red':
    print('You just earned 5 point.')
elif alien_color == 'yellow':
    print('You have just earned 10 points')
else:
    print('You just earned 15 point.')        


age = 17
if age < 2:
    print('This person is baby.')
elif age <4:
    print('This person is toddler')
elif age < 13:
    print('This person is a kid')
elif age<20:
    print('This person is teenager.')
elif age<65:
    print('This person is adult.')
else:
    print('This person is elder')        



favorite_fruits = ['blueberries', 'salmonberries', 'peaches']
if 'bananas' in favorite_fruits:
 print("You really like bananas!")
if 'apples' in favorite_fruits:
 print("You really like apples!")
if 'blueberries' in favorite_fruits:
 print("You really like blueberries!")
if 'kiwis' in favorite_fruits:
 print("You really like kiwis!")
if 'peaches' in favorite_fruits:
 print("You really like peaches!")


