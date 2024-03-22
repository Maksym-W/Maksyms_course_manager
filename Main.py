from os import path
from decimal import Decimal

"""
The way the files are organized are as follows.

How many assignments are therefore
How much of your final grade is determined already
The rest of the lines are grade, weight, name of assignment
"""


def output_file_data(file_name: str) -> None:
    f = open(file_name, "r")
    grade = 0
    num_of_assignments = f.readline().rstrip()
    total_weight = f.readline().rstrip()

    print("You currently have: " + num_of_assignments + " assessments logged.")
    print("They make up: " + total_weight + "% of your final grade.")
    print("They are as follows:\n")

    while True:
        line = f.readline().rstrip()
        if line == "":
            break
        results = line.split(',')
        print("Name of Assignment: " + results[2] +
              ". Weight of the final grade: " + results[1] +
              "%. Grade: " + results[0] + "%")
        grade += (float(results[0]) * (float(results[1]) / 100))

    print("\n")
    print("Your current average is: " + str((grade/float(total_weight))*100) + "%")
    print("If you were to get 0% on the rest of your assignments, "
          "you would have this as your final grade: " + str(grade) + "%.")
    print("If you were to get 100% on the rest of your assignments, "
          "you would have this as your final grade: " + str(grade + (100 - float(total_weight))) + "%.")

    f.close()


def input_file_data(file_name: str, assignment: list) -> None:
    # Open the file in read mode
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Modify the lines as needed
    lines[0] = str(int(lines[0]) + 1) + "\n"
    lines[1] = str(float(lines[1]) + float(assignment[1])) + "\n"
    lines.append(assignment[0] + ", " + assignment[1] + ", " + assignment[2] + "\n")

    # Open the file in write mode to overwrite its contents
    with open(file_name, 'w') as file:
        file.writelines(lines)


def main() -> None:
    print("Welcome to Maksym's Course Manager!")
    course = input("Please enter in your course: ")
    choice = input("To view your course details enter 1. To enter in data, press 2:")

    if not (path.exists("Courses/" + course + ".txt")):
        with open("Courses/" + course + ".txt", 'w') as file:
            file.writelines(["0\n", "0\n"])  # Use writelines to write multiple lines
        print("Course did not exist previously, thus created a new file for it.\n")

    if choice == "1":
        output_file_data("Courses/" + course + ".txt")
    elif choice == "2":
        assignment = [None, None, None]
        assignment[2] = input("Enter the name of the assignment: ")
        assignment[0] = input("Enter your grade: ")
        assignment[1] = input("Enter the weight of assignment: ")
        input_file_data("Courses/" + course + ".txt", assignment)
    else:
        print("Please enter in 1 or 2 next time")


main()  # Lets run the code
