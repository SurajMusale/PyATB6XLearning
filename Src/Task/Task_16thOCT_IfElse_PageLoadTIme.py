
# Q3- You want to check whether a web page loads within 3 seconds (performance test condition).
#
# load_time = 4.2
# ⚠️ Page load too slow: 4.2 seconds

load_time=float(input("Enter load time: "))
if load_time<=0:
    print("enter valid load time")
elif load_time<=3:
    print("The page load within 3 second")
else:
    print("The page is not loading")


