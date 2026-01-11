#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Takes details of 3 customers
c1= "Bisea Rozy"
c2= "Maria"
c3= "Harry Potter"
c1_no= 9087654321
c2_no= 7890543210
c3_no= 9087654321


# In[2]:


#c1 item store
c1item1= (("name", "Marry Gold"),("price", 20), ("quantity", 5))
c1item2= (("name", "Lays"),("price", 50), ("quantity", 2))
c1item3= (("name", "Dairy Milk"),("price", 10), ("quantity", 5))

#c2 item store
c2item1= (("name", "Goodday Chocolate Cookies"),("price", 20), ("quantity", 5))
c2item2= (("name", "Sugar Lipstick"),("price", 699), ("quantity", 1))
c2item3= (("name", "Bottle"),("price", 100), ("quantity", 1))

#c3 item store
c3item1= (("name", "Goodday Chocolate Cookies"),("price", 10), ("quantity", 3))
c3item2= (("name", "Perfume"),("price", 349), ("quantity", 1))
c3item3= (("name", "Dress"),("price", 1000), ("quantity", 1))


# In[3]:


# Data Store of c1:
data_c1={
    "name": c1,
    "items": (c1item1, c1item2, c1item3),
    "contact": c1_no
}
# Data Store of c2:
data_c2={
    "name": c2,
    "items": (c2item1, c2item2, c2item3),
    "contact": c2_no
}
# Data Store of c3:
data_c3={
    "name": c3,
    "items": (c3item1, c3item2, c3item3),
    "contact": c3_no
}


# In[4]:


# c1 item
c1_item1_total= c1item1[1][1]*c1item1[2][1]
c1_item2_total= c1item2[1][1]*c1item2[2][1]
c1_item3_total= c1item3[1][1]*c1item2[2][1]
t1= c1_item1_total+c1_item2_total+c1_item3_total
#c2 item
c2_item1_total= c2item1[1][1]*c2item1[2][1]
c2_item2_total= c2item2[1][1]*c2item2[2][1]
c2_item3_total= c2item3[1][1]*c2item2[2][1]
t2= c2_item1_total+c2_item2_total+c2_item3_total
#c3 item
c3_item1_total= c3item1[1][1]*c3item1[2][1]
c3_item2_total= c3item2[1][1]*c3item2[2][1]
c3_item3_total= c3item3[1][1]*c3item2[2][1]
t3= c3_item1_total+c3_item2_total+c3_item3_total


# In[6]:


# Shopping Bill Final Output:c1
print("=== Bill : C1 ===")
print("Name:" , data_c1["name"])
print("Customer Number:" , data_c1["contact"])

#Item 1:
print("Item 1:")
print("", data_c1["items"][0][0][1])
print(" Price:", data_c1["items"][0][1][1])
print(" Quantity:", data_c1["items"][0][2][1])

# Item 2:
print("Item 2:")
print("", data_c1["items"][1][0][1])
print(" Price:", data_c1["items"][1][1][1])
print(" Quantity:", data_c1["items"][1][2][1])
# Item 3:
print("Item 3:")
print("", data_c1["items"][2][0][1])
print(" Price:", data_c1["items"][2][1][1])
print(" Quantity:", data_c1["items"][2][2][1])
print("""
      """)
print("Total:", t1)

# Shopping Bill Final Output:c2
print("=== Bill : C2 ===")
print("Name:" , data_c2["name"])
print("Customer Number:" , data_c2["contact"])

#Item 1:
print("Item 1:")
print("", data_c2["items"][0][0][1])
print(" Price:", data_c2["items"][0][1][1])
print(" Quantity:", data_c2["items"][0][2][1])

# Item 2:
print("Item 2:")
print("", data_c2["items"][1][0][1])
print(" Price:", data_c2["items"][1][1][1])
print(" Quantity:", data_c2["items"][1][2][1])
# Item 3:
print("Item 3:")
print("", data_c2["items"][2][0][1])
print(" Price:", data_c2["items"][2][1][1])
print(" Quantity:", data_c2["items"][2][2][1])
print("""
      """)
print("Total:", t2)

# Shopping Bill Final Output:c3
print("=== Bill : C1 ===")
print("Name:" , data_c3["name"])
print("Customer Number:" , data_c3["contact"])

#Item 1:
print("Item 1:")
print("", data_c3["items"][0][0][1])
print(" Price:", data_c3["items"][0][1][1])
print(" Quantity:", data_c3["items"][0][2][1])

# Item 2:
print("Item 2:")
print("", data_c3["items"][1][0][1])
print(" Price:", data_c3["items"][1][1][1])
print(" Quantity:", data_c3["items"][1][2][1])
# Item 3:
print("Item 3:")
print("", data_c3["items"][2][0][1])
print(" Price:", data_c3["items"][2][1][1])
print(" Quantity:", data_c3["items"][2][2][1])
print("""
""")
print("Total:", t3)


# In[ ]:




