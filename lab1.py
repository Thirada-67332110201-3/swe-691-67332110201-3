def calculate_grade(scores):
    total = 0
    for score in scores:
        total = total + score
    
    # Bug: หาก scores เป็นลิสต์ว่าง [] จะเกิด ZeroDivisionError
    average = total / len(scores)

    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"
    return grade, average

# กรณีที่ 1: มีคะแนนปกติ
scores = [85, 92, 78, 88, 95]
print(f"Normal Case: {calculate_grade(scores)}")

# ขั้นที่ 4: ลองกรณีที่ AI มักลืม (ลิสต์ว่าง)
# print(calculate_grade([])) # ถ้าเอาคอมเมนต์ออก จะเจอ Error: division by zero

