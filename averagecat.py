def average():
    marks=[]
    try:
        number=int(input("How many marks do you want to enter?"))
        if number <=0 :
            raise ValueError("Number cannot be negative")

        for count in range(number):
            while True:
                try:
                    mark=int(input(f"Enter cat {count +1} marks:"))
                    if mark < 0 or mark > 100:
                        print("Marks must be between 0 and 100")
                        continue
                    marks.append(mark)
                    break

                except ValueError:
                    print("Please Enter a whole number.")
        return sum(marks)/len(marks)

    except ValueError as error:
        print(f"Invalid number input {error}")
        return None

result=average()
if result is not None:
    print(f"Average for cats: {result:.2f}")