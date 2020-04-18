#!/usr/bin/env python
# coding: utf-8

# In[ ]:


input_month = input().lower()
input_day = int(input())

''' Type your code here. '''

spring = ['march','april','may','june']
summer = ['june','july','august','september']
autumn = ['september','october','november','december']
winter = ['january','february','march']

if (input_day>30 or input_day<1):
    print("Invalid")
    exit()

if input_month in spring:
    if (input_month != "march") and (input_month !="june"):
        print("Spring")
    elif (input_month == "march" and input_day<20):
        print("Winter")
    elif (input_month == "march" and input_day>=20) or (input_month=="june" and input_day<=20):
        print("Spring")
    else:
        print("Summer")
        
elif input_month in summer:
    if (input_month != "june") and (input_month !="september"):
        print("Summer")
    elif (input_month == "june" and input_day>=21) or (input_month=="september" and input_day<=21):
        print("Summer")
    else:
        print("Autumn")
        
elif input_month in autumn:
    if (input_month != "september") and (input_month !="december"):
        print("Autumn")
    elif (input_month == "september" and input_day>=22) or (input_month=="december" and input_day<=20):
        print("Autumn")
    else:
        print("Winter")
        
elif input_month in autumn:
    if (input_month != "december") and (input_month !="march"):
        print("Winter")
    elif (input_month == "december" and input_day>=21) or (input_month=="march" and input_day<=19):
        print("Winter")
    else:
        print("Spring")
else:
        print("Invalid")

