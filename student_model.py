class University:
    def __init__(self, name, location):
        self.name = name
        self.location = location
    
    def get_details(self):
        return {
            "name": self.name,
            "location": self.location
        }
        
class Department:
    def __init__(self, name, course):
        self.name = name
        self.course = course
    
    def get_details(self):
        return {
            "name": self.name,
            "course": self.course.get_details()
        }
    
class Course:
    def __init__(self, name, level):
        self.name = name
        self.level = level
    
    def get_details(self):
        return {
            "name": self.name,
            "level": self.level
        }
    
class Unit:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    
    def get_details(self):
        return {
            "name": self.name,
            "code": self.code
        }
    
class Semester:
    def __init__(self, name):
        self.name = name
        self.units = []
    
    def add_unit(self, unit):
        self.units.append(unit)
    
    def get_units(self):
        return [unit.get_details() for unit in self.units]
    
    def get_details(self):
        return {
            "name": self.name
        }

class Student():
    def __init__(self, name, reg_no, course):
        self.name = name
        self.reg_no = reg_no
        self.course = course
        self.semester = None
    
    def student_grades(self) -> str:
        results =[]
        
        for unit in self.semester.get_units():
            score = int(input(f"Score for {unit['name']}: "))
            
            if score >= 70:
                grade = "A, Pass"
            elif score >= 60:
                grade = "B, Pass"
            elif score >= 50:
                grade = "C, Pass"
            elif score >= 40:
                grade = "D, Pass"
            else:
                grade = "F, Fail"
        
            results.append(f"{unit['name']}: {score} - {grade}")
        
        return "\n".join(results)
    
    def get_details(self):
        return {
            "Name": self.name,
            "Registration Number": self.reg_no,
            "Course": self.course.get_details()
        }

def main():
    course = Course(name="Computer Science", level="Undergraduate")

    department = Department(name="Computing", course=course)

    university = University(name="Tech University", location="Nairobi")

    unit1 = Unit(name="Data Structures", code="CS201")
    unit2 = Unit(name="Algorithms", code="CS202")
    unit3 = Unit(name="Computer Networks", code="CS203")
    unit4 = Unit(name="Database Systems", code="CS204")

    semester_3_2 = Semester(name="3.2")
    
    semester_3_2.add_unit(unit1)
    semester_3_2.add_unit(unit2)
    semester_3_2.add_unit(unit3)
    semester_3_2.add_unit(unit4)

    student = Student(name="Rop K.", reg_no="CS2025/1234", course=course)
    student.semester = semester_3_2
 
    print(university.get_details())
    print()
    
    print("Student Info:")
    for key, value in student.get_details().items():
        print(f"{key}: {value}")
    print()
    
    print("\nGrading:")
    print(student.student_grades())

if __name__ == "__main__":
    main()
