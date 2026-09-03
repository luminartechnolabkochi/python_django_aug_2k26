"""
✅ 3. Login System with Password and OTP

Task:
Ask for password.

If password is correct:

Ask for OTP

If OTP is correct → "Login successful"

Else → "Incorrect OTP"


Else → "Incorrect password"

"""

db_password = "password123"

db_otp=7890

password = input("enter password... ")

if db_password == password:

    otp = int(input("enter otp..."))

    if otp == db_otp:

        print("login success")
    else:

        print("invalid otp")

else:
    print("inavlid password")

