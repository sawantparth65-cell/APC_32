# ============================================================
# PYTHON PRACTICALS - FILE HANDLING, MODULES, PACKAGES
# All programs combined into ONE Python file
# ============================================================

# ============================================================
# PART A - FILE HANDLING
# ============================================================

# ============================================================
# 1. Create student.txt and write student details
# ============================================================

def program_1():
    with open("student.txt", "w") as f:
        f.write("Name: Parth Sawant\n")
        f.write("Roll No: 32\n")
        f.write("Branch: CSE\n")
        f.write("Semester: 5\n")
    print("Student information written successfully.")


# ============================================================
# 2. Open a text file and display complete contents
# ============================================================

def program_2():
    with open("student.txt", "r") as f:
        print(f.read())


# ============================================================
# 3. Append additional student information
# ============================================================

def program_3():
    with open("student.txt", "a") as f:
        f.write("College: D.Y. Patil College of Engineering and Technology\n")
        f.write("City: Kolhapur\n")
    print("Information appended successfully.")


# ============================================================
# 4. Read a text file line by line
# ============================================================

def program_4():
    with open("student.txt", "r") as f:
        for line in f:
            print(line.strip())


# ============================================================
# 5. Count total number of lines
# ============================================================

def program_5():
    with open("student.txt", "r") as f:
        lines = f.readlines()
    print("Total number of lines:", len(lines))


# ============================================================
# 6. Count total number of words
# ============================================================

def program_6():
    with open("student.txt", "r") as f:
        data = f.read()
    print("Total number of words:", len(data.split()))


# ============================================================
# 7. Count total number of characters including spaces
# ============================================================

def program_7():
    with open("student.txt", "r") as f:
        data = f.read()
    print("Total characters:", len(data))


# ============================================================
# 8. Display lines in reverse order
# ============================================================

def program_8():
    with open("student.txt", "r") as f:
        lines = f.readlines()

    for line in reversed(lines):
        print(line.strip())


# ============================================================
# 9. Count vowels and consonants
# ============================================================

def program_9():
    with open("student.txt", "r") as f:
        data = f.read()

    vowels = 0
    consonants = 0

    for ch in data:
        if ch.isalpha():
            if ch.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1

    print("Vowels:", vowels)
    print("Consonants:", consonants)


# ============================================================
# 10. Count alphabets, digits, spaces and special characters
# ============================================================

def program_10():
    with open("student.txt", "r") as f:
        data = f.read()

    alphabets = digits = spaces = special = 0

    for ch in data:
        if ch.isalpha():
            alphabets += 1
        elif ch.isdigit():
            digits += 1
        elif ch.isspace():
            spaces += 1
        else:
            special += 1

    print("Alphabets:", alphabets)
    print("Digits:", digits)
    print("Spaces:", spaces)
    print("Special characters:", special)


# ============================================================
# 11. Find the longest word
# ============================================================

def program_11():
    with open("student.txt", "r") as f:
        data = f.read()

    words = data.split()

    if words:
        longest = max(words, key=len)
        print("Longest word:", longest)


# ============================================================
# 12. Count occurrence of each word using dictionary
# ============================================================

def program_12():
    with open("student.txt", "r") as f:
        data = f.read().lower()

    words = data.split()
    frequency = {}

    for word in words:
        word = word.strip(".,!?")

        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    print("Word Frequency:")
    print(frequency)


# ============================================================
# 13. Search a word and display occurrences and line numbers
# ============================================================

def program_13():
    word = input("Enter word to search: ")

    count = 0
    line_number = 0

    with open("student.txt", "r") as f:
        for line in f:
            line_number += 1

            for w in line.split():
                if w.lower().strip(".,!?") == word.lower():
                    count += 1
                    print("Found in line:", line_number)

    print("Total occurrences:", count)


# ============================================================
# 14. Replace a specified word with another word
# ============================================================

def program_14():
    old_word = input("Enter word to replace: ")
    new_word = input("Enter new word: ")

    with open("student.txt", "r") as f:
        data = f.read()

    data = data.replace(old_word, new_word)

    with open("student.txt", "w") as f:
        f.write(data)

    print("Word replaced successfully.")


# ============================================================
# 15. Remove single-line comments from Python source file
# ============================================================

