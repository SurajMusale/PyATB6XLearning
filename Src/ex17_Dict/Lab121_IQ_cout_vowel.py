input_string = "hello, world!"
# a,e, i,o,u.
# vowel ?

vowels = "aeiou"

vowels_Count=0
result=dict()

for char in input_string:
    if char in vowels:
        vowels_Count+=1
print(vowels_Count)