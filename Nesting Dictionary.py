#Nesting
#List of dictionaries
alien_0 = {'color': 'green' , 'points': 5}
alien_1 = {'color': 'yellow' , 'points': 10}
alien_2 = {'color': 'red' , 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

aliens=[]
for alien in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
 print(alien)
print("......")

print('Total number of aliens'+ str(len(aliens)))



child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
 }

print(child2)
print({'child2'},{'name'})

message = input("Tell me something and i will repeat the sentence:")
print(message)