def program_15():
    input_file = input("Enter Python source filename: ")
    output_file = "without_comments.py"

    try:
        with open(input_file, "r") as f:
            with open(output_file, "w") as out:
                for line in f:
                    if not line.strip().startswith("#"):
                        out.write(line)

        print("Comments removed successfully.")
        print("Output file:", output_file)

    except FileNotFoundError:
        print("Input file not found.")


# ============================================================
# 16. Create uppercase copy of a text file
# ============================================================

def program_16():
    with open("student.txt", "r") as f:
        data = f.read()

    with open("uppercase.txt", "w") as out:
        out.write(data.upper())

    print("Uppercase file created.")


# ============================================================
# 17. Student Records
# ============================================================

def program_17():
    records = [
        ("101", "Amit", 85),
        ("102", "Priya", 92),
        ("103", "Rahul", 78)
    ]

    print("All Records:")
    for record in records:
        print(record)

    highest = max(records, key=lambda x: x[2])

    print("\nStudent with highest marks:")
    print(highest)

    total = sum(record[2] for record in records)
    average = total / len(records)

    print("\nAverage Marks:", average)

    print("\nStudents scoring more than 80:")
    for record in records:
        if record[2] > 80:
            print(record)


# ============================================================
# 18. Employee Records
# ============================================================

def program_18():
    employees = [
        ("101", "Amit", "IT", 50000),
        ("102", "Priya", "HR", 60000),
        ("103", "Rahul", "Sales", 45000)
    ]

    def display_employees():
        for employee in employees:
            print(employee)

    def highest_paid():
        return max(employees, key=lambda x: x[3])

    def average_salary():
        return sum(employee[3] for employee in employees) / len(employees)

    def above_salary(amount):
        for employee in employees:
            if employee[3] > amount:
                print(employee)

    print("All Employees:")
    display_employees()

    print("\nHighest Paid Employee:")
    print(highest_paid())

    print("\nAverage Salary:", average_salary())

    amount = float(input("\nEnter salary: "))
    print("\nEmployees earning above given salary:")
    above_salary(amount)


# ============================================================
# 19. Student Attendance
# ============================================================

def program_19():
    attendance = [
        ("101", "Amit", 70, 100),
        ("102", "Priya", 90, 100),
        ("103", "Rahul", 65, 100)
    ]

    for roll, name, present, total in attendance:
        percentage = (present / total) * 100

        print(name, "Attendance:", percentage, "%")

        if percentage < 75:
            print("Below 75%")


# ============================================================
# 20. Deposits and Withdrawals
# ============================================================

def program_20():
    transactions = [
        ("deposit", 10000),
        ("withdraw", 2000),
        ("deposit", 5000),
        ("withdraw", 1000)
    ]

    total_deposit = 0
    total_withdrawal = 0
    amounts = []

    for transaction_type, amount in transactions:
        amounts.append(amount)

        if transaction_type == "deposit":
            total_deposit += amount
        elif transaction_type == "withdraw":
            total_withdrawal += amount

    balance = total_deposit - total_withdrawal
    largest = max(amounts)

    print("Total Deposits:", total_deposit)
    print("Total Withdrawals:", total_withdrawal)
    print("Final Balance:", balance)
    print("Largest Transaction:", largest)


# ============================================================
# 21. Book Management System
# ============================================================

def program_21():
    books = []

    def add_book():
        book_id = input("Enter Book ID: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")

        books.append({
            "id": book_id,
            "title": title,
            "author": author,
            "available": True
        })

        print("Book added.")

    def search_book():
        book_id = input("Enter Book ID: ")

        for book in books:
            if book["id"] == book_id:
                print(book)
                return

        print("Book not found.")

    def issue_book():
        book_id = input("Enter Book ID: ")

        for book in books:
            if book["id"] == book_id:
                if book["available"]:
                    book["available"] = False
                    print("Book issued.")
                else:
                    print("Book already issued.")
                return

        print("Book not found.")

    def return_book():
        book_id = input("Enter Book ID: ")

        for book in books:
            if book["id"] == book_id:
                book["available"] = True
                print("Book returned.")
                return

        print("Book not found.")

    def display_available():
        print("Available Books:")
        for book in books:
            if book["available"]:
                print(book)

    # Add sample books so the program can be tested immediately
    books.append({
        "id": "101",
        "title": "Python Programming",
        "author": "ABC",
        "available": True
    })

    while True:
        print("\n1. Add Book")
        print("2. Search Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Display Available Books")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            search_book()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            display_available()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")


