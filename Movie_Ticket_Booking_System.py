# %%
#Customer Details
c1= "Madhav"
c2= "Raikishori"
c3= "Lalita Sakhi"""
# %%
#contact number
c1_ph= 9087654321
c2_ph= 8901234567
c3_ph= 7098563412
# %%
# movie details
m1= "Border 2"
m2= "Avtar 2"
m3= "Dhurandhar"
# %%
#ticket price & Number of details
m1_price= 250
m2_price= 175
m3_price= 390
m1_ticket_no= 2
m2_ticket_no =1
m3_ticket_no= 4
# %%
# total amt of each customer
b1= m1_price * m1_ticket_no
b2= m2_price * m2_ticket_no
b3= m3_price * m3_ticket_no
# %%
#data store of c1
data_c1= {
    "name":c1,
    "ph_no":c1_ph,
    "booking":(m1, m1_price,m1_ticket_no)
}
# %%
#data store of c2
data_c2= {
    "name":c2,
    "ph_no":c2_ph,
    "booking":(m2, m2_price,m2_ticket_no)
}
# %%
#data store of c3
data_c3= {
    "name":c3,
    "ph_no":c3_ph,
    "booking":(m3, m3_price,m3_ticket_no)
}
# %%
#Final Output of C1
print("___Movie Ticket C1___")
print("Name:", data_c1["name"])
print("Contact:", data_c1["ph_no"])
print(" "
      " ")
print("Movie:", data_c1["booking"][0])
print("Price:", data_c1["booking"][1])
print("Ticket:", data_c1["booking"][2])
print("Total:", b1)
print(" "
      " ")
#Final Output of C2
print("___Movie Ticket C2___")
print("Name:", data_c2["name"])
print("Contact:", data_c2["ph_no"])
print(" "
      " ")
print("Movie:", data_c2["booking"][0])
print("Price:", data_c2["booking"][1])
print("Ticket:", data_c2["booking"][2])
print("Total:", b2)
print(" "
      " ")
#Final Output of C3
print("___Movie Ticket C3___")
print("Name:", data_c3["name"])
print("Contact:", data_c3["ph_no"])
print(" "
      " ")
print("Movie:", data_c3["booking"][0])
print("Price:", data_c3["booking"][1])
print("Ticket:", data_c3["booking"][2])
print("Total:", b3)
print(" "
      " ")
# %%
