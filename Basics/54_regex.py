#------------Regular Expressions--------------#

# Regex: A way of describing patterns within search strings
# Potential Use Cases: 
	# validating email id(checking format)
	# Credit Card number validating
	# Phone Number Validating
	# Advanced find/replace in text
	# Formatting Text Output
	# Syntax Highlighting

# Some regex syntax
# \d : digit 0 - 9
# \w : letter, digit, or underscore
# \s : whitespace character
# \D : not a digit
# \W : not a word character
# \S : not a whitespace character
# . any character except line break

# Quantifiers (How many times a thing should occur)
# + : One or more
# {3} : Exactly x times {3} - 3 times
# {3,5} : Three to five times
# {4,} : Four or more times
# * : Zero or more times
# ? : Once or none(optional) 

# [aeiou] : instance that match one of these characters say a or e or i or u or u
# [aeiou]{2} : instance that match two same chars of these characters say aa or ee or ii or oo or uu
# [a-z] : instance that matches a to z any of them
# [a-z0-9] : instance that matches a to z or  0-9 any of them 
# [^k] : not the letter k

# Anchors and Boundaries
# ^ : Start of string or line
# $ : End of string or line
# \b : Word Boundary

# Logical OR (|) ex: Mr|Mrs|Ms


# Validating phone number with Python*******************************************************
# import regex module
import re

pattern = re.compile(r'\d{3} \d{3}-\d{4}')	# r :raw string that way you tell that you actually wanna use '\'

res = pattern.search('Call me at 415 555-4242!')

print(res)	# gives you a match object: <re.Match object; span=(11, 23), match='415 555-4242'>

print(res.group())		# 415 555-4242

res2 = pattern.search('Call me at 415 555-4242! or 310 445-4234')

print(res2.group())	# 415 555-4242 : It gives the first match

res3 = pattern.findall('Call me at 415 555-4242! or 310 445-4234')

print(res3)	# ['415 555-4242', '310 445-4234']

res4 = re.search(r'\d{3} \d{3}-\d{4}', 'Call me at 415 555-4242!').group()

print(res4)		# 415 555-4242


# Write a function called is_valid_time that accepts a single string argument.It should return True if the
# string is formatted correctly at a time like 3:15 or 12:48 and return False otherwise. Note that timees can
# start with a single number (2:30) or two (11:18)
def is_valid_time(str):
	pattern = re.compile("^\d\d?:\d\d$")
	if pattern.search(str):
		return True
	return False
print(is_valid_time('12:10'))	#True
print(is_valid_time('132:10'))	#False

# Passing urls with Python*******************************************************
url_regex = re.compile(r"(https?://)(www\.[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)")
match = url_regex.search("http://www.youtube.com/videos/asd/hds/ad/fa")
print(match.group())	# http://www.youtube.com/videos/asd/hds/ad/fa
print(match.group(0))	# http://www.youtube.com/videos/asd/hds/ad/fa
print(f"Protocol: {match.group(1)}")	# http://
print(f"Domain: {match.group(2)}")	# www.youtube.com
print(f"Everything Else : {match.group(3)}")	# /videos/asd/hds/ad/fa
print(match.groups())	# ('http://', 'www.youtube.com', '/videos/asd/hds/ad/fa')


# Write a function parse_bytes that accepts a string. It should return a list of the binary bytes contained in the string
# Each byte is just a combination of eight 1's or 0's
def parse_bytes(string):
	pattern = re.compile(r"\b[01]{8}\b")
	match = pattern.findall(string)
	return match
print(parse_bytes("my data is 10101000 and 01010110"))	# ['10101000', '01010110']


# OR (|)
def parse_name(string):
	name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) ([A-Za-z]+) ([A-Za-z]+)$')
	matches = name_regex.search(string)
	return matches.groups()
print(parse_name("Mrs. Tilda Swinton"))	# ('Mrs.', 'Tilda', 'Swinton')

def parse_name2(string):
	name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')
	matches = name_regex.search(string)
	return matches.group('first')
	# return matches.group(1)
print(parse_name2("Mrs. Tilda Swinton"))	# Tilda


# parse_date fn: check if the string matches a date format. format: dd/mm/yyyy or dd.mm.yyyy or dd,mm,yyyy
# It should return a dict as {d: ,m: ,y: }
def parse_date(string):
	pattern = re.compile(r'^(\d{2})[/.,](\d{2})[/.,](\d{4})$')
	matches = pattern.search(string)
	if matches:
		return {
			'd': matches.group(1),
			'm': matches.group(2),
			'y': matches.group(3)
		}
print(parse_date("12,04,2001"))	# {'d': '12', 'm': '04', 'y': '2001'}

# Compilation Flags
# re.VERBOSE helps us to add comments and use regex in multiple lines
# re.IGNORECASE ignores the case
pat = re.compile(r"""
	^([a-z0-9_\.-]+) 	# first part of email
	@ 					# single @ sign
	([0-9a-z\.-]+) 		# email provider
	\. 					# single period
	([a-z\.]{2,6})$ 	# com, org, net, etc.
	""", re.VERBOSE | re.IGNORECASE)
match = pat.search("johndoe@yahoo.com")
match1 = pat.search("johndoe@yYahoo.com")
print(match.group())	# johndoe@yahoo.com
print(match.groups())	# ('johndoe', 'yahoo', 'com')
print(match1.groups())	# ('johndoe', 'yYahoo', 'com')


# Regex Substitution Basics
text = "Last Evening Mrs. Daisy and Mr. White went to Disney land with Ms. Clark"
# patt = re.compile(r"(Mr.|Mrs.|Ms.) [a-z]+", re.IGNORECASE))
patt = re.compile(r"(Mr.|Mrs.|Ms.) ([a-z])[a-z]+", re.IGNORECASE)
# result = patt.sub("REDACTED", text)	# Last Evening REDACTED and REDACTED went to Disney land with REDACTED
result = patt.sub("\g<1> \g<2>", text)	
print(result)	# Last Evening Mrs. D and Mr. W went to Disney land with Ms. C


# censor fn : accepts a string. censor any word starts with frack. This includes frack, fracker, fracking etc. Replace the entire word with "CENSORED"
# your regex should be insensitive
def censor(str):
	pattern = re.compile(r"\bfrack\w*\b", re.I)
	match = pattern.sub("CENSORED", str)
	print(match)
censor("frack you!")				# CENSORED you!
censor("I hope you fracking die!")	# I hope you CENSORED die!
censor("you fracking frack")		# you CENSORED CENSORED


# Swapping file names
titles = [
    "Significant Others (1987)",
    "Tales of the City (1978)",
    "The Days of Anna Madrigal (2014)",
    "Mary Ann in Autumn (2010)",
    "Further Tales of the City (1982)",
    "Babycakes (1984)",
    "More Tales of the City (1980)",
    "Sure of You (1989)",
    "Michael Tolliver Lives (2007)"
]

titles.sort()
print(titles)
fixed_titles = []
pat = re.compile(r"(^[\w ]+) \((\d{4})\)")
for book in titles:
	fixed_titles.append(pat.sub("\g<2> - \g<1>", book))
fixed_titles.sort()
print(fixed_titles)