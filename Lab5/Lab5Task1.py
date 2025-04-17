rollno = int(input("Enter roll number:"))
present_students = {1,2,3,4,5}
def checkAttendance(rollno):
    if rollno in present_students:
        print("Present")
    else:
        print("Absent")
checkAttendance(rollno)


