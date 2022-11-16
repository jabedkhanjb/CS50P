print(
"""
****************************************************
****************** Admission Form ******************
****************************************************
"""
)
name = input("Student name: ").strip().title()

name2 = input("Father name: ").strip().title()

name3 = input("Mother name: ").strip().title()

# academy
academy = int(input("Last Academic year: "))

academy2 = float(input("SSC Gpa: "))
academy3 = float(input("HSC Gpa: "))
academytotal = academy2 + academy3

if academy < 2017:
    print("Sorry, We don't allow students who has more than 4 years academic study gap.")
    exit()
if academytotal < 7.00:
        print("Sorry your result didn't meet our admission criteria.")
else:
    print(f"Congratulate {name}, We approved your admission.")
    print(
    """
    ****************************************************
    ********** Admission Approval Information **********
    ****************************************************
    """
    )
    print(f"Student      : {name}")
    print(f"Father       : {name2}")
    print(f"Mother       : {name3}")
    print(f"SSC          : {academy2}")
    print(f"HSC          : {academy3}")
    print(f"Passing Year : {academy}")