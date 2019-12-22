"""
	dictionary structure to browse countries-their cities-sub areas and finally get pin code
	author-Chetan Pawar
"""

#way 1

d ={
    "India":{
            "Maharashtra":{
                    "Pune":{
                            "Shivaji nagar":411001,
                            "Kothrud":411038,
                            "Kalyani nagar":411014
                        },
                    "Mumbai":{
                            "Kalyan":30012,
                            "Panwel":30014,
                            "andheri":30015
                        }
                },
            "Gujrat":{
                    "Ahmedabad":{
                            "Thaltej":20021,
                            "Shilaj":20032
                        },
                    "Surat":{
                            "Patel nagar":30900,
                            "Gandhi nagar":30901
                        }
                }
        }
    }

print("Countries=",d.keys())
country = input("Browse Country=")
print(d[country])
state = input("Browse State=")
print(d[country][state])
city = input("Browse City=")
print(d[country][state][city])
area= input("Browse Area for pin code=")
print(d[country][state][city][area])


#way 2

state={
        'Maharashtra':{
            'Pune':{'Shivaji nagar':'411001','Kothrud':'411038','kalyani':'411014'},
            'Mumbai':{'Borivali':'412012','Thane':'412013'},
            'Nashik':{}},
        'Gujrat':{
            'Surat':{'test1':'00001','test2':'00002'},
            'Ahmedabad':{'Bopal':'380001','South bopal':'380002'},
            'Vadodara':{}
            },
        'UP':{},
        'Goa':{}
       }

print('States=',state.keys())
statename=input('select state to view cities:')
print(state[statename])
cityname=input('select city name:')
print(state[statename][cityname])
area=input('select area to view area code')
print(state[statename][cityname][area])


