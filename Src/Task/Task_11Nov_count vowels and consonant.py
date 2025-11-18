# Question - ✅ Count vowels and consonants in a String

value=input("Enter string")# delcare input
vowels="aeiou"
count_vowels=0
count_consonants=0

for char in value:
    if char in vowels:
        count_vowels+=1
    elif char.isalpha():
        count_consonants+=1

print("Vowels count in string: ", count_vowels)
print("Consonants in string: ", count_consonants)