# ============================================================
# 22. Combine Two Text Files into Third File
# ============================================================

def program_22():
    with open("file1.txt", "w") as f:
        f.write("This is the first file.\n")

    with open("file2.txt", "w") as f:
        f.write("This is the second file.\n")

    with open("file1.txt", "r") as f1:
        data1 = f1.read()

    with open("file2.txt", "r") as f2:
        data2 = f2.read()

    with open("file3.txt", "w") as f3:
        f3.write(data1)
        f3.write(data2)

    print("Files combined successfully into file3.txt.")


# ============================================================
# 23. Compare Two Text Files
# ============================================================

def program_23():
    # Sample files for demonstration
    with open("compare1.txt", "w") as f:
        f.write("Hello Python\n")
        f.write("File Handling\n")

    with open("compare2.txt", "w") as f:
        f.write("Hello Python\n")
        f.write("File Handling\n")

    with open("compare1.txt", "r") as f1:
        lines1 = f1.readlines()

    with open("compare2.txt", "r") as f2:
        lines2 = f2.readlines()

    if lines1 == lines2:
        print("Both files are identical.")
    else:
        print("Files are different.")

        minimum = min(len(lines1), len(lines2))

        for i in range(minimum):
            if lines1[i] != lines2[i]:
                print("First difference is at line:", i + 1)
                print("File 1:", lines1[i])
                print("File 2:", lines2[i])
                break


# ============================================================
# PART B - MODULES
# ============================================================

# ============================================================
# 1. Calculator Module
# ============================================================

def program_24():
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        return a / b

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("Addition:", add(a, b))
    print("Subtraction:", subtract(a, b))
    print("Multiplication:", multiply(a, b))

    if b != 0:
        print("Division:", divide(a, b))
    else:
        print("Division by zero is not possible.")


# ============================================================
# 2. Student Result Module
# ============================================================

def program_25():
    def total(m1, m2, m3):
        return m1 + m2 + m3

    def percentage(total_marks):
        return total_marks / 3

    def grade(per):
        if per >= 75:
            return "A"
        elif per >= 60:
            return "B"
        elif per >= 50:
            return "C"
        elif per >= 40:
            return "D"
        else:
            return "F"

    m1 = int(input("Enter marks 1: "))
    m2 = int(input("Enter marks 2: "))
    m3 = int(input("Enter marks 3: "))

    t = total(m1, m2, m3)
    p = percentage(t)

    print("Total:", t)
    print("Percentage:", p)
    print("Grade:", grade(p))


# ============================================================
# 3. Number Utilities Module
# ============================================================

def program_26():
    def prime(n):
        if n < 2:
            return False

        for i in range(2, n):
            if n % i == 0:
                return False

        return True

    def palindrome(n):
        return str(n) == str(n)[::-1]

    def armstrong(n):
        digits = str(n)
        total = 0

        for digit in digits:
            total += int(digit) ** len(digits)

        return total == n

    def perfect(n):
        if n <= 0:
            return False

        total = 0

        for i in range(1, n):
            if n % i == 0:
                total += i

        return total == n

    n = int(input("Enter number: "))

    print("Prime:", prime(n))
    print("Palindrome:", palindrome(n))
    print("Armstrong:", armstrong(n))
    print("Perfect:", perfect(n))


# ============================================================
# 4. String Utilities Module
# ============================================================

def program_27():
    def count_vowels(s):
        return sum(1 for ch in s.lower() if ch in "aeiou")

    def reverse(s):
        return s[::-1]

    def palindrome(s):
        return s == s[::-1]

    def count_words(s):
        return len(s.split())

    def remove_spaces(s):
        return s.replace(" ", "")

    s = input("Enter string: ")

    print("Vowels:", count_vowels(s))
    print("Reverse:", reverse(s))
    print("Palindrome:", palindrome(s))
    print("Words:", count_words(s))
    print("Without spaces:", remove_spaces(s))


# ============================================================
# 5. Salary Module
# ============================================================

def program_28():
    def gross_salary(basic, allowance):
        return basic + allowance

    def deductions(gross):
        return gross * 0.10

    def net_salary(gross):
        return gross - deductions(gross)

    basic = float(input("Enter basic salary: "))
    allowance = float(input("Enter allowance: "))

    gross = gross_salary(basic, allowance)

    print("Gross Salary:", gross)
    print("Deductions:", deductions(gross))
    print("Net Salary:", net_salary(gross))


