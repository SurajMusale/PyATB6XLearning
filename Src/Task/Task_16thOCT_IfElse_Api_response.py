"""Q - You receive an API response code from your test script.
Write an if-else block to check whether the response is successful (status code 200) or not.

I/P response = 404 , O/P ❌ Failed API Request
I/P response = 200 , O/P ✅ Passed API Request"""

Api_Response=int(input("Enter the response code: "))
if Api_Response==200:
    print("passed API request",200,"ok")
elif Api_Response==404:
    print("Failed API request",404)
else:
    print("enter valid response")

