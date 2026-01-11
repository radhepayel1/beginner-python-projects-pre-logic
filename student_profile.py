# %%
# students name
Student1 = input()
Student2 = input()
Student3 = input()
Student4 = input()
Student5 = input()
# %%
# roll numbers
s1_roll = input()
s2_roll = input()
s3_roll = input()
s4_roll = input()
s5_roll = input()
# %%
# age
s1_age = input()
s2_age = input()
s3_age = input()
s4_age = input()
s5_age = input()
# %%
# city
s1_city=input()
s2_city=input()
s3_city=input()
s4_city=input()
s5_city=input()
# %%
# Marks in 3 subjects
s1_Math= input()
s2_Math= input()
s3_Math= input()
s4_Math= input()
s5_Math= input()
s1_Bio= input()
s2_Bio= input()
s3_Bio= input()
s4_Bio= input()
s5_Bio= input()
s1_Eng= input()
s2_Eng= input()
s3_Eng= input()
s4_Eng= input()
s5_Eng= input()
# %%
# Profile of Student 1
Data_s1= {
    "name" : Student1,
    "info" : (("roll",s1_roll),
              ("age",s1_age)),
    "marks": [["Math",s1_Math],
              ["Bio",s1_Bio ],
              ["Eng",s1_Eng]],
    "city": s1_city
}

# Profile of Student 2
Data_s2= {
    "name" : Student2,
    "info" : (("roll",s2_roll),
              ("age",s2_age)),
    "marks": [["Math",s2_Math],
              ["Bio",s2_Bio ],
              ["Eng",s2_Eng]],
    "city": s2_city
}

# Profile of Student 3
Data_s3= {
    "name" : Student3,
    "info" : (("roll",s3_roll),
              ("age",s3_age)),
    "marks": [["Math",s3_Math],
              ["Bio",s3_Bio ],
              ["Eng",s3_Eng]],
    "city": s3_city
}

# Profile of Student 4
Data_s4= {
    "name" : Student4,
    "info" : (("roll",s4_roll),
              ("age",s4_age)),
    "marks": [["Math",s4_Math],
              ["Bio",s4_Bio ],
              ["Eng",s4_Eng]],
    "city": s4_city
}

# Profile of Student 5
Data_s5= {
    "name" : Student5,
    "info" : (("roll",s5_roll),
              ("age",s5_age)),
    "marks": [["Math",s5_Math],
              ["Bio",s5_Bio ],
              ["Eng",s5_Eng]],
    "city": s5_city
}
# %%
print("_____STUDENT 1 PROFILE_____")
print("Name:", Data_s1["name"])
print("Roll:", Data_s1["info"][0][1])
print("Age:", Data_s1["info"][1][1])
print("City:", Data_s1["city"])
print("Marks:")
print(" ", Data_s1["marks"][0][0], ":", Data_s1["marks"][0][1])
print(" ", Data_s1["marks"][1][0], ":", Data_s1["marks"][1][1])
print(" ", Data_s1["marks"][2][0], ":", Data_s1["marks"][2][1])

print("_______________")

print("_____STUDENT 2 PROFILE_____")
print("Name:", Data_s2["name"])
print("Roll:", Data_s2["info"][0][1])
print("Age:", Data_s2["info"][1][1])
print("City:", Data_s2["city"])
print("Marks:")
print(" ", Data_s2["marks"][0][0], ":", Data_s2["marks"][0][1])
print(" ", Data_s2["marks"][1][0], ":", Data_s2["marks"][1][1])
print(" ", Data_s2["marks"][2][0], ":", Data_s2["marks"][2][1])

print("_______________")

print("_____STUDENT 3 PROFILE_____")
print("Name:", Data_s3["name"])
print("Roll:", Data_s3["info"][0][1])
print("Age:", Data_s3["info"][1][1])
print("City:", Data_s3["city"])
print("Marks:")
print(" ", Data_s3["marks"][0][0], ":", Data_s3["marks"][0][1])
print(" ", Data_s3["marks"][1][0], ":", Data_s3["marks"][1][1])
print(" ", Data_s3["marks"][2][0], ":", Data_s3["marks"][2][1])

print("________________")

print("_____STUDENT 4 PROFILE_____")
print("Name:", Data_s4["name"])
print("Roll:", Data_s4["info"][0][1])
print("Age:", Data_s4["info"][1][1])
print("City:", Data_s4["city"])
print("Marks:")
print(" ", Data_s4["marks"][0][0], ":", Data_s4["marks"][0][1])
print(" ", Data_s4["marks"][1][0], ":", Data_s4["marks"][1][1])
print(" ", Data_s4["marks"][2][0], ":", Data_s4["marks"][2][1])

print("________________")

print("_____STUDENT 5 PROFILE_____")
print("Name:", Data_s5["name"])
print("Roll:", Data_s5["info"][0][1])
print("Age:", Data_s5["info"][1][1])
print("City:", Data_s5["city"])
print("Marks:")
print(" ", Data_s5["marks"][0][0], ":", Data_s5["marks"][0][1])
print(" ", Data_s5["marks"][1][0], ":", Data_s5["marks"][1][1])
print(" ", Data_s5["marks"][2][0], ":", Data_s5["marks"][2][1])
# %%
