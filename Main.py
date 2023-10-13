def output_file_data(file_name : str) -> None:
    f=open(file_name, "r")

    print("You currently have: " + f.readline().rstrip() + " assessments logged.")
    print("They make up: " + f.readline().rstrip() + "% of your final grade.")
    print("They are as follows:\n")

    total_weight = 0
    grade = 0
    while True:
        line = f.readline().rstrip()
        if line == "":
            break
        results = line.split(',')
        print("Name of Assignment: " + results[2] +
        ". Weight of the final grade: " + results[1] +
        "%. Grade: " + results[0] + "%\n")
        total_weight += int(results[1])
        grade += (int(results[0]) * (int(results[1])/100))

    print("If you were to get 0% on the rest of your assignments, "
          "you would have this as your final grade: " + str(grade) + "%.")
    print("If you were to get 100% on the rest of your assignments, "
          "you would have this as your final grade: " + str(grade + (100- total_weight)) + "%.")

    f.close()


def input_file_data(file_name : str, assignment : list) -> None:
    print("TODO") # TODO


def main():

    print("Welcome to Maksym's Course Manager!")
    course = input("Please enter in your course: ")
    choice = input("To view your course details enter 1. To enter in data, press 2:")

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


main() # Lets run the code
