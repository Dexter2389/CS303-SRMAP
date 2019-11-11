"""
Created on Saturday, November 02, 2019 11:00:46 IST

@author: Saurabh Ghanekar
"""

ip = input("Enter ip adddress: ")
firstq1 = ""

flag = 0

for i in range(len(ip)):
    if ip[i] == ".":
        firstqs = ip[:i + 1]
        break

for i in range(len(ip)):
    if ip[i] == ".":
        firsths = ip[:i + 1]
        flag += 1
        if flag == 2:
            break

firstq = int(firstqs[:len(firstqs) - 1])
class_ = ""

if firstq >= 1 and firstq <= 126:
    print("Class A")
    class_ = "A"
elif firstq >= 128 and firstq <= 191:
    print("Class B")
    class_ = "B"
elif firstq >= 192 and firstq <= 223:
    print("Class C")
    class_ = "C"
elif firstq > 223:
    print("Out of range")

subnet_mask = ""
if class_ == "A":
    subnet_mask = "255.0.0.0"
elif class_ == "B":
    subnet_mask = "255.255.0.0"
elif class_ == "C":
    subnet_mask = "255.255.255.0"

print("Subnet mask is=", subnet_mask)
if class_ == "A":
    print("After bitwise adding=", firstqs + "0.0.0")
elif class_ == "B":
    print("After bitwise adding=", ip[:len(firstqs)+1] + ".0.0")
elif class_ == "C":
    print("After bitwise adding=", firsths + "0.0")

subnet_value = int(input("Enter subnet value(1,2,3,4,5,6,7,8)= "))
if class_ == "A":
    sembin = "255." + "1"*subnet_value + "0"*(8 - subnet_value) + ".0.0"
    dec = int("1"*subnet_value + "0"*(8 - subnet_value), 2)
    print("255." + str(dec) + ".0.0")
elif class_ == "B":
    sembin = "255.255." + "1"*subnet_value+"0"*(8 - subnet_value) + ".0"
    dec = int("1"*subnet_value + "0"*(8 - subnet_value), 2)
    print("255.255." + str(dec) + ".0")
elif class_ == "C":
    sembin = "255.255.255." + "1"*subnet_value + "0"*(8 - subnet_value)
    dec = int("1"*subnet_value + "0"*(8 - subnet_value), 2)
    print("255.255.255." + str(dec))

