import csv

def search_student_by_roll(file_path, roll_number):
    found = False

    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['Roll Number'] == str(roll_number):
                print("Student record found")

                for key, value in row.items():
                    print(f"{key}: {value}")

                found = True
                break

    if not found:
        print(f"No student found with Roll Number: {roll_number}")


n=int(input("Enter roll no to search:bv                           "))
print(search_student_by_roll("student.csv", n))