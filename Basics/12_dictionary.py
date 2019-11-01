#------------dictionary--------------#

# creating dictionary
person = {'name':'Anu', 'age':25, 'isCute':True}
# OR
person2 = dict(name = 'Micheal', age = 42, isCute = False)

print(person)
print(person2)


# accessing data from the dictionary
print(person['name'])		#Anu
print(person2['isCute'])	#False

#getting full name
artist = {"first":"Neil", "last":"Young"}
full_name = artist["first"]+' '+artist["last"]
print(full_name)

#iterating over dictionary
for detail in person.values():  #use.values() to retrieve values
	print(detail)


for detail in person.keys():  #use.keys() to retrieve keys
	print(detail)

for key, value in person.items():  #use.items() to retrieve key and values
	print(f"key is {key} and value is {value}")

#sum donation values
donations = {"sam":25.0, "lena":88.99, "chuck":13.0, "linus":99.5, "stan":150.0, "lisa":50.25, "harrison":10.0}
total_donations = 0
for v in donations.values():
	total_donations += v  
print(total_donations)

# check whether the randomly generated food is available at bakery_stock and if it is then, print the quantity left
from random import choice
food = choice(['cheese balls', 'quiche', 'morning bun', 'gummy bear', 'tea cake'])
bakery_stock = {
	"almond croissant" : 12,
	"toffee cookie" : 3,
	"morning bun" : 1,
	"chocolate chunk cookie" : 9,
	"tea cake" : 25
}
if food in bakery_stock:
	print(f"{food} : {bakery_stock[food]} left")
else:
	print(f"Sorry, we don't make {food}.")

#dictionary methods

#clear (it clear out all keys and values)
d = dict(a=1, b=2, c=3)
d.clear()	#{}

#copy (make a copy of a dictionary)
c = d.copy()	#{'a':1, 'b':2, 'c':3}
c is d # False means c and d both doesn't point to same memory location

#fromkeys (creates key-value pairs from comma separated values)
{}.fromkeys('a','b')	#{'a':'b'}
{}.fromkeys(['email'],'unknown')	#{'email':'unknown'}
{}.fromkeys('a',[1,2,3,4,5])	#{'a':[1,2,3,4,5]}

#get (retrieves a key in an object and return None instead of a keyError if the key does not exist)
d.get('a') 	#1
d.get('hjfda')	#None instead of keyError

#using fromkeys method
game_properties = ["current_score", "high_score", "number_of_lives", "items_of_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills"]
initial_game_state = {}.fromkeys(game_properties,0)
print(initial_game_state)

#pop method (takes a key and removes a key-value pair and returns the value of that key)
d = dict(a=1, b=2, c=3)
d.pop('a')	#1 (removes a=1)

#popitem method (removes a random key-value pair, takes no argument)
e = dict(a=1, b=2, c=3, d=4, f=5)
e.popitem()	#('d',4) 

#update (Update keys and values in a dictionary with another set of key value pair)
person1 = {'name':'Anu', 'age':27, 'isCute':True}
person2 = {"city": "Antigua"}
person2.update(person1)	
print(person2)	#{'city': 'Antigua', 'name': 'Anu', 'age': 27, 'isCute': True}
person2['name'] = 'Olive'
print(person2)	#{'city': 'Antigua', 'name': 'Olive', 'age': 27, 'isCute': True}

#Exercises
inventory = {'croissant':19, 'bagel': 4, 'muffin':8, 'cake':1}
stock_list = {}
stock_list.update(inventory)
print(stock_list)
stock_list['cookie'] = 18 
print(stock_list)
stock_list.pop('cake')
print(stock_list)