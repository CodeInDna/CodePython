print("Hello")	# print function

#-----------------------------------------------------------------
#String Concatenation
username = "kitty"
print("Hello "+ username)

#-----------------------------------------------------------------
#Interpolation(Formatting Strings)
guess = 8
print(f"Your guess of {guess} was Incorrect!")  #Converting Interger into a string

# OR

fname = 'John'
lname = 'Doe'
formatted = "First name : {}, Last name : {}".format(fname, lname)
print(formatted)