# basic for loop
students = ['Laura', 'Georgie', 'Kasia']

uppercase_students = []

for student in students:
    uppercase_students.append(student.upper())

print(uppercase_students)


# list comp version

students = ['Laura', 'Georgie', 'Kasia']

uppercase_students = [student.upper() for student in students]

print("list comp version:", uppercase_students)


# map version

students = ['Laura', 'Georgie', 'Kasia']

uppercase_students = list(map(lambda student: student.upper(), students))

print("lambda version:", uppercase_students)


# use map to find student name length

students = ['Laura', 'Georgie', 'Kasia']

# applies the len function to every item in a list
student_name_lengths = list(map(lambda student: len(student), students))

print("Student name lengths: ",student_name_lengths)

# practice

students = ['Laura', 'Georgie', 'Kasia']

student_name_sorted = list(map(lambda student: student.replace('a', 'isha'), students))

print(student_name_sorted)

students = [
    {'name': 'Laura', 'python_mark': 100, 'sql_mark': 150},
    {'name': 'Georgie', 'python_mark': 101, 'sql_mark': 120},
    {'name': 'Kasia', 'python_mark': 99, 'sql_mark': 200},
]

# key can determine what sorting by, alphabetically order is the default
# here we are sorting by their total mark (python + sql)
# don't understand where the looping is occuring (sorted, goes through each item and orders)
print(sorted(students, key=lambda student: student['python_mark'] + student['sql_mark']))