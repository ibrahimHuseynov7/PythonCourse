
grades = {
    "Tural": [90, 85, 78],
    "Aytac": [95, 88, 92],
    "Vusal": [70, 80, 65]
}


for students, grades in grades.items():
    avg = sum(grades) / len(grades)
    print(f"{students} average grades: {avg:.2f}")
