
    
# ==========================================================
#              STUDENT MANAGEMENT SYSTEM
# ==========================================================

students = []


# ==========================================================
#                    MAIN MENU
# ==========================================================

print("\n======================================")
print("       STUDENT MANAGEMENT SYSTEM")
print("======================================")

print("1. Add Student")
print("2. View Students")
print("3. Search Student")
print("4. Marks & Average")
print("5. Delete Student")
print("6. Exit")


while True:

    choice = input("\nEnter Your Choice: ")


    # ======================================================
    # 1. ADD STUDENT
    # ======================================================

    if choice == "1":

        print("\n===== ADD STUDENT =====")

        name = input("Enter Student Name: ")
        roll = input("Enter Roll Number: ")
        semester = int(input("Enter Your Semester: "))
        department = input("Enter Department: ")

        subjects = {}

        exam_marks = float(
            input("Exam is out of how many marks? ")
        )

        number = int(
            input("How many subjects? ")
        )


        # Enter subject marks

        for i in range(number):

            subject = input(
                f"Enter Subject {i + 1}: "
            )

            marks = float(
                input(f"Enter Marks for {subject}: ")
            )

            subjects[subject] = marks


        # Calculate total

        total = sum(subjects.values())


        # Calculate average

        average = total / number


        # Calculate percentage

        percentage = (
            total / (number * exam_marks)
        ) * 100


        # Create student dictionary

        student = {

            "name": name,
            "roll": roll,
            "semester": semester,
            "department": department,
            "subjects": subjects,
            "total": total,
            "average": average,
            "percentage": percentage

        }


        # Add student to list

        students.append(student)


        print("\nStudent Added Successfully!")

        print("Total Marks:", total)
        print("Average Marks:", average)
        print("Percentage:", percentage, "%")


    # ======================================================
    # 2. VIEW STUDENTS
    # ======================================================

    elif choice == "2":

        print("\n===== VIEW STUDENTS =====")


        if len(students) == 0:

            print("No student data available.")


        else:

            for student in students:

                print("\n--------------------------------")
                print("Name:", student["name"])
                print("Roll:", student["roll"])
                print("Semester:", student["semester"])
                print("Department:", student["department"])

                print("\nSubjects & Marks:")


                for subject, marks in student["subjects"].items():

                    print(subject, ":", marks)


                print("Total:", student["total"])
                print("Average:", student["average"])
                print("Percentage:", student["percentage"], "%")

                print("--------------------------------")


    # ======================================================
    # 3. SEARCH STUDENT
    # ======================================================

    elif choice == "3":

        print("\n===== SEARCH STUDENT =====")

        roll = input("Enter Roll Number: ")

        found = False


        for student in students:

            if student["roll"] == roll:

                print("\n===== STUDENT FOUND =====")

                print("Name:", student["name"])
                print("Roll:", student["roll"])
                print("Semester:", student["semester"])
                print("Department:", student["department"])

                print("\nSubjects & Marks:")


                for subject, marks in student["subjects"].items():

                    print(subject, ":", marks)


                print("Total:", student["total"])
                print("Average:", student["average"])
                print("Percentage:", student["percentage"], "%")

                found = True

                break


        if not found:

            print("\nStudent Not Found.")


    # ======================================================
    # 4. MARKS & AVERAGE
    # ======================================================

    elif choice == "4":

        print("\n===== MARKS & AVERAGE =====")

        roll = input("Enter Roll Number: ")

        found = False


        for student in students:

            if student["roll"] == roll:

                print("\n===== MARKS REPORT =====")

                print("Student:", student["name"])
                print("Roll:", student["roll"])


                print("\nSubject Marks:")


                for subject, marks in student["subjects"].items():

                    print(subject, ":", marks)


                print("\nTotal Marks:", student["total"])
                print("Average Marks:", student["average"])
                print("Percentage:", student["percentage"], "%")


                # Get percentage

                percentage = student["percentage"]


                # Grade calculation

                if percentage >= 90:

                    grade = "A+"

                elif percentage >= 80:

                    grade = "A"

                elif percentage >= 70:

                    grade = "B"

                elif percentage >= 60:

                    grade = "C"

                elif percentage >= 40:

                    grade = "D"

                else:

                    grade = "F"


                print("Grade:", grade)


                found = True

                break


        if not found:

            print("\nStudent Not Found.")


    # ======================================================
    # 5. DELETE STUDENT
    # ======================================================

    elif choice == "5":

        print("\n===== DELETE STUDENT =====")

        roll = input("Enter Roll Number: ")

        found = False


        for student in students:

            if student["roll"] == roll:

                students.remove(student)

                print("\nStudent Deleted Successfully!")

                found = True

                break


        if not found:

            print("\nStudent Not Found.")


    # ======================================================
    # 6. EXIT
    # ======================================================

    elif choice == "6":

        print("\n======================================")
        print("Thank You!")
        print("Program Closed.")
        print("======================================")

        break


    # ======================================================
    # INVALID CHOICE
    # ======================================================

    else:

        print("\nInvalid Choice!")
        print("Please enter a number between 1 and 6.")



