students=[]
def log_in():
    name=input("Enter student name to enroll:")

    if not name:
        print("name cannot be empty")
    elif name in students:
        print("Student already enrolled")
    else:
        students.append(name)
        print("Student logged in succesfuly")

log_in()



def log_out():
    name=input("Enter student to log_out")

    if not name:
        print("name cannot be empty")
    elif name not in students:
        print("student was never logged in:")
    else:
        students.remove(name)
        print("Student logged out successfully")
log_out()