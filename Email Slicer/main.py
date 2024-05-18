print("Welcome From Thaw's Email Slicer ")
email_input = input("Enter Email : ")
(username,domain) = email_input.split("@")
(company,ext) = domain.split(".")

print(f"name is : {username} ")
print(f"doamin is : {company}")
print(f"extension is : {ext}")