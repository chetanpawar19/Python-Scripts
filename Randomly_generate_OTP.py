"""
Script allow you to generate random OTP
"""

from random import *

#way-1
for i in range(5):
    print(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), sep="")

#way-2
import math
def generateOTP():
    digits='0123456789'
    otp=''
    for i in range(4):
        otp=otp+digits[math.floor(random()*10)]
    return otp
print('OPT=',generateOTP())

#way 3

def generateOTP():
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    OTP = ""
    length = len(string)
    for i in range(6):
        OTP += string[math.floor(random() * length)]
    return OTP
print('OPT=',generateOTP())
