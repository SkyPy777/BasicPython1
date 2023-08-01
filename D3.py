#variables
message = "hello python world"
print(message)

message = "hello python crash course"
print(message)

Note = 'variables name are case-sensitive'
print(Note)

#string
text = "This is string"
text = 'This is also string'
print (text)
print (text)
single_quote = 'hello world'
print(single_quote)

double_quote = "hello world"
print(double_quote)

multiple_string = "This is a 'multiple string'"
print(multiple_string)

message = 'I told my friend, "Python is my favourite language"'
print(message)

#changing case in string
name = 'python'
print(name.title())
print(name.upper())
print(name.lower())

#combining or concatenation strings
first_name = 'subhash'
middle_name = 'kumar'
last_name = 'yadav'
full_name = (first_name.title()+ " " + middle_name.title()+ " " + last_name.title())
print(full_name)

first_name = 'John'
last_name = 'lace'
full_name = (first_name + " " + last_name)
message = "Hello," + full_name.title()+ "."
print(message)

#adding whitespace to string
address = "123 street,\nBangalore"   #\n - new line
print(address)

message = "Hello\tWorld"    #\t - new tab
print(message)

simple_message = "Address:230 Avenue,\n\tsuite 103 palo alto."
print(simple_message)

languages = ("Languages:\n\tpython\n\tjavascript\n\tc\n\tc++")
print(languages)

#strip whitespace
text_with_whitespace = '  Hello world!  '
strriped_text = text_with_whitespace.strip()
print("|" + strriped_text + "|")

text_with_leading_whitespace = "   Hello world!  "
leading_whitespace = text_with_leading_whitespace.lstrip()
print("|" + leading_whitespace + "|")

text_with_trailing_whitespace = "  Hello world!  "
trailing_whitespace = text_with_trailing_whitespace.rstrip()
print("|" + trailing_whitespace+"|")

#Avoid syntax error
message = "Here's how to use single and double quote's"  #no error
print(message)

#message = 'Here's how to use single and double quote's'  #Syntax error
#print(message)

#Exercise
message = "Hello Eric, Would you like to learn python?"
print(message)

message = 'subhash'
print(message.title())
print(message.upper())
print(message.lower())

Famous_quotes = '\tAlbert Einstein once said:"A person who never made a\n\tmistake never tried anything new."'
print(Famous_quotes)

print('Success is not the key to happiness.')
print('Happiness is the key to success')
print('if you love what you are doing you will be successfull')

famous_person = 'Albert Schweitzer:\n'
message = 'Success is not the key to happiness\n Happiness is the key to success.'
print(famous_person + " " + message)

Name = '  Eric  '
print("\nUsing strip()")
print("|" + Name.strip() + "|")
print("\nUsing lstrip()")
print("|" + Name.lstrip() + "|")
print("\nUsing rstrip()")
print("|" + Name.rstrip()+ "|")

#integer

age = 23
quantity = 1000
population = 987654321
print(age)
print(quantity)
print(population)

#Arithmetic operation
a = 10
b = 15

sum_result = a+b
subtract_result = a-b
multiply_result = a*b
division_result = a/b

print("Sum:", sum_result)
print("Subtract:",subtract_result )
print("multiple:", multiply_result)
print("division:", division_result)

#float
a = 2.5
b = 3.8

sum_result = a+b
subtract_result = a-b
multiply_result = a*b
division_result = a/b

print("Sum:", sum_result)
print("Subtract:",subtract_result )
print("multiple:", multiply_result)
print("division:", division_result)

age = 21
message = " Happy " + str(age) + "rd birthday"
print(message)

#Comment
#Say hello to everyone         #This is comment which is ignored
print("Hello python people")



