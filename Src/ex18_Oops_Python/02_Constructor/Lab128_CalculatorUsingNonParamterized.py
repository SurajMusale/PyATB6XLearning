class calculator:
    a=None
    b=None

    def __init__(self):
        print("DC")
    def sum(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mult(self,a,b):
     return a*b
    def div(self,a,b):
        return a/b


a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
result = calculator()

sum_result=result.sum(a,b)
sub_result=result.sub(a,b)
mult_result=result.mult(a,b)
div_result=result.div(a,b)

print(sum_result,sub_result,mult_result,div_result)
