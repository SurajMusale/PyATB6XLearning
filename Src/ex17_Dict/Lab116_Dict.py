dict1={"a":1,"b":2,"c":3}
print(dict1.keys())
print(dict1.values())

dict2={"a":1,"b":2}

missng_keys=(dict1.keys()-dict2.keys())
print(missng_keys)