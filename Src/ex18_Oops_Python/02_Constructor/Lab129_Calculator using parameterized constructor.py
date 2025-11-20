class calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def sum(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b

result=calc(1,2)
print(result.sum())
print(result.sub())
print(result.mul())
print(result.div())