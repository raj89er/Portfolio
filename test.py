# this is a comment

# it doesnt matter how many lines
# we can have loads of comments! 


print("Hello Kekambas 142") #comment after code! 

#vars!

# syntax --> <var> = <value>
x = 5 #int value

a_greeting = "How is it going?" #string val

# Data types
    #numbers
        # Integers, floats, and complex numbers
    # string
    #list ,range
    #dictionary (sometimes called an object)
    # Boolean
    #Nonetype

#Numbers

#int
num1 = 10
num2 = -33
num3 = 30
num4 = float(num1)
print(num1,num2,num3, num4)
#floats have decimals!

num5 = 5.0
print(type(num5))

# math operations

print(" \n MATH STUFF")

#add +

print(num1+num3)

#subtract -
print(num3 - num1)
print(5 -3)

# multiply *

print(num1 * num3)

#divide / this is always going to give us a float!

print(num1/num4)

#floor divison // always give an int!(mostly)

print(num1 // num2)
print(27//5)
num6 = 5
#quick adding!
print("======================================")
#trad
print(num6)
num6 = num6 + 1
print(num6)

#quick 
num6 +=  1
print(num6)

num6 -= 1
print(num6)

num6 *= 10
print(num6)


# Modulo always an int (mostly) %
print(27 % 5)
print(5 % 15)
print(25% 5)


# quick note ! = vs  == 
# = is assignment (this is this now!)
# == evaluation (does this equal this?) 
num6 = 5
print(num6)
print(num6 == 5.0)
# will always be a boolean!
# comparison ops:
# == equal to
# != Does not equal 
# < less than packman rules he wants the bigger one!
# > greater than 
# <= less than or equal too
# >= greater than or equal to  


print(2 < 1)
print(2 > 1)

#this is important!
#even or odd? 
print(26 % 2 == 0) #even
print(27 %2 != 0) #Odd

print(27 % 2 == 0) # this gives false because it is an odd number and will not equal 0!


#exponents (gah) ** 
print(5**5)


# naming conventions 
x = 33
int 
str 
float
#dont overwrite these

#predefined char set (functions or classes)
#Built in's are your friend!

#strings!
print("=============================================================")
# indexable, iterable, immutable
str1 = "This is a string"
str2 = "this one is too!"
str3= "So iS ThIS oNE!"
# double or single qoutes are fine, as long as they match, or using an escape char
str4 = 'so\'s this one' 
str5 = "so's this one second time"
str6 = 'travis said "you guys are cool!"'

print(type(str1))
print(str4)

print(str1[6])

print("string"[0])

#concat fancy way of saying add these strings together!

print(str1 + " "+str2)

print("="*100)

#interpolation an even fancier way of saying we are going to add strings and pyhton things together!
f_string = f"this is an f-string that also has this from python --> {num6+ 100}!"
print(f_string)
f_name = "mIkE"
print(f"Hello {f_name.title()}!")

# methods vs functions!
# kinda the same thing here... except methods work on specific data types!
# syntax is the magic clue  methods == <data_type>.methodname(parameter) vs function == function(parameter)

# method we have used: 
#function we have used:   

# my_str = str()
# print(my_str)
# print("hello ")

#slicing!
my_string = "Duck Duck duck Goose!"
print(my_string[15:20])
print(my_string[-6:20])
my_str2="goose duck duck duck"
print(my_str2[:5])


#LISTS
print("\n LISTS!!!!!!!!!!!!!!!!!")

#lists also called arrays(in other lang)! 
#ordered/indexed , iterable , and mutable!

#syntax --> <var_name> = [] or <var_name> = list() 
# filled with values seperated by commas!
#we can store just about anything in a list!

my_list = []
my_num_list = [1,2,3,4,5,6,7]
my_string_num_list = ['1','2','3','4','5']
confused = [1,'2','three',4.0,True,None]

print(my_num_list[3])

print(confused[4])

#adding to a list!
#syntax -> <list>.append(<what i want to add>) this is a method!

my_list.append("jeff")
my_list.append("adonai")
print(my_list)
my_list.append("ryan"*2)
print(my_list)
my_list.append("ryan")
print(my_list)
my_list.append("ryan"*2)
#remove or pop 
# my_list.pop(2)
my_list.remove("ryanryan")
my_list.remove("ryanryan") #not optional, it will delete the first instance of the remove argument
print(my_list)
#pop is index based, if i dont specify it will take off the -1 index, if i do, it will remove the index given (optional parameter)
popped = my_num_list.pop()
print(popped)
print(my_num_list)

# help(list)


#check for membership
# in keyword
print("travis" in my_list)
print(1 in my_num_list)
print("n" in 'None')

#conditionals! 
# if elif else
#we can use as many if statments as we want, each one checks for a circumstance to be true
# if we want to check the same var against other circumstances we can use elif or else
#we will always start with an if, we CAN have as many elifs as we want after that! and we CAN finish with an else

# print("\n AGE and conditionals")

# age = input("Whats ya age????")
# if age.isdigit():
#     age = int(age)
# else:
#     age = int(input("GIVE A VALID NUMBER USING BASE LITERAL"))
 
# if age > 64:
#     print("senior")
# elif age >= 21:
#     print("welcome to da club")
# else:
#     print("A child!")

# #chaining
    
# if age > 20 and age <65:
#     print("welcome to da club")
# else:
#     print("Get outta here!")



#truth tree
    
#T and T == T
#T and F == F
# F and F == F
    
# T or T == T
#T or F == T
#F and F == F
    
#functions
print("====="*50)

#syntax : 
#def <function name>(param(s)):
    # codeblock to execute
    # return (optional!!!!)

def even_or_odd(num):
    if num % 2 == 0:
        print("EVENSTEVENS")
    else:
        print("ODD")
even_or_odd(7)

def even_or_odd2(num):
    if num %2 == 0:
        return "EVEN STEVENS"
    else:
        return "ODD"
    
tuesday = even_or_odd2(4)
thursday = even_or_odd(4)
print(f'Tuesday :{tuesday}', f"Thursday:{thursday}")

#loops (not the fruit kind :( )

for student in my_list:
    student = student.title() 
    print(len(student))


#while loop!
#while <condition>
while True:
    print("Helllllllllllllllllllllooooooooooooooooooooooooooooooo")
    break

my_list = [1,2,2,2,2,3,3,3,3,4,5,6,7,8]
while 2 in my_list:
    my_list.remove(2)
    

print(my_list)