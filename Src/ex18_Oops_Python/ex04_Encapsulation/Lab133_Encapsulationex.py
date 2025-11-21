class vwologinpage:
    def __init__(self,email_arg,password_Arg):
        self.email_arg=email_arg
        self.password_Arg=password_Arg
    def Login_Confirm(self):
        if self.email_arg=="suraj@gmail.com" and  self.password_Arg=="pass123":
            print("Login Successful")
        else:
            print("Login Failed")

email=input("Enter your email: ")
password=input("Enter your password: ")

vwo_object_ref=vwologinpage(email,password)
vwo_object_ref.Login_Confirm()
