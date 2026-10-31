class Employee:
    def __init__(self,name,role):
        self.name=name
        self.role=role
    def displayInfo(self):
        print(f"Employee name:{self.name}")
        print(f"Employee's role:{self.role}")

    def reportToWork(self):
        print(f"{self.name} the {self.role} reports to work very early ")
        print(f"{self.name} requires to be appreciated for everyday's efforts.")

Employee1=Employee("Brian","Manager")
Employee2=Employee("Dorcas","Director")

Employee1.displayInfo()
Employee1.reportToWork()
Employee2.displayInfo()
Employee2.reportToWork()