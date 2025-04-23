#Program 6: Dictionary of Student Records

students = {
    101: {"name": "Ram", "grade": "A+", "Attendance": 91},
    102: {"name": "Daya", "grade": "A", "Attendance": 84},
    103: {"name": "RohitKaustubh", "grade": "C", "Attendance": 75}
}

#Add a new student
students[104] = {"name": "Sagar", "grade": "B", "Attendance": 69}

#Update a grade of a student
students[101]["grade"] = "A"

#Display all students records
for students_id, details in students.items():
    print(f"ID: {students_id}, Name: {details['name']}, Grade: {details['grade']}, Attendance: {details['Attendance']}" )
