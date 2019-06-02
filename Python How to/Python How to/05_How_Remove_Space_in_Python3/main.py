#Remove the Starting Spaces in Python
string1="    This is Test String to strip leading space"
print (string1)
print (string1.lstrip())
#Remove the Trailing or End Spaces in Python
string2="This is Test String to strip trailing space     "
print (string2)
print (string2.rstrip())
#Remove the whiteSpaces from Beginning and end of the string in Python
string3="    This is Test String to strip leading and trailing space      "
print (string3)
print (string3.strip())
#Remove all the spaces in python
string4=("   This is Test String to test all the spaces        ")
print (string4)
print (string4.replace(" ", ""))


