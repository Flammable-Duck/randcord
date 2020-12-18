import random 
from os import system, name


# define clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

# get imput from user
clear()

print("Please imput the minimum distance:")

minval = input()

clear()

print("please imput the maximum distance:")

maxval = input()

clear()

# do cool math stuff idk

minval = int(minval)
maxval = int(maxval)

x = random.randint(minval, maxval)

z = random.randint(minval, maxval)

neg = random.choice([True, False])
if neg == True:
    x = ~x

neg = random.choice([True, False])
if neg == True:
    z = ~z
# show result
print("Your random location is")
print("x:", x, "z:", z)
