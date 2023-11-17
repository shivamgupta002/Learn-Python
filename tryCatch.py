# try:
#     a=int(input("Enter your number = "))
#     print(a+3)
# except:
#     print("Some error Occurred")

# ---------------------------------------------------------

try:
    a=int(input("Enter your number = "))
    print(a+3)
except Exception as e:
    print("Some error Occurred",e)