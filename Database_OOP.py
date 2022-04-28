import csv

class Student:
    def __init__(self, id, fName, lName, email, app_on_file):
        """creates students based on fields exported from a database"""
        self.id = id
        self.fName = fName
        self.lName = lName
        self.email = email
        self.app_on_file = app_on_file

    def checkApp(self):
        """used to check to see if app is on file"""
        if self.app_on_file == "False":
            print(f"{student.fName} {student.lName} needs to fill out an application.")
            return False

#location of the database
data = './myFile0.csv'


#store all students created somewhere
student_bucket = []

#count of total students
count_of_students = 0

#count of how many missing apps
count_of_apps = 0

with open(data,newline='' ) as db:
    reader = csv.reader(db, delimiter = ",")
    #iterate through all of the fields in the csv file
    for id, first, last, email, app in reader:
        id = id
        fName = first
        lName = last
        email = email
        app = app

        student_bucket.append(Student(id, fName, lName, email, app))
        count_of_students += 1

    for student in student_bucket:
        if student.checkApp() == False:
            count_of_apps += 1


print()
print()
print(f"Out of a total of {count_of_students} students, {count_of_apps} students are missing applications.")