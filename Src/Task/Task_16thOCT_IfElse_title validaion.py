

# Q2- In automation, you often compare expected and actual outputs.
# Write code to check if a test case passed or failed.
#
# expected_title = "Dashboard"
# actual_title = "Dashboard "
#
# ✅ Test Passed – Title matches
#
#
# True - why >  Strip and convert them into the lowercase = both of them are equal.


actual_title=input("Enter the  actual title").strip()
expected_title=input("Enter the expected title").strip()
if expected_title.lower()==actual_title.lower():
    print("The title is correct")
else:
    print("The title is not correct")

