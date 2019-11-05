#--------------debugging part 1--------------#
#common types of errors

#SyntaxError : Occurs when python encounters incorrect syntax
def first: #SyntaxError:  invalid syntax**********ERROR
None = 1   #SyntaxError:  invalid syntax**********ERROR
return     #SyntaxError:  invalid syntax**********ERROR


#NameError : Occurs when a variable is not defined i.e. hasn't been assigned
test #Name error 'test' is not defined********************ERROR

#TypeError : Occurs when an operation or fn is applied to wrong type
len(5)	#TypeError: object of type 'int' has no len()*******************ERROR
"awesome" + [] #TypeError: cannot concatenate 'str' and 'list' objects*******************ERROR


#IndexError : Occurs when you try to access an element in a list using 
#an invalid index(i.e. outside the range of the list or string)
lst = ["hello"]
lst[5]	#IndexError: list index out of range*****************ERROR

name = "Anubha"
name[2]	#u	
name[7]	#IndexError: string index out of range*****************ERROR

#ValueError : Occurs when built-in operation or fn recieves an argument that
#has the right type but an inappropriate value
int('10')	#10
int('foo') #ValueError: invalid literal for int() with base 10: 'foo'******************ERROR

#KeyError : Occurs when a dictionary does not have a specific key
d = {}
d['foo']	#KeyError: 'foo'**************ERROR

#AttributeError : Occurs when a variable does not have an attribute
[1,2,3].hello()	#AttributeError: 'list' object has no attribute 'hello'**************ERROR
"".joint(['a','b']) #AttributeError: 'str' object has no attribute 'joint'**************ERROR
