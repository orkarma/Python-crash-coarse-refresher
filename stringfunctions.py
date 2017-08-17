#STRING funtions
from variables import myStr

myStr = 'hello world'

#captilize
print(myStr.capitalize())

#swap case
print(myStr.swapcase())

#get length
print(len(myStr))

# replace
print(myStr.replace('world', 'everyone'))

#count
sub = "l"
print(myStr.count(sub))

#startsWith
print(myStr.startswith('hello'))

#endswith

print(myStr.endswith('d'))

#split to list
print(myStr.split())

#find
print(myStr.find('w'))

#index
print(myStr.index('r'))

#is all alphanumeric
print(myStr.isalnum())

#is all alphabetic 
print(myStr.isalpha())

#is all numeric
print(myStr.isnumeric())
