# frequencey of char in a string


string=input("Enter a string: ")

char_Count={} # it si dictonay

for char in string:
    char_Count[char]=char_Count.get(char,0)+1
print(char_Count)