
def manage_student_database():
    students = []
    student_id = 1

    while True:
        name = input("Please enter the student's name (or type 'stop' to finish): ").strip()

        if name.lower() == "stop":
            break

        # Check for duplicate names
        if any(student_name == name for _, student_name in students):
            print("This name is already in the list.")
        else:
            students.append((student_id, name))
            student_id += 1

    # Display the complete list of student tuples
    print("\nComplete List of Students (Tuples):")
    print(students)

    # Display each student's ID and name individually
    print("\nList of Students with IDs:")
    for sid, name in students:
        print(f"ID: {sid}, Name: {name}")

    # Total number of students
    total_students = len(students)
    print(f"\nTotal number of students: {total_students}")

    # Calculate the total length of all student names combined
    total_length = sum(len(name) for _, name in students)
    print(f"Total length of all student names combined: {total_length}")

    # Identify the student with the longest and shortest name
    if students:
        longest_name_student = max(students, key=lambda student: len(student[1]))[1]
        shortest_name_student = min(students, key=lambda student: len(student[1]))[1]

        print(f"The student with the longest name is: {longest_name_student}")
        print(f"The student with the shortest name is: {shortest_name_student}")

# Call the function to run the program
manage_student_database()
