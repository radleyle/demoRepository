# Student Grade Tracker 

DATA_FILE = "grades.txt"

def load_data():
    data = {}
    try:
        with open(DATA_FILE, "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(",")
                course_name = parts[0]
                assignments_str = parts[1].split(";")
                exams_str = parts[2].split(";")

                assignments = []
                for assignment_str in assignments_str:
                    assignment = None
                    if assignment_str.strip().isdigit():
                        assignment = float(assignment_str.strip())
                    if assignment is not None:
                        assignments.append(assignment)

                exams = []
                for exam_str in exams_str:
                    exam = None
                    exam_str_strip = exam_str.strip().replace(".", "", 1)
                    if exam_str_strip.isdigit():
                        exam = float(exam_str_strip)
                    if exam is not None:
                        exams.append(exam)

                data[course_name] = {"assignments": assignments, "exams": exams}
    except FileNotFoundError:
        pass
    return data

def save_data(data):
    with open(DATA_FILE, "w") as file:
        for course_name in data:
            grades = data[course_name]

            assignments_str_list = []
            for grade in grades["assignments"]:
                assignments_str_list.append(str(grade))

            exams_str_list = []
            for grade in grades["exams"]:
                exams_str_list.append(str(grade))

            assignments_str = ";".join(assignments_str_list)
            exams_str = ";".join(exams_str_list)

            file.write(f"{course_name},{assignments_str},{exams_str}\n")

def add_course(data):
    course_name = input("Enter the course name: ")
    if course_name in data:
        print(f"Course '{course_name}' already existed.")
    else:
        data[course_name] = {"assignments": [], "exams": []}
        save_data(data)
        print(f"Course '{course_name}' added successfully.")

def remove_course(data):
    course_name = input("Enter the course name to remove: ")
    if course_name in data:
        del data[course_name]
        save_data(data)
        print(f"Course '{course_name}' removed successfully.")
    else:
        print("Course not found.")

def add_grade(data):
    course_name = input("Enter the course name: ")
    if course_name not in data:
        print("Course not found.")
        return
    grade_type = input("Enter grade type (assignment/exam): ").lower()
    if grade_type not in ("assignment", "exam"):
        print("Invalid grade type.")
        return
    grade = float(input("Enter grade: "))
    data[course_name][f"{grade_type}s"].append(grade)
    save_data(data)
    print(f"{grade_type.capitalize()} grade added successfully.")

def calculate_course_grade(course_data):
    try:
        total_assignments = sum(course_data["assignments"])
        total_exams = sum(course_data["exams"])
        total_grades = total_assignments + total_exams
        course_grade = total_grades / (len(course_data["assignments"]) + len(course_data["exams"]))

        if 93 <= course_grade <= 100:
            return course_grade, 'A'
        elif 90 <= course_grade <= 92:
            return course_grade, 'A-'
        elif 87 <= course_grade <= 89:
            return course_grade, 'B+'
        elif 83 <= course_grade <= 86:
            return course_grade, 'B'
        elif 80 <= course_grade <= 82:
            return course_grade, 'B-'
        elif 77 <= course_grade <= 79:
            return course_grade, 'C+'
        elif 73 <= course_grade <= 76:
            return course_grade, 'C'
        elif 70 <= course_grade <= 72:
            return course_grade, 'C-'
        elif 67 <= course_grade <= 69:
            return course_grade, 'D+'
        elif 63 <= course_grade <= 66:
            return course_grade, 'D'
        elif 60 <= course_grade <= 62:
            return course_grade, 'D-'
        else:
            return course_grade, 'F'

    except ZeroDivisionError:
        pass
    return None, None

def generate_grade_report(data):
    print("Grade Report:")
    for course in data:
        grades = data[course]
        course_grade, letter_grade = calculate_course_grade(grades)
        if course_grade is not None:
            print(f"Course: {course}")
            print(f"Average Grade: {course_grade:.2f} ({letter_grade})")
            print()
        else:
            print(f"Course: {course}")
            print("No grades available.")
            print()

def main():
    data = load_data()

    while True:
        print("\nStudent Grade Tracker")
        print("1. Add new course")
        print("2. Remove course")
        print("3. Add grade")
        print("4. Generate grade report")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_course(data)
        elif choice == "2":
            remove_course(data)
        elif choice == "3":
            add_grade(data)
        elif choice == "4":
            generate_grade_report(data)
        elif choice == "5":
            print("Exiting program...")
            with open(DATA_FILE, "w"):
                pass
            break
        else:
              print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
