# Nested dictionary yaradılır
students= {
    "Ali": {
        "math": 85,
        "physics": 78
    },
    "Vusal": {
        "Principles of Finance": 88
    }
}


students["Ali"].update({"math": 90})


students["Vusal"].setdefault("chemistry", 80)


print(students)
