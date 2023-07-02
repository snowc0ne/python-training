#fname = input("What is your name? ")
#lname = input("What is your last name? ")

#print("Hello there,"+" " + fname + " " + lname)

#first_name = 'nig'
#last_name = 'ma'
#full_name = first_name +" "+ last_name
#print("Hello " + full_name)

#print(type(name))
#print("Hey " + name)

#age = 21
#age += 1
#print("Your age is: "+str(age))


#height = 250.5
#print("Your height is: "+str(height)+" CM")


#human = True
#print("Are you a human: "+str(human))
#print(type(human))




#name = "nig"
#age = 21
#attractive = True

#name, age, attractive = "nig", 21, True

#print(name)
#print(age)
#print(attractive)

#Sponge = Patrick = Sand = Squid = 30
#print(Sponge,Patrick)


#name = "big"

#print(len(name))
#print(name.find("i"))
#print(name.capitalize())
#print(name.upper())
#print(name.lower())
#print(name.isdigit())
#print(name.isalpha()) #checks for alphabetical letters
#print(name.count("i"))
#print(name.replace("i", "igg"))
#print(name*3)


#x = 1
#y = 2.0
#z = "3"

#typecasting converting values
#x = float(x)
#y = float(y)
#z= float(z)

#print(type(x))
#("X is "+str(x)) #displaying a float as a string while retaining float
#print("Y is "+str(y))
#print(z*3)



#Accept user input

#name = input("What is your name?: ")
#age = float(input("How old are you?: "))
#height = float(input("How tall are you in cm?: "))


#print("Hello " +name)
#print("Damn homes you really "+str(age)+ " years old? shieet")
#print("Damn homie you tall as shit at "+str(height)+ " cm")


# Things you can do with importing math
#import math

#pie = 3.14
#x=1
#y=2
#z=3

#print(round(3.49))
#print(math.ceil(pie)) #rounds a number up - ceiling
#print(math.floor(pie)) #rounds down
#print(abs(pie)) #how far a number is from 0
#print(pow(pie,9)) #to the power of
#print(math.sqrt(pie)) #calcuates the square root
#print(max(pie,x,y,z)) #finds the largest in given variables
#print(min(pie,x,y,z)) #finds the lowest in given variables

## String Slicing in Python - create a substring by extracting elements from another string
# indexing[] or slice()
# [start:stop:step] - Step lets you set it so you can count more than 1 word after (every 2 letters)

##Demonstrates indexing

#name = "maciej"

#first_name = name[0:3]
#last_name = name[3:6]
#funky_name = name[::2] # Counts every 2 letters. Leaving the :: blank means that the array starts at 0 and ends at the end of the string
#reversed_name = name[::-1] # Counts backwards - printing your name backwards


#print(first_name)
#print(last_name)
#print(funky_name)
#print(reversed_name)


##Slice demonstration to remove http:// and .com

#website1 = "http://google.com"
#website2 = "http://wikipedia.com"

#slice = slice(7,-4)

#print(website1[slice])
#print(website2[slice])


### if statement = a block of code that will execute if True

#age = int(input("How old are you?: "))

#if age == 21:
    #print("You can drink Alcohol in the states")
#elif age >= 18:
    #print("You are old")
#elif age < 0:
    #print("You are a fetus")
#else:
    #print("You are young")



