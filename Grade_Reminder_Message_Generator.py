"""
Takes user input to craft messages for students with missing assignments.
"""

names = (input("Enter student names, separated by a comma followed by a space: ")).title().split(", ")
assignments = (input("Enter student's count of missing assignments, separated by a comma followed by a space:"
                     " ")).split(", ")
grades = (input("Enter student grades, separated by a comma followed by a space: ")).split(", ")

# message string to be used for each student
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. Your current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for name, assignment, grade in zip(names, assignments, grades):
    possible_increased_grade = (int(assignment)*2)+int(grade)
    print(message.format(name, assignment, grade, possible_increased_grade))
