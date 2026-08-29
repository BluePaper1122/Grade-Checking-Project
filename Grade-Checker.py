"""
reminder*
git add Grade-Checker.py
git commit -m "changes"
git push
"""
class Class:
    def __init__(self, name, credit_hours):
        # check for errors in input
        if not(name):
            raise ValueError("The class must have a name! (enter your university class code)")
        elif not(isinstance(name, str)):
            raise TypeError("The class must be a string! (enter your university class code)")
        if not(isinstance(credit_hours, (int, float))):
            raise ValueError(f"The credit hours must be an integer or float! Enter the credit hours for {name} in the object.")
        elif credit_hours < 0:
            raise ValueError(f"The credit hours must not be a negative value! Enter the credit hours for {name} in the object.")

        # initialize values for given inputs
        self.name = name
        self.credit_hours = credit_hours
        self.grades = []

    def __str__(self):
        # format for checking their grades and classes
        return f"\n************************************************\nClass Name: {self.name} ({self.credit_hours} credits)\nCurrent Grade: grade input here\nLetter Grade: placeholder A\n"

    def add_grade(self, assignment_name, points, category, category_weight):
        # check for errors in input
        if not assignment_name:
            raise ValueError("The added grade entry must have a name!")
        elif not isinstance(assignment_name, str):
            raise TypeError("The assignment grade entry must be a string!")
        if not isinstance(points, (int, float)):
            raise TypeError("points must be a number!")
        if not category:
            raise ValueError("There must be a category for the entry!")
        elif not isinstance(category, str):
            raise TypeError("The category entry must be a string!")
        if not category_weight:
            raise ValueError("The category must have a weight!")
        elif not isinstance(category_weight, (int, float)):
            raise TypeError("The weight of the category must be a *number* between 0 and 1! (please input a number)")
        elif not (0 <= category_weight <= 1):
            raise ValueError("The weight of the category must be a number *between 0 and 1*! (please convert the percent weight into a decimal)")

        # add the entry for points, category, and category_weight into a dictionary
        grade_entry = {
            "assignment_name": assignment_name,
            "points": points,
            "category": category,
            "category_weight": category_weight
        }

        # append temp dictionary into the grade_entry list
        self.grades.append(grade_entry)

    def check_added_grades(self):
        # allows the user to check the grades they added in a dictionary in list format
        return self.grades

    def change_grade(self, assignment_name, new_points, new_category, new_category_weight):
        if not self.grades:
            raise ValueError("You must have a grade inputted before you can change your entries!")
        
        if grades(assignment_name)


    



# User uses this section to define grades and assignments
comp140 = Class("COMP140", 4)
psyc203 = Class("PSYC203", 3)
bios310 = Class("BIOS310", 3)
math212 = Class("MATH212", 3)
stat310 = Class("STAT310", 3)
stat314 = Class("STAT314", 1)
univ194 = Class("UNIV194", 0)
comp140.add_grade("homework1", 95, "homework", 0.05)

print(comp140.check_added_grades())