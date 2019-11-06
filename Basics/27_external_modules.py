#----------------external modules------------------#
# pip is used to install packages in python
# python -m pip install NAME_OF_PACKAGE
# python -m pip install --upgrade pip - to upgrade pip

# use command 'python -m pip install termcolor' in cmd prompt or powershell(it adds color to our text)
import pyfiglet
from termcolor import colored

# print(dir(termcolor))	#returns the list of valid attributes and functions for the object
# print(help(termcolor))	#returns the documentation for the passed object

text = colored("Hi There!", color="cyan", on_color="on_magenta", attrs=[
               'blink'])  # color will not gonna show on powershell
print(text)

# ASCII ART Exercise
# print(help(termcolor))
result = pyfiglet.figlet_format(input("What do you wanna print?"))
print(result)


# autopep8 package is used to make your python code more organised
# How to use it
# install autopep8 using command 'python -m pip install autopep8'
# use command 'autopep8 --in-place file_name'
# you can see changes in the specified file

#if you want the code to follow aggressive(strict) standards then use 
#autopep8 --in-place -a -a file_name.py