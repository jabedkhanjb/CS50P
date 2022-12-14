def DecimalToBinary(number):
    if number >= 1:
        DecimalToBinary(number / 2)
    print(number % 2, end="")


DecimalToBinary(number=int(input("Enter a decimal number: ")))
