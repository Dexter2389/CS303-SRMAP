"""
Created on Saturday, November 02, 2019 11:00:46 IST

@author: Saurabh Ghanekar
"""

ip = input("Enter ip adddress= ")
firstq1 = ""

flag = 0

for i in range(len(ip)):
    if ip[i] == ".":
        firstqs = ip[:i+1]
        break

for i in range(len(ip)):
    if ip[i] == ".":
        firsths = ip[:i+1]
        flag = flag+1
        if flag == 2:
            break

firstq = int(firstqs[:len(firstqs)-1])
clas = ""

if firstq >= 1 and firstq <= 126:
    print("Class A")
    clas = "A"
elif firstq >= 128 and firstq <= 191:
    print("Class B")
    clas = "B"
elif firstq >= 192 and firstq <= 223:
    print("Class C")
    clas = "C"
elif firstq > 223:
    print("Out of range")

smask = ""
if clas == "A":
    smask = "255.0.0.0"
elif clas == "B":
    smask = "255.255.0.0"
elif clas == "C":
    smask = "255.255.255.0"

print("Subnet mask is=", smask)
if clas == "A":
    print("After bitwise adding=", firstqs+"0.0.0")
elif clas == "B":
    print("After bitwise adding=", ip[:len(firstqs)+1]+".0.0")
elif clas == "C":
    print("After bitwise adding=", firsths+"0.0")

snetvalue = int(input("Enter subnet value(1,2,3,4,5,6,7,8)= "))
if clas == "A":
    sembin = "255."+"1"*snetvalue+"0"*(8-snetvalue)+".0.0"
    dec = int("1"*snetvalue+"0"*(8-snetvalue), 2)
    print("255."+str(dec)+".0.0")
elif clas == "B":
    sembin = "255.255."+"1"*snetvalue+"0"*(8-snetvalue)+".0"
    dec = int("1"*snetvalue+"0"*(8-snetvalue), 2)
    print("255.255."+str(dec)+".0")
elif clas == "C":
    sembin = "255.255.255."+"1"*snetvalue+"0"*(8-snetvalue)
    dec = int("1"*snetvalue+"0"*(8-snetvalue), 2)
    print("255.255.255."+str(dec))
