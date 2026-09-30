username=input("Enter username:")
password=input("Enter password:")

if username=="admin" and password=="1234":
    print("Login successfully completed")

elif username!="admin" and password!="1234":
    print("Use valid username and password")

elif username!="admin":
    print("Invalid username")

elif password!="1234":
    print("Invalid password")