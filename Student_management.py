
import tkinter as tk
from tkinter import ttk, messagebox


# BLOCK 1: DATA STORAGE


students = []

# Tuple containing table column names
columns = ("Roll No", "Name", "Course", "Marks")



# BLOCK 2: ADD STUDENT (CREATE)


def add_student():

    roll = roll_entry.get().strip()
    name = name_entry.get().strip()
    course = course_entry.get().strip()
    marks = marks_entry.get().strip()

    if not roll or not name or not course or not marks:
        messagebox.showerror("Error", "Please fill all fields.")
        return

    # Check whether roll number already exists
    for student in students:
        if student["roll"] == roll:
            messagebox.showerror(
                "Error", f"Roll number {roll} already exists."
            )
            return

    # Validate marks
    try:
        marks = int(marks)
    except ValueError:
        messagebox.showerror("Error", "Marks must be a number.")
        return

    if marks < 0 or marks > 100:
        messagebox.showerror(
            "Error", "Marks must be between 0 and 100."
        )
        return

    # Store student details in dictionary
    student = {
        "roll": roll,
        "name": name,
        "course": course,
        "marks": marks
    }

    students.append(student)

    messagebox.showinfo(
        "Success",
        f"Record added: {roll} | {name} | {course} | {marks}"
    )

    clear_fields()
    view_students()



# BLOCK 3: VIEW STUDENTS (READ)


def view_students():

    # Remove previous table records
    for item in student_table.get_children():
        student_table.delete(item)

    # Insert updated records
    for student in students:
        student_table.insert(
            "",
            tk.END,
            values=(
                student["roll"],
                student["name"],
                student["course"],
                student["marks"]
            )
        )



# BLOCK 4: SEARCH STUDENT 

def search_student():

    roll = roll_entry.get().strip()

    if not roll:
        messagebox.showerror("Error", "Enter roll number.")
        return

    for student in students:

        if student["roll"] == roll:

            name_entry.delete(0, tk.END)
            name_entry.insert(0, student["name"])

            course_entry.delete(0, tk.END)
            course_entry.insert(0, student["course"])

            marks_entry.delete(0, tk.END)
            marks_entry.insert(0, str(student["marks"]))

            messagebox.showinfo(
                "Found",
                f'{student["roll"]} | {student["name"]} | '
                f'{student["course"]} | {student["marks"]}'
            )
            return

    messagebox.showerror(
        "Not Found", f"Roll number {roll} not found."
    )



# BLOCK 5: UPDATE STUDENT (UPDATE)


def update_student():

    roll = roll_entry.get().strip()
    new_marks = marks_entry.get().strip()

    if not roll or not new_marks:
        messagebox.showerror(
            "Error", "Enter roll number and new marks."
        )
        return

    try:
        new_marks = int(new_marks)
    except ValueError:
        messagebox.showerror(
            "Error", "Marks must be a number."
        )
        return

    if new_marks < 0 or new_marks > 100:
        messagebox.showerror(
            "Error", "Marks must be between 0 and 100."
        )
        return

    for student in students:

        if student["roll"] == roll:

            student["marks"] = new_marks

            messagebox.showinfo(
                "Success", f"Marks updated: {new_marks}"
            )

            clear_fields()
            view_students()
            return

    messagebox.showerror(
        "Not Found", f"Roll number {roll} not found."
    )



# BLOCK 6: DELETE STUDENT (DELETE)


def delete_student():

    roll = roll_entry.get().strip()

    if not roll:
        messagebox.showerror(
            "Error", "Enter roll number to delete."
        )
        return

    for student in students:

        if student["roll"] == roll:

            students.remove(student)

            messagebox.showinfo(
                "Success", f"Student {roll} deleted."
            )

            clear_fields()
            view_students()
            return

    messagebox.showerror(
        "Not Found", f"Roll number {roll} not found."
    )



# BLOCK 7: CLEAR INPUT FIELDS


def clear_fields():

    roll_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)



# BLOCK 8: CREATE MAIN WINDOW


root = tk.Tk()

root.title("Student Record Management System")
root.geometry("850x600")
root.configure(bg="#EAF2F8")

# Main heading
heading = tk.Label(
    root,
    text="STUDENT RECORD MANAGEMENT SYSTEM",
    font=("Arial", 19, "bold"),
    bg="#1F4E79",
    fg="white",
    pady=15
)

heading.pack(fill="x")



# BLOCK 9: STUDENT INPUT FORM


form_frame = tk.Frame(root, bg="#EAF2F8", pady=15)
form_frame.pack()

tk.Label(
    form_frame, text="Roll Number:",
    font=("Arial", 11), bg="#EAF2F8"
).grid(row=0, column=0, padx=10, pady=8, sticky="w")

roll_entry = tk.Entry(form_frame, width=25)
roll_entry.grid(row=0, column=1, padx=10, pady=8)

tk.Label(
    form_frame, text="Student Name:",
    font=("Arial", 11), bg="#EAF2F8"
).grid(row=1, column=0, padx=10, pady=8, sticky="w")

name_entry = tk.Entry(form_frame, width=25)
name_entry.grid(row=1, column=1, padx=10, pady=8)

tk.Label(
    form_frame, text="Course:",
    font=("Arial", 11), bg="#EAF2F8"
).grid(row=2, column=0, padx=10, pady=8, sticky="w")

course_entry = tk.Entry(form_frame, width=25)
course_entry.grid(row=2, column=1, padx=10, pady=8)

tk.Label(
    form_frame, text="Marks:",
    font=("Arial", 11), bg="#EAF2F8"
).grid(row=3, column=0, padx=10, pady=8, sticky="w")

marks_entry = tk.Entry(form_frame, width=25)
marks_entry.grid(row=3, column=1, padx=10, pady=8)



# BLOCK 10: BUTTONS


button_frame = tk.Frame(root, bg="#EAF2F8")
button_frame.pack(pady=10)

tk.Button(
    button_frame, text="Add Student",
    command=add_student, width=14,
    bg="#2E8B57", fg="white"
).grid(row=0, column=0, padx=5, pady=5)

tk.Button(
    button_frame, text="View All",
    command=view_students, width=14,
    bg="#2874A6", fg="white"
).grid(row=0, column=1, padx=5, pady=5)

tk.Button(
    button_frame, text="Search",
    command=search_student, width=14,
    bg="#7D3C98", fg="white"
).grid(row=0, column=2, padx=5, pady=5)

tk.Button(
    button_frame, text="Update Marks",
    command=update_student, width=14,
    bg="#D68910", fg="white"
).grid(row=0, column=3, padx=5, pady=5)

tk.Button(
    button_frame, text="Delete",
    command=delete_student, width=14,
    bg="#C0392B", fg="white"
).grid(row=1, column=0, padx=5, pady=5)

tk.Button(
    button_frame, text="Clear",
    command=clear_fields, width=14,
    bg="#566573", fg="white"
).grid(row=1, column=1, padx=5, pady=5)



# BLOCK 11: STUDENT RECORD TABLE


table_frame = tk.Frame(root)
table_frame.pack(pady=20, padx=20, fill="both", expand=True)

student_table = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings"
)

for column in columns:
    student_table.heading(column, text=column)
    student_table.column(column, width=150, anchor="center")

student_table.pack(fill="both", expand=True)



# BLOCK 12: RUN APPLICATION


root.mainloop()
