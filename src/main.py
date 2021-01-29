#!/bin/python
import random 
from os import system, name

def clear(): 
  
    if name == 'nt': 
        system('cls') 
    else: 
        system('clear') 

clear()

minval = int(input("Minimum distance: "))

clear()

maxval = int(input("Maximum distance: "))

clear()

x = random.randint(minval, maxval)
z = random.randint(minval, maxval)

neg = random.choice([True, False])
if neg == True:
    x = ~x

neg = random.choice([True, False])
if neg == True:
    z = ~z

print(f"Your random location is\nX: {x} Z: {z}")
