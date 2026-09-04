"""
reminder*
git add Grade-Checker.py
git commit -m "changes"
git push
"""
import numpy as np
import matplotlib as plt

class Class:
    def __init__(self, name: str, credit_hours: int | float) -> None:
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
        self.categories = []

    def __str__(self) -> str:
        # format for checking their grades and classes
        return f"\n************************************************\nClass Name: {self.name} ({self.credit_hours} credits)\nCurrent Grade: {self.calculate_grade()}\nLetter Grade: {self.grade_converter}\n"

    def add_grade(self, assignment_name: str, points: int | float, category: str) -> None:
        # check for errors in input
        if not(self.categories) or not(any(category in cat for cat in self.categories)):
            raise ValueError("The category has not been defined yet! Use the add_category method to add a category!")
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

        # add the entry for points, category into a dictionary
        grade_entry = {
            "assignment_name": assignment_name,
            "points": points,
            "category": category
        }

        # append temp dictionary into the grade_entry list
        self.grades.append(grade_entry)

    def check_added_grades(self) -> str:
        # allows the user to check the grades they added in a dictionary in list format
        print("\n")
        for index, entry in enumerate(self.grades):
            print(f"Inputted grade {index + 1} has the name '{entry['assignment_name']}' belonging to the '{entry['category']}' category. The assignment received a score of {entry['points']}%.")
        return f"\n************************************************\nThe grades are within this chart below: {self.grades}\n"

    def calculate_grade(self) -> str:
        # checks that there are grades within the system.
        if not self.grades:
            raise ValueError(f"No grades recorded for {self.name} yet. Enter a grade in order to check your current standing!")
        total_grade = 0.00        # Temporary placeholder variable to prevent NameError crash | now functions as an initializatin for grades
        categories = [list(cat.keys())[0] for cat in self.categories] # lists the category types in a list categories

        for cat in categories:
            # Checks if there is >=1 grade matching the category name.
            has_grades = any(grade['category'] == cat for grade in self.grades)
            
            if not has_grades:
                raise ValueError(
                    f"Cannot calculate grades with empty grade categories! "
                    f"The category '{cat}' has no grades. Remove categories that do not have "
                    f"any grades using the 'remove_category' method!")

        for index in range(len(categories)):
            grade_holder = 0.00
            grades_in_category = 0
            for grade in self.grades:
                if grade['category'] == categories[index]:
                    grade_holder += grade['points']
                    grades_in_category += 1
            if grades_in_category > 0:
                total_grade = (total_grade) + ((grade_holder / grades_in_category) * self.categories[index][categories[index]])
            else:
                total_grade += 0

        return f"The course grade based on current assignments in the course {self.name} is: {total_grade:.2f}%"


    def change_grade(self, assignment_name: str, new_points: int | float, new_category: str) -> None:
        if not self.grades:
            raise ValueError("You must have a grade inputted before you can change your entries!")

        # updates the points, category, and category weight from the previous grade_entry if desired by user
        for entry in self.grades:
            if entry["assignment_name"] == assignment_name:
                entry["points"] = new_points
                entry["category"] = new_category

    def remove_grade(self, assignment_name: str) -> None:
        # removes entry associated with the desired assignment.
        remove_count = 0
        for index, entry in enumerate(self.grades):
            if entry["assignment_name"] == assignment_name:
                item = self.grades[index]
                self.grades.remove(item)
                remove_count += 1

        if remove_count == 0:
            raise ValueError("The grade you tried to remove is not a pre-existing defined grade! Nothing has been removed.")


    def add_category(self, category: str, category_weight: int | float) -> None:
        # error handling
        if not category_weight:
            raise ValueError("The category must have a weight!")
        elif not isinstance(category_weight, (int, float)):
            raise TypeError("The weight of the category must be a *number* between 0 and 1! (please input a number)")
        elif not (0 <= category_weight <= 1):
            raise ValueError("The weight of the category must be a number *between 0 and 1*! (please convert the percent weight into a decimal)")
        elif any(category in cat for cat in self.categories):
            raise ValueError("This category already exists!")

        category_entry = {
            f"{category}": category_weight
        }
        self.categories.append(category_entry)

    def check_categories(self) -> list:
        return self.categories

    def remove_category(self, category: str) -> None:
        remove_count = 0
        for index, cat in enumerate(self.categories):
            if category in cat:
                item = self.categories[index]
                self.categories.remove(item)
                remove_count += 1

        if remove_count == 0:
            raise ValueError("The category you tried to remove is not a pre-existing defined category! Nothing has been removed.")

    def grade_converter(self):
        # directly from previous calculate_grade method
        if not self.grades:
            raise ValueError(f"No grades recorded for {self.name} yet. Enter a grade in order to check your current standing!")
        total_grade = 0.00        # Temporary placeholder variable to prevent NameError crash | now functions as an initializatin for grades
        categories = [list(cat.keys())[0] for cat in self.categories] # lists the category types in a list categories

        for cat in categories:
            # Checks if there is >=1 grade matching the category name.
            has_grades = any(grade['category'] == cat for grade in self.grades)
            
            if not has_grades:
                raise ValueError(
                    f"Cannot calculate grades with empty grade categories! "
                    f"The category '{cat}' has no grades. Remove categories that do not have "
                    f"any grades using the 'remove_category' method!")

        for index in range(len(categories)):
            grade_holder = 0.00
            grades_in_category = 0
            for grade in self.grades:
                if grade['category'] == categories[index]:
                    grade_holder += grade['points']
                    grades_in_category += 1
            if grades_in_category > 0:
                total_grade = (total_grade) + ((grade_holder / grades_in_category) * self.categories[index][categories[index]])
            else:
                total_grade += 0

        if total_grade >= 93:
            return "A"
        elif total_grade >= 90:
            return "A-"
        elif total_grade >= 87:
            return "B+"
        elif total_grade >= 83:
            return "B"
        elif total_grade >= 80:
            return "B-"
        elif total_grade >= 77:
            return "C+"
        elif total_grade >= 73:
            return "C"
        elif total_grade >= 70:
            return "C-"
        elif total_grade >= 67:
            return "D+"
        elif total_grade >= 63:
            return "D"
        elif total_grade >= 60:
            return "D-"
        elif total_grade < 60:
            return "F"


if __name__ == '__main__':
    # User uses this section to define grades and assignments
    comp140 = Class("COMP140", 4)
    psyc203 = Class("PSYC203", 3)
    bios310 = Class("BIOS310", 3)
    math212 = Class("MATH212", 3)
    stat310 = Class("STAT310", 3)
    stat314 = Class("STAT314", 1)
    univ194 = Class("UNIV194", 0)
    comp140.add_category("homework", 0.10)
    comp140.add_category("exams", 0.50)
    comp140.add_category("written", 0.40)
    comp140.add_category("random", 0.01)

    comp140.remove_category("random")

    comp140.add_grade("exam1", 98, "exams")
    comp140.add_grade("exam2", 95, "exams")
    comp140.add_grade("homework1", 92, "homework") # raises ValueError
    comp140.add_grade("written_recipe_1", 88, "written")

    print(comp140.check_categories())
    print(comp140.check_added_grades())
    print(comp140.calculate_grade())
    print(comp140)

    # test push for clone 2
    # this is a test commit to ensure that the python file is still referenced by github