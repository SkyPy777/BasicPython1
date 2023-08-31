
#input() function
message = input('Tell me something and, I will repeat it back:')
print(message)

Name = input('Can you say your name and please repeat it again:')
print(Name)

Name = input('Can you please enter your name:')
print('Hello, ' + Name + '.')

value = input('Please enter your value: ')
print('The value is : ' + value  + '.')

#Int() to accept numerical inputs
age = input('What is your age? ')
print('age : ' + age)

#height = input('\nHow tall are you, in inches ? ')
#height = int(height)
#if height >= 36:
    #print('You are tall enough for ride.')
#else:
    #print('\nYou will be able to ride when you will be litte older.')    

#age = input("\nWhat is you age right now ? ")
#age = int(age)
#if age >=18: 
    #print('You are eligibe to vote.')
#else:
    #print('\nYou are not eligible to vote.')    


#The modulo operator
num = 15
if num % 2 == 4:
    print('This is even number.')
else:
    print('This is odd number.')    


number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
 print(f"\nThe number {number} is even.")
else:
 print(f"\nThe number {number} is odd.")


Car = input('What kind of car are you looking for? ' )
print(f"Let me see if i can find u {Car.title()}.")   



resturant = input("How many people are in their dinner group?")
resturant = int("resturant")
if resturant > 8:
   print('You will have to wait for sometimes for the dinning table.')
else:
   print('The table is ready.')  


#pizza toppings
prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "
while True:
 topping = input(prompt)


 
