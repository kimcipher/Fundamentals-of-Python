# This is a code to add, replace, retrieve and update students in an exam
# Create a list of 5 students.
# a. add 2 new students
# b. show the 4th to the 7th student in the list
# c. replace the third student
# d. check if a student is not existing, add the student


print("The following students did their KCSE examinations")
students = ["Lisandra", "Makena","Joseph","Anthony","Makau","Spanishia","Gregory","Awiti"]
print(students)
print("Moses and Patrick were added to the list")
students.append("Moses")
students.append("Patrick")
print(students)
print("The following  students passed with flying colors")
print(students[3:7])
print("Joseph was then replaced by Mark in the list")
students[2] = "Mark"
print(students)

if "Patricia" not in students:
    print("Patricia marks were missing")
    print("She was added in the list though")
    students.append("Patricia")
    print(students)
if "Spanishia" in students:
    print("Spanishia scored an A")