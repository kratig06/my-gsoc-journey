# Create a class called Student
# It should have: name, age, and a list of grades
# Methods:
#   - add_grade(grade) → adds a grade to the list
#   - average() → returns average of all grades
#   - is_passing() → returns True if average >= 40
#   - __str__ → prints something like "Alice | Age: 20 | Avg: 78.5"

# Then create 2 Student objects and test all methods
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []
        
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def average(self):
        if (len(self.grades)==0):
            return 0 
        return sum(self.grades)/ len(self.grades)
    
    def is_passing(self):
        return self.average()>= 40
    
    def __str__ (self):
        return f"{self.name} | Age: {self.age} | Avg: {self.average():.2f}"

    def top_grade(self):
        if len(self.grades) == 0:
            return "No grades yet"
        
        top = self.grades[0]
        for grade in self.grades:
            if grade > top:
                top = grade
        return top

s1 = Student("Kratika", 20)
s2 = Student("Karan", 20) 

s1.add_grade(80)
s1.add_grade(75)
s1.add_grade(79)

print(s1.average())
print(s1.is_passing())
print(s1)      
print(s1.top_grade())