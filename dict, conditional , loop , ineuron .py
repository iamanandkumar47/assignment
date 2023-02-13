#!/usr/bin/env python
# coding: utf-8

# In[5]:


d = {}


# In[6]:


type(d)


# In[7]:


d1 = {'key':"anand"}


# In[8]:


d1


# In[10]:


d2 = {'name':"anand kumar","email": "anandkumar@gmail.com", "number": 56748}


# In[11]:


d2


# In[12]:


d3 = {234:'anand', '_anand':'kumar',True:45677}


# In[13]:


d3


# In[15]:


#for taking out value
d3[234]


# In[16]:


d3[True]


# In[17]:


d3[1]


# In[18]:


# key should always be unique beacuse to avoid override 
d4 ={'name':'anand','mail_id':'anand@gmail.com','name':'anandkumar'}


# In[20]:


d4['name']


# In[21]:


d5 = {'company':'newnumco.','course':['web dev','data science','java with dsa system design']}


# In[22]:


d5['course']


# In[23]:


d5['course'][2]


# In[37]:


d6 = {"number" : [2,34,3,56,34] , "assignment" : (1,2,3,4,5,6) , "launch_date":{28,12,14},"class_time":{"web_dev":8 , "data science" :8 , "java with dsa and system design":7}}


# In[38]:


d6


# In[40]:


d6 ['class_time']['java with dsa and system design']


# In[41]:


#how to add new key in previous term  , if the key is already available then is override or change new one
d6['mentor'] = ['sudhanshu','krish','anurag' , 'haider']


# In[42]:


d6


# In[43]:


#how to delete key 
del d6['number']


# In[44]:


d6


# In[46]:


#how gets keys
d6.keys()


# In[47]:


#to make proper lists form then, 
list(d6.keys())


# In[51]:


# how to gets values 
d6.values()


# In[52]:


#only gets values 
list(d6.values())


# In[53]:


#how to gets pair of values and keys  ,both 
d6.items()


# In[54]:


list(d6.items())


# In[55]:


#to remove
d6.pop('assignment')


# In[56]:


d6


# In[57]:


#always assign arguments 
d6.pop()


# In[59]:


#suppose 
marks = 65
if marks >= 80:
    print("you will be a part of A0 batch")
elif marks >= 60 and marks <80:
    print("you will be a part of A1 batch")
elif marks >=40 and marks <60:
    print("you will be a part of A2 batch")
else :
    print ("you will be a part of A3 batch ")


# In[1]:


# in case of "and" conditions 
# 1 and 1 = 0 
# 1 and 0 = 0 
# 0 and 1 = 0 
# 0 and 0 = 0


# In[3]:


# input operation has one problem it convert all things into srings 
marks = input ("enter your marks")


# In[4]:


marks


# In[5]:


type(marks)


# In[6]:


# to change string into integers we need to use type casting  or we need to change into just put it flot(input("enter your marks "))


# In[8]:


markss = int(input("enter your marks"))


# In[9]:


marks


# In[10]:


type(marks)


# In[13]:


price = int(input("enter price"))
if price > 1000:
    print("i will not purchase")
else :
    print("i will purchase")


# In[15]:


# if contion is not satisfied then i will not print 
price = int(input("enter price"))
if price> 1000:
    print("i will not purchase")


# In[16]:


# if we take two times " if " then , it will print in sequence order basecilly python write always in order
price = int(input("enter price "))
if price > 1000:
    print(" i will not purchse")
    if price > 5000:
        print("price is too much")


# In[25]:


# how to add ,but it takes lots of time 
l = [1,2,3,4,5,6,7,8]


# In[26]:


l[0]+1


# In[27]:


l2 = []


# In[28]:


l2.append(l[0]+1)


# In[29]:


l2


# In[30]:


# to add in a simple way we need loop concept
ll = [1,2,3,4,5,6,7,8,9]


# In[31]:


for i in ll:
    print(i)


# In[32]:


for i in ll:
    print(i+1)


# In[35]:


l1 = []
for i in ll :
    print(i+1)
    l1.append(i+1)
l1


# In[36]:


l = ["anand","kumar","pwskills","course"]


# In[42]:


l1 =[]
for i in l:
    print(i)
    l1.append(i.upper())


# In[43]:


l1


# In[44]:


# how to make two seperate data list 1 = integer and 2 =  string
l = [1,2,3,4,5,6,7,8,"anand","kumar", 324, 34.456,"abc"]


# In[48]:


l1_num = []
l2_str = []
for i in l :
    if type(i) == int or type(i) == float :
        l1_num.append(i)
    else:
        l2_str.append(i)


# In[49]:


l1_num


# In[50]:


l2_str


# In[ ]:




