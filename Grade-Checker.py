"""
reminder*
git add Grade-Checker.py
git commit -m "changes"
git push
"""
from math import isfinite, isclose
import matplotlib as plt
import numpy as np
import scipy as stats

class Course:
    def __init__(self, name: str, credit_hours: int | float) -> None:
        # check for errors in input
        if not(name):
            raise ValueError("The class must have a name! (enter your university class code)")
        elif not(isinstance(name, str)):
            raise TypeError("The class must be a string! (enter your university class code)")
        if not(isinstance(credit_hours, (int, float))):
            raise ValueError(f"The credit hours must be an integer or float! Enter the credit hours for {name} in the object.")
        elif not isfinite(credit_hours) or credit_hours < 0:
            raise ValueError(f"The credit hours must be a finite, nonnegative value! Enter the credit hours for {name} in the object.")

        # initialize values for given inputs
        self.name = name
        self.credit_hours = credit_hours
        self.grades = []
        self.categories = []

    def __str__(self) -> str:
        def check_error_calculate_grade(calculate_grade):
            try:
                return calculate_grade()
            except ValueError:
                return "N/A"
        def check_error_grade_converter(grade_converter):
            try:
                return grade_converter()
            except ValueError:
                return "N/A"

        # format for checking their grades and classes
        return f"\n************************************************\nClass Name: {self.name} ({self.credit_hours} credits)\nCurrent Grade: {check_error_calculate_grade(self.calculate_grade)}\nLetter Grade: {check_error_grade_converter(self.grade_converter)}\n"

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

    def calculate_percentage(self) -> float:
        # checks that there are grades within the system.
        try:
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

            if not isclose(sum(weight for category in self.categories for weight in category.values()), 1.0):
                raise ValueError("Category weights must add up to 1.0 (100%).")
            return total_grade
        except ValueError as e:
            raise ValueError(f"Grade Entry Error: {e}")

            

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

    def calculate_grade(self) -> str:
        percentage = self.calculate_percentage()
        return f"The course grade based on current assignments in the course {self.name} is: {percentage:.2f}%"

    def grade_converter(self) -> str:
        percentage = self.calculate_percentage()
        for minimum, letter in (
            (93, "A"), (90, "A-"), (87, "B+"), (83, "B"),
            (80, "B-"), (77, "C+"), (73, "C"), (70, "C-"),
            (67, "D+"), (63, "D"), (60, "D-"),
        ):
            if percentage >= minimum:
                return letter
        return "F"

    def get_grade_point(self) -> float:
        return GPACalculator.GRADE_POINTS[self.grade_converter()]

class GPACalculator:
    # Adjust this mapping if your university uses a different GPA scale.
    GRADE_POINTS = {
        "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7,
        "C+": 2.3, "C": 2.0, "C-": 1.7, "D+": 1.3, "D": 1.0,
        "D-": 0.7, "F": 0.0,
    }

    def __init__(self, courses=None) -> None:
        self.courses: list[Course] = []
        if courses is not None:
            self.transfer_courses(*courses)

    def transfer_courses(self, *courses: Course) -> str:
        if any(not isinstance(course, Course) for course in courses):
            raise TypeError("Pass Course objects, not course names.")
        for course in courses:
            if course in self.courses:
                raise ValueError(f"{course.name} has already been added.")
        if len({id(course) for course in courses}) != len(courses):
            raise ValueError("The same Course object cannot be added twice.")
        self.courses.extend(courses)
        names = ", ".join(course.name for course in self.courses)
        return f"Courses successfully initialized! Your courses to calculate GPA are: {names}"

    def calculate_gpa(self) -> float:
        total_points = 0.0
        total_credits = 0.0
        for course in self.courses:
            # Zero-credit courses do not affect GPA or need recorded grades.
            if course.credit_hours == 0:
                continue
            total_points += course.get_grade_point() * course.credit_hours
            total_credits += course.credit_hours
        if total_credits == 0:
            return 0.0
        return round(total_points / total_credits, 2)

if __name__ == '__main__':
    # User uses this section to define grades and assignments
    comp140 = Course("COMP140", 4)
    psyc203 = Course("PSYC203", 3)
    bios310 = Course("BIOS310", 3)
    math212 = Course("MATH212", 3)
    stat310 = Course("STAT310", 3)
    stat314 = Course("STAT314", 1)
    univ194 = Course("UNIV194", 0)
    comp140.add_category("homework", 0.10)
    comp140.add_category("exams", 0.50)
    comp140.add_category("written", 0.40)
    comp140.add_category("random", 0.01)

    comp140.remove_category("random")

    comp140.add_grade("exam1", 98, "exams")
    comp140.add_grade("exam2", 95, "exams")
    comp140.add_grade("homework1", 92, "homework") # raises ValueError if removed
    comp140.add_grade("written_recipe_1", 88, "written")

    psyc203.add_category("homework", 0.10)
    psyc203.add_category("exams", 0.50)
    psyc203.add_category("written", 0.40)
    psyc203.add_category("random", 0.01)
    
    psyc203.remove_category("random")
    
    psyc203.add_grade("exam1", 97, "exams")
    psyc203.add_grade("exam2", 92, "exams")
    psyc203.add_grade("homework1", 100, "homework") # raises ValueError if removed
    psyc203.add_grade("essay1", 95, "written")

    calculator = GPACalculator()
    print(calculator.transfer_courses(comp140, psyc203))
    print(f"GPA: {calculator.calculate_gpa():.2f}")


    #all_courses = [comp140, psyc203, bios310, math212, stat310, stat314, univ194]
    #for course in all_courses:
    #    print(course)