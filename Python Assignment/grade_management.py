#declaring a dictionary to hold student records
student_records = {}

# Defining a function to add grades to student records
def add_grade(student_name, grade):
    if student_name in student_records:
        student_records[student_name].append(grade)
    else:
        student_records[student_name] = [grade]

#inputting grades from user
while True:
    name = input("Enter student name (or 'exit' to stop): ")
    if name.lower() == 'exit':
        break
    try:
        grade = float(input(f"Enter grade for {name}: "))
        add_grade(name, grade)
    except ValueError:
        print("Invalid grade. Please enter a numeric value.")
        
#printing class average
total_grades = sum(sum(grades) for grades in student_records.values())
total_count = sum(len(grades) for grades in student_records.values())
if total_count > 0:
    class_average = total_grades / total_count
    print(f"Class Average: {class_average:.2f}")
        
print("Student Records:", student_records) 