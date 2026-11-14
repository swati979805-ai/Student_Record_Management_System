# Student Record Management System

## Project Information

-   **Project Number:** PS No. 17
-   **Project Title:** Student Record Management System
-   **Programming Language:** Python 3
-   **GUI Framework:** Tkinter
-   **Concepts Used:** Lists, Tuples, Dictionaries, Functions, CRUD
    Operations, and Input Validation

## 1. Project Description

The **Student Record Management System** is a Python-based desktop
application designed to store and manage student records in an organized
way. The application provides a graphical user interface (GUI) through
which users can add, view, search, update, and delete student
information.

Each student record contains four details:

-   Roll Number
-   Student Name
-   Course
-   Marks

The system checks that each roll number is unique and that marks are
numeric values between 0 and 100. It also displays student records in a
table so that information can be viewed clearly.

## 2. Objectives

The main objectives of this project are to:

1.  Create a simple application for managing student records.
2.  Add new student information.
3.  Display all stored student records in a table.
4.  Search for a student using their roll number.
5.  Update a student's marks.
6.  Delete a student record.
7.  Validate user input and prevent duplicate roll numbers.
8.  Apply Python data structures and programming concepts in a practical
    project.

## 3. Features

-   **Add Student:** Adds a new student after validating the entered
    details.
-   **View Students:** Displays all student records in a table.
-   **Search Student:** Finds a student using their roll number.
-   **Update Marks:** Updates the marks of an existing student.
-   **Delete Student:** Removes a student record using the roll number.
-   **Input Validation:** Prevents empty fields, duplicate roll numbers,
    non-numeric marks, and marks outside the 0--100 range.
-   **GUI:** Provides input fields, buttons, messages, and a
    student-record table.

## 4. Technologies and Concepts Used

  Technology / Concept   Purpose
  ---------------------- --------------------------------------------------------
  Python 3               Main programming language
  Tkinter                Creates the graphical user interface
  Lists                  Stores multiple student records
  Dictionaries           Stores each student's details as key-value pairs
  Tuples                 Defines the table column names
  Functions              Organizes the program into reusable operations
  CRUD                   Implements Create, Read, Update, and Delete operations
  Input validation       Checks user input before changing records
  ttk.Treeview           Displays student records in a table

## 5. Project Structure

``` text
Student_Record_Management_System/
└── student_management.py
```

The main Python file contains the data storage, CRUD functions, input
validation, GUI design, and application event loop.

## 6. Requirements

-   Python 3.x
-   Tkinter (usually included with the standard Python installation)

On some Linux systems, Tkinter may need to be installed separately
through the operating system's package manager.

## 7. How to Run the Project

1.  Install Python 3 if it is not already installed.
2.  Open the project folder in a terminal or command prompt.
3.  Run the following command:

``` bash
python student_management.py
```

4.  The Student Record Management System window will open.
5.  Enter student details and use the buttons to manage records.

On some systems, the command may be:

``` bash
python3 student_management.py
```

## 8. Input Validation

The application applies the following validation rules:

-   All four fields must be filled before adding a student.
-   Roll numbers must be unique.
-   Marks must be entered as a whole number.
-   Marks must be between 0 and 100, inclusive.
-   A search, update, or delete operation must use an existing roll
    number.

## 9. Test Cases

The project can be tested using the cases provided in the project
specification.

  -------------------------------------------------------------------------
  Test Case               Input / Action            Expected Result
  ----------------------- ------------------------- -----------------------
  Normal Input            Add                       Record is added
                          `101, Aman, BTech, 78`    successfully

  Boundary Input          Add                       Record is added
                          `102, Riya, BTech, 100`   successfully

  Invalid Input 1         Add roll number `101`     Duplicate roll number
                          again                     error

  Invalid Input 2         Add                       Marks validation error
                          `103, Ravi, BTech, 150`   

  Search                  Search for roll number    Aman's record is
                          `101`                     displayed

  Update                  Change marks of roll      Marks are updated to 85
                          number `101` to `85`      

  Delete                  Delete roll number `999`  Record-not-found
                                                    message
  -------------------------------------------------------------------------

The test cases should be run in order using the same running application
because the current version stores records in memory.

## 10. Data Storage

In this version, student records are stored in a Python list while the
application is running. Each student's information is represented by a
dictionary.

**Note:** Records are temporary and are cleared when the application is
closed. File-based or database storage can be added as a future
improvement.

## 11. Future Enhancements

Possible improvements include:

-   Save records permanently using a file or database.
-   Add student details such as email address and phone number.
-   Add sorting and filtering options.
-   Improve the GUI with additional styling and dashboard summaries.
-   Add login and access-control features.

## 12. Conclusion

The Student Record Management System demonstrates how Python can be used
to develop a simple desktop application for managing student
information. It combines lists, dictionaries, tuples, functions, input
validation, and CRUD operations with a Tkinter graphical interface. The
project provides practical experience in Python programming and basic
GUI development.
