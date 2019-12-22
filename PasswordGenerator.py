"""
the script allows you to generate random password based on your choice of length, password combination.

requirements-
python 3 (any version)
random module of python in-built

author -chetan pawar
version- v1.0.1
"""

import random

digits_choice='0123456789'
alpha_uppercase_choice='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha_lowercase_choice='abcdefghijklmnopqrstuvwxyz'
special_char_choice='!@#$%^&*()'



no_of_passwords = int(input("how many passwords do you want?"))

digits=int(input('How many digits:'))
alpha_uppercase=int(input('How many uppercase chars:'))
alpha_lowercase=int(input('How many lower case chars:'))
special_char=int(input('How many special chars:'))

combination_dict={digits_choice:digits,alpha_uppercase_choice:alpha_uppercase,alpha_lowercase_choice:alpha_lowercase,special_char_choice:special_char}

for i in range(no_of_passwords):
    password=''
    l=[]
    for key,value in combination_dict.items():
        for i in range(0,int(value)):
            password=password+random.choice(str(key))
    l =list(password)
    random.shuffle(l)
    print('Password for you:',(''.join(l)))
