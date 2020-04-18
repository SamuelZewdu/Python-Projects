#!/usr/bin/env python
# coding: utf-8

# In[1]:


#The weeks dictionary
weeks={"hours1":[{"name":"Earl", "hours":35}, {"name":"Lilly", "hours":55},
{"name":"Thomas", "hours":41},    {"name":"Ellis", "hours":40},
    {"name":"Sally", "hours":40}], "hours2":[{"name":"Earl", "hours":35},
 {"name":"Lilly", "hours":25},{"name":"Thomas", "hours":61},
    {"name":"Ellis", "hours":35}, {"name":"Sally", "hours":40}],
  "hours6":[{"name":"Earl", "hours":22}, {"name":"Lilly", "hours":35},{"name":"Ellen", "hours":39},
{"name":"Bes", "hours":40}], "hours4":[ {"name":"Ellen", "hours":40},
{"name":"Joseph", "hours":41}],  "hours5":[{"name":"Greg", "hours":22},
 {"name":"Lilly", "hours":55},{"name":"Beth", "hours":61}, {"name":"Sally", "hours":40}],
       "hours3":[{"name":"Greg", "hours":41},    {"name":"Joseph", "hours":40},
    {"name":"Beth", "hours":40}],   "hours7":[ {"name":"Lilly", "hours":55}],"hours8":[    {"name":"Joseph", "hours":40},
    {"name":"Sally", "hours":40}],  "hours9":[{"name":"Earl", "hours":40},
 {"name":"Lilly", "hours":40},{"name":"Thomas", "hours":40},
    {"name":"Ellis", "hours":40},   {"name":"Sally", "hours":40}],
    "hours10":[    {"name":"Greg", "hours":40},{"name":"Earl", "hours":35},
 {"name":"Lilly", "hours":55},{"name":"Thomas", "hours":41},    {"name":"Joseph", "hours":40},
    {"name":"Ellis", "hours":40}, {"name":"Sally", "hours":40}]
    }

#The payroll dictionary of employee hourly rate and tax rate
payroll={ "Earl":{ "hrrate":15.455,
 "taxrate":.09},"Greg":{"hrrate":15.455, "taxrate":.09},"Alice":{ "hrrate":19.175,
 "taxrate":.085}, "Ellen":{ "hrrate":11.3, "taxrate":.091},   "George":{ "hrrate":13.25,
 "taxrate":.1},"Bes":{ "hrrate":8.5, "taxrate":.009},"Joseph":{ "hrrate":18,
 "taxrate":.12},"Ellis":{ "hrrate":13.25,
 "taxrate":.1}, "Sally":{ "hrrate":8.5, "taxrate":.092}, "Thomas":{ "hrrate":6.5,
 "taxrate":.08},    "Lilly":{ "hrrate":12.2, "taxrate":.12}
    }


#Input the week number
week=int(input("Which week?"))
print()
#   DO NOT change any of the code above
weeks_key = "hours"+str(week)
paycards = weeks[weeks_key]
for user in paycards:
    name = user["name"]
    hours = user["hours"]
    hrrate= payroll[name]["hrrate"]
    taxrate = payroll[name]["taxrate"]
    if(hours>40):
        gross = 40*hrrate+(1.5*hrrate*(hours-40))
    else:
        gross = hours*hrrate
    tax_amount = gross*taxrate
    net = gross-tax_amount
    print("Name: {}".format(name))
    print("Gross ${:.2f}".format(gross))
    print("(less tax amt) ({:.2f})".format(tax_amount))
    print("Net ${:.2f}".format(net))
    print("*"*25)


#Put your code here





# In[ ]:




