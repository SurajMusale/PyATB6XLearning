# Question - ✅Palidrome of String
# 🧩 Example Walkthrough
# Let’s take the word "level":
# Forward: "level"
# Backward: "level"
# Both are identical → Palindrome ✅
# Now, "hello":
# Forward: "hello"
# Backward: "olleh"
# Not the same → Not a palindrome


Value=input("Enter a string: ")

rev=""

for char in Value:
    rev=char+rev
if Value==rev:
    print("The string is Pallindrome", Value)
else:
    print("The string is not Pallindrome", Value)
