""""
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Student Registration")
root.geometry("300x300")

tk.Label(root, text="Student Registration Form",
         font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Name").pack()
name = tk.Entry(root)
name.pack()

tk.Label(root, text="Age").pack()
age = tk.Entry(root)
age.pack()

tk.Label(root, text="Gender").pack()
gender = tk.StringVar(value="Male")

tk.Radiobutton(root, text="Male", variable=gender,
               value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender,
               value="Female").pack()

def submit():
    messagebox.showinfo(
        "Registration Details",
        f"Name: {name.get()}\n"
        f"Age: {age.get()}\n"
        f"Gender: {gender.get()}"
    )

tk.Button(root, text="Submit", command=submit).pack(pady=10)

root.mainloop()


#Validation
'''import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Student Registration")
root.geometry("300x350")

tk.Label(root, text="Student Registration",
         font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Name").pack()
name = tk.Entry(root)
name.pack()

tk.Label(root, text="Age").pack()
age = tk.Entry(root)
age.pack()

tk.Label(root, text="Gender").pack()
gender = tk.StringVar(value="Male")

tk.Radiobutton(root, text="Male", variable=gender,
               value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender,
               value="Female").pack()

def submit():
    n = name.get().strip()
    a = age.get().strip()

    # Name validation
    if n == "":
        messagebox.showerror("Error", "Please enter your name")
        return

    if not n.replace(" ", "").isalpha():
        messagebox.showerror("Error", "Name must contain letters only")
        return

    # Age validation
    if a == "":
        messagebox.showerror("Error", "Please enter your age")
        return

    if not a.isdigit():
        messagebox.showerror("Error", "Age must be a number")
        return

    if int(a) < 1 or int(a) > 100:
        messagebox.showerror("Error", "Enter age between 1 and 100")
        return

    messagebox.showinfo(
        "Success",
        f"Name: {n}\nAge: {a}\nGender: {gender.get()}"
    )

tk.Button(root, text="Submit", command=submit).pack(pady=15)

root.mainloop()

#Notepad

import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("Untitled - Notepad")
root.geometry("600x400")

current_file = None

# Text area
text = tk.Text(root, font=("Arial", 12), undo=True)
text.pack(expand=True, fill="both")

# New file
def new_file():
    global current_file
    if messagebox.askyesno("New", "Create a new file?"):
        text.delete("1.0", tk.END)
        current_file = None
        root.title("Untitled - Notepad")

# Open file
def open_file():
    global current_file
    file = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file:
        with open(file, "r", encoding="utf-8") as f:
            text.delete("1.0", tk.END)
            text.insert("1.0", f.read())
        current_file = file
        root.title(file + " - Notepad")

# Save file
def save_file():
    if current_file:
        with open(current_file, "w", encoding="utf-8") as f:
            f.write(text.get("1.0", "end-1c"))
        messagebox.showinfo("Save", "File saved successfully!")
    else:
        save_as()

# Save As
def save_as():
    global current_file
    file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file:
        current_file = file
        save_file()
        root.title(file + " - Notepad")

# Exit
def exit_app():
    if messagebox.askyesno("Exit", "Do you want to exit?"):
        root.destroy()

# Menu bar
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

# Edit menu

import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("Untitled - Notepad")
root.geometry("600x400")

current_file = None

# Text area
text = tk.Text(root, font=("Arial", 12), undo=True)
text.pack(expand=True, fill="both")

# New file
def new_file():
    global current_file
    if messagebox.askyesno("New", "Create a new file?"):
        text.delete("1.0", tk.END)
        current_file = None
        root.title("Untitled - Notepad")

# Open file
def open_file():
    global current_file
    file = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file:
        with open(file, "r", encoding="utf-8") as f:
            text.delete("1.0", tk.END)
            text.insert("1.0", f.read())
        current_file = file
        root.title(file + " - Notepad")

# Save file
def save_file():
    if current_file:
        with open(current_file, "w", encoding="utf-8") as f:
            f.write(text.get("1.0", "end-1c"))
        messagebox.showinfo("Save", "File saved successfully!")
    else:
        save_as()

# Save As
def save_as():
    global current_file
    file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file:
        current_file = file
        save_file()
        root.title(file + " - Notepad")

# Exit
def exit_app():
    if messagebox.askyesno("Exit", "Do you want to exit?"):
        root.destroy()

# Menu bar
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

# Edit menu
edit_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(
    label="Cut",
    command=lambda: text.event_generate("<<Cut>>")
)
edit_menu.add_command(
    label="Copy",
    command=lambda: text.event_generate("<<Copy>>")
)
edit_menu.add_command(
    label="Paste",
    command=lambda: text.event_generate("<<Paste>>")
)
edit_menu.add_command(
    label="Select All",
    command=lambda: text.tag_add("sel", "1.0", "end-1c")
)

root.mainloop()
"""
