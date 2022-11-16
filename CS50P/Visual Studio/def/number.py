def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)


add(10, 20)
add(20, 30, 50)
add(50, 60, 90)