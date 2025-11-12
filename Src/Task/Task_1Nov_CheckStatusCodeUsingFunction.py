# #🧩 1️⃣ Write a Function to Check Test Case Status
#
# Problem:
#
# Write a function check_status(status_code) that returns:
#
# "PASS" if status_code = 200
#
# "FAIL" if status_code = 400 or 500
#
# "UNKNOWN" otherwise
#
# Example Input & Output:
#
# print(check_status(200))   # PASS
#
# print(check_status(500))   # FAIL
#
# print(check_status(302)

status=int(input("Enter status_Code"))
def check_test_case_status(status_code):

    if status_code>0:
        if status_code==200:
            print("Test Case Status: Passed")
        elif status_code==400 or status_code==500:
            print("Test Case Status: Failed")
        else:
            print("Unknown status code")

check_test_case_status(status)