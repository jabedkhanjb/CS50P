# i = 1
# while i < 3:
#     try:
#         x = int(input("What's x?\n> "))
#         print(f"Your given number is {x}")
#     except ValueError:
#         print("x is not an integer.")
#         if i == 1:
#             print(f"{i}st attempt failed.")
#         else:
#             print(f"{i}nd attempt failed.")
#     else:
#         break

i = 1

while i <= 3:
    try:
        x = int((input("What's x?\n> ")))
        print(f"You have inputed {x}")
            
    except ValueError:
        print("x is not integer.")
        if i == 1:
             print(f"{i}st attempt failed.")
        else:
            print(f"{i}nd attempt failed.")
        i += 1