# ============================================================
# 6. Recursive Functions Module
# ============================================================

def program_29():
    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n - 1)

    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    def sum_digits(n):
        if n == 0:
            return 0
        return n % 10 + sum_digits(n // 10)

    def binary(n):
        if n == 0:
            return ""
        return binary(n // 2) + str(n % 2)

    n = int(input("Enter number: "))

    print("Factorial:", factorial(n))
    print("Fibonacci:", fibonacci(n))
    print("Sum of digits:", sum_digits(n))
    print("Binary:", binary(n) if n != 0 else "0")


# ============================================================
# PART C - PACKAGES AND DIRECTORIES
# ============================================================

# ============================================================
# 7. mathutils Package
# basic.py, number.py, statistics.py
# ============================================================

def program_30():
    # basic.py functions
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    # number.py functions
    def prime(n):
        if n < 2:
            return False

        for i in range(2, n):
            if n % i == 0:
                return False

        return True

    def palindrome(n):
        return str(n) == str(n)[::-1]

    def armstrong(n):
        digits = str(n)
        return sum(int(d) ** len(digits) for d in digits) == n

    # statistics.py functions
    def mean(numbers):
        return sum(numbers) / len(numbers)

    def maximum(numbers):
        return max(numbers)

    def minimum(numbers):
        return min(numbers)

    print("Addition:", add(10, 5))
    print("Subtraction:", subtract(10, 5))

    n = 121

    print("Prime:", prime(n))
    print("Palindrome:", palindrome(n))
    print("Armstrong:", armstrong(n))

    numbers = [10, 20, 30, 40]

    print("Mean:", mean(numbers))
    print("Maximum:", maximum(numbers))
    print("Minimum:", minimum(numbers))


# ============================================================
# 8. student Package
# marks.py, grade.py, attendance.py
# ============================================================

def program_31():
    def total(m1, m2, m3):
        return m1 + m2 + m3

    def percentage(total_marks):
        return total_marks / 3

    def grade(per):
        if per >= 75:
            return "A"
        elif per >= 60:
            return "B"
        elif per >= 50:
            return "C"
        elif per >= 40:
            return "D"
        else:
            return "F"

    def eligible(present, total_classes):
        return (present / total_classes) * 100 >= 75

    m1, m2, m3 = 80, 75, 90

    t = total(m1, m2, m3)
    p = percentage(t)

    print("Total:", t)
    print("Percentage:", p)
    print("Grade:", grade(p))

    if eligible(80, 100):
        print("Student is eligible.")
    else:
        print("Student is not eligible.")


# ============================================================
# 9. banking Package
# account.py, transaction.py, loan.py
# ============================================================

def program_32():
    def create_account(name, balance):
        return {"name": name, "balance": balance}

    def get_balance(account):
        return account["balance"]

    def deposit(account, amount):
        account["balance"] += amount

    def withdraw(account, amount):
        if amount <= account["balance"]:
            account["balance"] -= amount
        else:
            print("Insufficient balance.")

    def loan_amount(principal, rate, years):
        interest = principal * rate * years / 100
        return principal + interest

    account = create_account("Parth", 10000)

    deposit(account, 5000)
    withdraw(account, 2000)

    print("Balance:", get_balance(account))
    print("Loan Amount:", loan_amount(100000, 8, 2))


# ============================================================
# 10. texttools Package
# cleaning.py, tokenization.py, frequency.py
# ============================================================

def program_33():
    import string

    def remove_punctuation(text):
        return text.translate(str.maketrans("", "", string.punctuation))

    def remove_extra_spaces(text):
        return " ".join(text.split())

    def tokenize(text):
        return text.split()

    def frequency(text):
        result = {}

        for word in text.split():
            result[word] = result.get(word, 0) + 1

        return result

    text = "Hello, Python! Python is easy."

    clean = remove_punctuation(text)
    clean = remove_extra_spaces(clean)

    print("Clean text:", clean)
    print("Tokens:", tokenize(clean))
    print("Frequency:", frequency(clean))


# ============================================================
# 11. College Project Directory
# student and faculty packages
# ============================================================

def program_34():
    def student_details():
        print("Name: Parth")
        print("Roll No: 32")
        print("Branch: CSE")

    def student_marks():
        print("Python: 85")
        print("Java: 80")
        print("Cloud: 90")

    def faculty_details():
        print("Faculty Name: Professor ABC")
        print("Department: Computer Science")

    print("Student Information")
    student_details()
    student_marks()

    print("\nFaculty Information")
    faculty_details()


# ============================================================
# 12. Library Application
# Books, Members, Transactions packages
# ============================================================

def program_35():
    def add_book(title):
        print("Book added:", title)

    def search_book(title):
        print("Searching for:", title)

    def add_member(name):
        print("Member added:", name)

    def search_member(name):
        print("Searching member:", name)

    def issue_book(book, member):
        print(book, "issued to", member)

    def return_book(book):
        print(book, "returned")

    add_book("Python Programming")
    search_book("Python Programming")

    add_member("Parth")
    search_member("Parth")

    issue_book("Python Programming", "Parth")
    return_book("Python Programming")


# ============================================================
# 13. Ecommerce Directory
# Products, Customers, Orders, Payments
# ============================================================

def program_36():
    def add_product(name, price):
        print("Product:", name)
        print("Price:", price)

    def search_product(name):
        print("Searching product:", name)

    def add_customer(name):
        print("Customer added:", name)

    def customer_profile(name):
        print("Customer profile:", name)

    def create_order(product):
        print("Order created for:", product)

    def order_status():
        print("Order Status: Shipped")

    def make_payment(amount):
        print("Payment successful:", amount)

    def refund(amount):
        print("Refund processed:", amount)

    add_product("Laptop", 50000)
    search_product("Laptop")

    add_customer("Parth")
    customer_profile("Parth")

    create_order("Laptop")
    order_status()

    make_payment(50000)
    refund(5000)


# ============================================================
# 14. Medical Management Project
# Patients, Doctors, Billing, Medical Records
# ============================================================

def program_37():
    def add_patient(name, age):
        print("Patient:", name)
        print("Age:", age)

    def search_patient(name):
        print("Searching patient:", name)

    def add_doctor(name, specialization):
        print("Doctor:", name)
        print("Specialization:", specialization)

    def doctor_schedule():
        print("Doctor available from 10 AM to 2 PM")

    def create_bill(amount):
        print("Total Bill:", amount)

    def make_payment(amount):
        print("Payment received:", amount)

    def add_record(patient, disease):
        print("Patient:", patient)
        print("Disease:", disease)

    def show_history(patient):
        print("Medical history of:", patient)

    add_patient("Parth", 20)
    search_patient("Parth")

    add_doctor("Dr. Sharma", "Cardiologist")
    doctor_schedule()

    add_record("Parth", "Fever")
    show_history("Parth")

    create_bill(5000)
    make_payment(5000)


# ============================================================
# MAIN MENU
# ============================================================

def main():
    programs = {
        1: program_1,
        2: program_2,
        3: program_3,
        4: program_4,
        5: program_5,
        6: program_6,
        7: program_7,
        8: program_8,
        9: program_9,
        10: program_10,
        11: program_11,
        12: program_12,
        13: program_13,
        14: program_14,
        15: program_15,
        16: program_16,
        17: program_17,
        18: program_18,
        19: program_19,
        20: program_20,
        21: program_21,
        22: program_22,
        23: program_23,
        24: program_24,
        25: program_25,
        26: program_26,
        27: program_27,
        28: program_28,
        29: program_29,
        30: program_30,
        31: program_31,
        32: program_32,
        33: program_33,
        34: program_34,
        35: program_35,
        36: program_36,
        37: program_37
    }

    while True:
        print("\n" + "=" * 60)
        print("PYTHON PRACTICAL PROGRAMS")
        print("=" * 60)

        print("\nFILE HANDLING")
        for i in range(1, 24):
            print(f"{i}. Program {i}")

        print("\nMODULES")
        for i in range(24, 30):
            print(f"{i}. Program {i}")

        print("\nPACKAGES AND DIRECTORIES")
        for i in range(30, 38):
            print(f"{i}. Program {i}")

        print("\n0. Exit")

        try:
            choice = int(input("\nEnter program number: "))

            if choice == 0:
                print("Program ended.")
                break

            if choice in programs:
                print("\n" + "=" * 60)
                print("Running Program", choice)
                print("=" * 60)
                programs[choice]()
            else:
                print("Invalid program number.")

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
