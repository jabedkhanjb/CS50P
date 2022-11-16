score = int(input("Enter your mark : "))

# if 90<= score and score <=100:
if score >= 90 and score <= 100:
    print("Grade : A+")

elif score > 100:
    print("Your marks is not appropriate.")

# elif 80<= score and score <90:
elif score >= 80:
    print("Grade : A")

# elif 70<= score and score <80:
elif score >= 70:
    print("Grade : A-")

# elif 60<= score and score <70:
elif score >= 60:
    print("Grade : B")

# elif 50<= score and score <60:
elif score >= 50:
    print("Grade : C")

# elif 40<= score and score <50:
elif score >= 40:
    print("Grade : D")

# elif 33<= score and score <40:
elif score >= 33:
    print("Grade : D-")

elif score <33:
    print("You failed.")

else:
    print("Something went wrong.")
