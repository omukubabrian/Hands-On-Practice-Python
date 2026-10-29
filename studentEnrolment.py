students_in=[]
student_exited=[]
def enter():
    name=input("Enter student name entering school:").strip().lower()
    if name not in students_in:
        print(f"{name} registered succeessfully")
        students_in.append(name)

    else:
        print("student already logged in")
#enter() 

def exitSchool():
    name=input("Enter student exiting school:").strip().lower()
    if name not in students_in:
        print("Student was never registered in school:")

    else:
        position=students_in.index(name)
        students_in.pop(position)
        student_exited.append(name)
        print(f"{name } exited successfuly")
#exitSchiool()

def display_exited():
    for name in student_exited:
        print(name)
#display_exited()


while True:
    print("="*10,"MENU","*10")
    print("\n 1.Enter school")
    print("\n 2.Exit school")
    print("\n 3.Display exited students")
    print("\n 4.Exit")

    choice=int(input("Choose an option:"))
    if choice==1:
        enter()
    elif choice==2:
        exitSchool()
    elif choice==3:
        display_exited()
    else:
        exit()
        break

