"""
	Program to validate password is strong or not.
	password validation 6 to 20 length, 2 lower, 2 upper, 2 nums and 2 special symbols at least

"""

import re

#way 1

password = input("Enter password to validate:")
print("Strong password " if (len(password)>=6 and len(password)<=20) and re.search(r'[a-z]+[A-Z]+[0-9]+[$#@_]+',password) else "Weak password")


#way 2

passwords=[i for i in input('Enter passworad:').split(',')]
flag=0
valid_passwords=[]
valid_pass_str=''

for password in passwords:
    while True:
        if not (len(password)>=6) and (len(password)<=12):
            break
        elif not re.search(r'[a-z]',password):
            break
        elif not re.search(r'[A-Z]',password):
            break
        elif not re.search(r'[0-9]',password):
            break
        elif not re.search(r'[$@#_]',password):
            break
        else:
            flag=1
            valid_passwords.append(password)
            break

if flag==1:
    valid_pass_str=','.join(str(i) for i in valid_passwords)        
    print('strong passwords:',valid_pass_str)
else:
    print('All passwords are strong!')
