import tkinter as tk
from tkinter import messagebox

# mian window
root = tk.Tk()
root.title("Student Management System")
root.geometry("600x500")

students = []

# functions

def show_courses():
    course_box.grid(row=3, column=3, padx=15, pady=5, sticky="nw")

def submit_data():
    msg_label.config(text="")
    name = name_entry.get()
    age = age_entry.get()
    courses = course_entry.get()
    if name == "" or age == "" or courses == "":
        msg_label.config(text="Please fill all details!", fg= "red")
        return
    record = f"{name} | Age: {age} | Courses: {courses}"
    # auto remove old record if more than 5
    if len(students) >= 5:
        students.pop(0)

    students.append(record)
    update_display()

    # clear fields
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    msg_label.config(text="Record added successfully!", fg="green")

def update_display():
    display_box.delete(0, tk.END)
    for s in students:
        display_box.insert(tk.END, s)
    
def delete_student():
    msg_label.config(text="")
    selected = display_box.curselection()
    if not selected:
        msg_label.config(text="Select a record to delete", fg="orange")
        return
    students.pop(selected[0])
    update_display()
    msg_label.config(text="Record deleted successfully!", fg="green")

# Frame for form
Frame_ = tk.Frame(root, padx=30, pady=20)
Frame_.pack(pady=10)
tk.Label(Frame_,text="Student Management System", font = ("Arial",20, "bold")).grid(row=0, columnspan=4,pady=20)


#name
tk.Label(Frame_, text="Name").grid(row=1, column=0,padx=10,pady=8,sticky="w")
name_entry = tk.Entry(Frame_, width=30)
name_entry.grid(row=1, column=1,padx=10,pady=8)

#age
tk.Label(Frame_, text="Age").grid(row=2, column=0, padx=10, pady=8)
age_entry = tk.Entry(Frame_, width=30)
age_entry.grid(row=2, column=1, padx=10, pady=8)

#course
tk.Label(Frame_, text="Courses:").grid(row=3, column=0, padx=10, pady=8, sticky="w")
course_entry = tk.Entry(Frame_, width=30)
course_entry.grid(row=3, column=1, padx=10, pady=8)

tk.Button(Frame_, text="List", command=show_courses).grid(row=3, column=2, padx=10)

# submit button")
tk.Button(Frame_, text="Submit", bg="green", fg="white", command=submit_data).grid(row=4, columnspan=4, pady=20)

# message label
msg_label = tk.Label(root, text="", font=("Arial", 10))
msg_label.pack()

# display box
display_Frame = tk.Frame(root)
display_Frame.pack(pady=15)

display_box = tk.Listbox(display_Frame, width=55, height=10)
display_box.pack()

tk.Button(display_Frame, text="Delete Selected", bg="red", fg="white", command=delete_student).pack(pady=10)

# course listbox
course_box = tk.Frame(Frame_, bd=2, relief="solid", padx=10, pady=5)

course_label = tk.Label(
    course_box,
    text="Available Courses:\n\n"
    "Python\nJava\nAI\nData Science\nWeb Development",
    justify="left"
)
course_label.pack()
root.mainloop()