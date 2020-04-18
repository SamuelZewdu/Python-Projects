#!/usr/bin/env python
# coding: utf-8

# In[2]:


def whatCar(make,model,year=2020,color="Red"):
    premiummakes={"mercedes", "bmw", "lexus", "rangerover"}
    if make.lower() in premiummakes:
        return("Ordering a premium {} {} {} {}".format(year, color.title(), make, model))
    else:
        return("Ordering a {} {} {} {}".format(year, color.title(), make.title(), model))


# In[ ]:




