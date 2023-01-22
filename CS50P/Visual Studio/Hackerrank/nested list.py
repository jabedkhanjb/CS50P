if __name__ == '__main__':
    grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades.append([name,score])
    
    student_score = sorted(set([grade[1] for grade in grades]))
    student_name = sorted([grade[0] for grade in grades if grade[1]==student_score[1]])
    for name in student_name:
       print(name)