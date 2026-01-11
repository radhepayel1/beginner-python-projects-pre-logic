# %%
# c1 details
c1_name = "Rohit Mondal"
c1_ph = 7550899670
c1_city = "Mayapur"
c1_email_1= "rohit6mondal@gmail.com"
c1_email_2= "rohit6mond@gmail.com"

# c2 details
c2_name = "Purabi Mondal"
c2_ph = 8907654321
c2_city = "Mayapur"
c2_email_1= "purabi.8mondal@gmail.com"
c2_email_2= "pur.89mondal@gmail.com"

#c3 details
c3_name = "Piyali Nandy"
c3_ph = 8765432109
c3_city = "Mumbai"
c3_email_1= "piyali.n9@gmail.com"
c3_email_2= "piu.n98@gmail.com"
# %%
#c1 data store
data_c1= {
    "name": c1_name,
    "info": (c1_ph, c1_city),
    "email id": [c1_email_1, c1_email_2]
}

#c2 data store
data_c2= {
    "name": c2_name,
    "info": (c2_ph, c2_city),
    "email id": [c2_email_1, c2_email_2]
}

#c3 data store
data_c3= {
    "name": c3_name,
    "info": (c3_ph, c3_city),
    "email id": [c3_email_1, c3_email_2]
}
# %%
print("_____Contact_1________")
print("Name:", data_c1["name"])
print("Contact Number:" , data_c1["info"][0])
print("City:", data_c1["info"][1])
print("Email id:" , data_c1["email id"][0])
print("         " , data_c1["email id"][1])


print("_____Contact_2________")
print("Name:", data_c2["name"])
print("Contact Number:" , data_c2["info"][0])
print("City:", data_c2["info"][1])
print("Email id:" , data_c2["email id"][0])
print("         " , data_c2["email id"][1])


print("_____Contact_3________")
print("Name:", data_c3["name"])
print("Contact Number:" , data_c3["info"][0])
print("City:", data_c3["info"][1])
print("Email id:" , data_c3["email id"][0])
print("         " , data_c3["email id"][1])
# %%
