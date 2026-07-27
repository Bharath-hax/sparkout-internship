students = [
    [101, "Alice", 85],
    [102, "Bob", 72],
    [103, "Charlie", 95],
    [104, "David", 88],
    [102, "Bob", 72]
]

def add_student(roll, name, marks):
    students.append([roll, name, marks])

def display_students():
    print("Roll\tName\t\tMarks")
    for student in students:
        print(f"{student[0]}\t{student[1]}\t\t{student[2]}")

def update_marks(roll, new_marks):
    for student in students:
        if student[0] == roll:
            student[2] = new_marks

def delete_student(roll):
    for student in students:
        if student[0] == roll:
            students.remove(student)
            break

def sort_by_marks():
    students.sort(key=lambda x: x[2], reverse=True)

def top_performer():
    highest = max(student[2] for student in students)
    print("\nTop Performer(s):")
    for student in students:
        if student[2] == highest:
            print(student)

def remove_duplicates():
    unique = []
    seen = set()
    for student in students:
        key = tuple(student)
        if key not in seen:
            seen.add(key)
            unique.append(student)
    students.clear()
    students.extend(unique)

display_students()

remove_duplicates()
add_student(105, "Eva", 91)
update_marks(102, 80)
delete_student(104)
sort_by_marks()

print("\nFinal Student Records:")
display_students()

top_performer()