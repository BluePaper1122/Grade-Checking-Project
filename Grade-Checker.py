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
        print("\n")
        for index, entry in enumerate(self.grades):
            print(f"Inputted grade {index + 1} has the name '{entry['assignment_name']}' belonging to the '{entry['category']}' category, with a weight of {entry['category_weight'] * 100}% of the grade. The assignment received a score of {entry['points']}%.")
        return f"\n************************************************\nThe grades are within this chart below: {self.grades}\n"

    def calculate_grade(self):
        # calculates the items in the gradebook and sums it up.
        temp_list = []
        for entry in self.grades:
            true_grade = entry["points"] * entry["category_weight"]
            temp_list.append(true_grade)

        # sums it up
        total_grade = 0
        for grade in temp_list:
            total_grade += grade

        return f"The course grade based on current assignments in the course {self.name} is: {total_grade:.2f}%"
        

    def change_grade(self, assignment_name, new_points, new_category, new_category_weight):
        if not self.grades:
            raise ValueError("You must have a grade inputted before you can change your entries!")

        # updates the points, category, and category weight from the previous grade_entry if desired by user
        for entry in self.grades:
            if entry["assignment_name"] == assignment_name:
                entry["points"] = new_points
                entry["category"] = new_category
                entry["category_weight"] = new_category_weight

    def remove_grade(self, assignment_name):
        # removes entry associated with the desired assignment.
        temp_list = self.grades # for storage for error-checking later
        for index, entry in enumerate(self.grades):
            if entry["assignment_name"] == assignment_name:
                item = self.grades[index]
                self.grades.remove(item)


    



# User uses this section to define grades and assignments
comp140 = Class("COMP140", 4)
psyc203 = Class("PSYC203", 3)
bios310 = Class("BIOS310", 3)
math212 = Class("MATH212", 3)
stat310 = Class("STAT310", 3)
stat314 = Class("STAT314", 1)
univ194 = Class("UNIV194", 0)
comp140.add_grade("homework1", 95, "homework", 0.05)
comp140.add_grade("homework2", 99, "homework", 0.05)
comp140.add_grade("exam1", 88, "exam", 0.40)
comp140.add_grade("recipe1", 72, "writing", 0.55)

comp140.remove_grade('homework2')

print(comp140.check_added_grades())
print(comp140.calculate_grade())
