
#Q4-
"""Check if the user can log in based on correct username and password.

I/p

username = "admin"
password = "1234"

O/p
✅ Login Successful


For the Fail condition Other O/"""

username=input("Enter your username: ").strip()
password=input("Enter your password: ").strip()

if username=="admin" and password=="1234":
    print("Login Successful")
else:
    print("Login Failed--invalid credentials")