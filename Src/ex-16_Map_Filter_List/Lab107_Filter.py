nums=[1,2,3,4,5]

def even_num(x):
    return x%2==0

print_even_no=list(filter(even_num,nums))
print(print_even_no)
