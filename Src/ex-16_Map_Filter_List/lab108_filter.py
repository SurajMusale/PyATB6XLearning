test_result=["pass","fail","skip","Fail"]

pass_give=list(filter(lambda x:x=="pass",test_result))
print(pass_give)