# Question 3 :
#
# Simulate a page loading check using a while loop.
# If page_loaded becomes True within 5 seconds, print success; else timeout.
#
# Hint: Use a counter (like wait_time) and break condition.

page_load=1

while(page_load <=5):
    num=int(input("Enter the page load number: ").strip())
    if num==5:
        print("Success")
        break
    else:
        print("Timeout")