# x = int(input("What's X? "))
# if x % 2 == 0:
#     print(f"{x} is an Even number.")

# else:
#     print(f"{x} is an Odd number.")
def main():
    x = int(input("What's X? "))
    if is_even(x):
        print(f"{x} is an Even number.")
    else:
        print(f"{x} is an Odd number.")

def is_even(n):
    return n % 2 == 0
    # return True if n % 2 == 0 else False

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

main()