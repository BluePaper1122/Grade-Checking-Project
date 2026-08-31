# Grade Checking Project

A Python-based grade tracker that calculates weighted course grades and helps students organize assignments across different grading categories.

This is my first programming project and is currently under active development as I learn Python and software development principles.

## Features

- Create courses with custom credit hours
- Create weighted grading categories
- Add assignments and grades to different categories
- Calculate weighted course grades
- Edit existing grades
- Remove assignments
- Validate user input and handle common errors

## Planned Features

- Improved current-grade calculations for courses with ungraded categories
- Target grade calculator ("What grade do I need on my final?")
- GPA and semester grade projections
- Persistent course and grade storage
- Automated testing
- Improved command-line interface
- Graphical or web-based user interface

## How It Works

A course can contain multiple weighted categories, such as:

| Category | Weight |
| --- | ---: |
| Homework | 20% |
| Exams | 50% |
| Final Exam | 30% |

Assignments are added to their respective categories. The program averages the grades within each category and applies the category weight to calculate the overall course grade.

For example:

```text
Homework:
Assignment 1 — 95%
Assignment 2 — 90%

Exams:
Exam 1 — 88%
Exam 2 — 94%
```

The program uses these scores and their corresponding category weights to calculate the student's weighted grade.

## Getting Started

### Requirements

- Python 3

### Installation

Clone the repository:

```bash
git clone https://github.com/BluePaper1122/Grade-Checking-Project.git
```

Navigate into the project directory:

```bash
cd Grade-Checking-Project
```

Run the program:

```bash
python Grade-Checker.py
```

## Project Structure

```text
Grade-Checking-Project/
├── Grade-Checker.py
├── README.md
└── .gitignore
```

As the project grows, the program will be separated into multiple modules for course management, grade calculations, data storage, and testing.

## What I'm Learning

This project is being developed as a way to practice and apply concepts including:

- Object-oriented programming
- Python classes and methods
- Lists and dictionaries
- Type hints
- Input validation
- Exception handling
- Weighted-average calculations
- Debugging and edge-case handling
- Git and version control

## Roadmap

### v0.x — Core Grade Tracker
- [x] Course objects
- [x] Assignment storage
- [x] Weighted categories
- [x] Grade calculation
- [x] Grade editing
- [x] Grade removal
- [ ] Refactor course and category data models
- [ ] Improve validation
- [ ] Handle ungraded categories correctly

### v1.0 — Complete CLI Application
- [ ] Target-grade calculator
- [ ] GPA calculator
- [ ] Save and load course data
- [ ] Unit tests
- [ ] Improved command-line interface
- [ ] Complete documentation

### Future
- [ ] Database integration
- [ ] Grade visualization
- [ ] Web interface
- [ ] Semester GPA projections
- [ ] Grade scenario simulation

## Status

**In active development.**

The current version focuses on implementing and refining the core grade-calculation logic. Additional features and architectural improvements are planned as development continues.
