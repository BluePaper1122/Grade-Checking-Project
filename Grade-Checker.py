class Class:
    def __init__(self, name, credit_hours):
        # check for errors in input
        if not(name):
            raise ValueError("The class must have a name! (enter your university class code)")
        elif not(isinstance(name, str)):
            raise ValueError("The class must be a string! (enter your university class code)")
        if not(isinstance(credit_hours, (int, float))):
            raise ValueError(f"The credit hours must be an integer or float! Enter the credit hours for {name} in the object.")
        elif credit_hours < 0:
            raise ValueError(f"The credit hours must not be a negative value! Enter the credit hours for {name} in the object.")

        # initialize values for given inputs
        self.name = name
        self.credit_hours = credit_hours
        self.grades = []

    def __str__(self):
        return f"\n************************************************\nClass Name: {self.name} ({self.credit_hours} credits)\nCurrent Grade: grade input here\nLetter Grade: placeholder A\n************************************************"

    def add_grade(self, points, category, category_weight):
        grade_entry = {
            "points": points,
            "category": category,
            "category_weight": category_weight
        }
        self.grades.append(grade_entry)
    



# User uses this section to define grades and assignments
comp140 = Class("COMP140", 4)
psyc203 = Class("PSYC203", 3)
bios310 = Class("BIOS310", 3)
math212 = Class("MATH212", 3)
stat310 = Class("STAT310", 3)
stat314 = Class("STAT314", 1)
univ194 = Class("UNIV194", 0)

print(comp140)
print(psyc203)