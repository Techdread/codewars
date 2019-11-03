def get_grade(s1, s2, s3):
    avg = (s1 + s2 + s3) / 3
    if (avg >= 90):
        return "A"
    elif (avg >= 80):
        return "B"
    elif (avg >= 70):
        return "C"
    elif (avg >= 60):
        return "D"
    return "F"

print(get_grade(95, 90, 93))
print(get_grade(70, 70, 100))
print(get_grade(60, 82, 76))
print(get_grade(66, 62, 68))
print(get_grade(48, 55, 52))