def output_file_data(file_name : str) -> None:
    f=open(file_name, "r")

    print("You currently have: " + f.readline().rstrip() + " assessments logged.")
    print("They make up: " + f.readline().rstrip() + "% of your final grade.")
    print("They are as follows:\n")


    f.close()



def main():

    print("Welcome to Maksym's Course Manager!")
    course = input("Please enter in your course: ")
    choice = input("To view your course details enter 1. To enter in data, press 2:")

    if choice == "1":
        output_file_data("Courses/" + course + ".txt")
    elif choice == "2":
        f=open("Courses/" + course + ".txt", "w")
        f.write("This is a test")
        f.close()
    else:
        print("Please enter in 1 or 2 next time")


main() # Lets run the code

"""
CURRENT TEMPLATE

You currently have: 0 assessments logged
They make up: 0% of your final grade
They are as follows:
\n
ASSIGNMENTS 1
\n
Your current average is: x%
If you were to get 0% on the rest of your assignments, you would have this as your final grade y%
If you were to get 100% on the rest of your assignments, you would have this as your final grade y%
The highest Possible GPA you can get is.
"""
