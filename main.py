from math import *

first = input("What's your first name? ")
last = input("Hey, " + first + "! What's your last name? ")

try:
  age = float(input("How old are you? "))
except:
  print: ("Your age should be a number, dumbass!")
 
 #how to get exception to print out?

city = input("Which city do you live in? ")

#currently working on figuring out how to use try and except to allow code to work when string is entered in age prompt

length = float(input ("How many years have you lived in " + city + "? "))

tenure = (age) - (length)

print (first + ", you moved to " + city + " when you were " + str(tenure))


#the code above took me 3 days to fix and several YT videos to figure how to convert a float to a string LMAO - feeling proud
#leaving previous code in here to look back on:

#print (first + ", you moved to " + city + " when you were")
#print (tenure)

print ("press any key to continue")
input(">")

print ("ITS MAD LIB TIME BITCH!")


color = input("What's your favorite color? ")
plural_noun = input("enter a plural noun ")
celebrity = input("Who's your favorite celebrity? ")


print ("Roses are " + color)
print (plural_noun + " are blue")
print ("I love " + celebrity)
print ("¯\_(ツ)_/¯")

