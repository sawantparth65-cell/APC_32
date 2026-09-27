# ============================================================
#                PYTHON OOP PROGRAMS
# ============================================================


# ============================================================
# 1. STUDENT DETAILS AND PERCENTAGE
# ============================================================

class Student1:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def percentage(self):
        return sum(self.marks) / len(self.marks)

    def display(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", self.percentage(), "%")
        print()


student1 = Student1(101, "Rahul", [80, 75, 90, 85, 70])
student2 = Student1(102, "Amit", [70, 65, 80, 75, 85])
student3 = Student1(103, "Priya", [90, 88, 95, 92, 85])

student1.display()
student2.display()
student3.display()


# ============================================================
# 2. EMPLOYEE - HRA, DA AND GROSS SALARY
# ============================================================

class Employee2:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_hra(self):
        return self.basic_salary * 0.20

    def calculate_da(self):
        return self.basic_salary * 0.10

    def gross_salary(self):
        return (
            self.basic_salary
            + self.calculate_hra()
            + self.calculate_da()
        )

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic Salary:", self.basic_salary)
        print("HRA:", self.calculate_hra())
        print("DA:", self.calculate_da())
        print("Gross Salary:", self.gross_salary())
        print()


employee2 = Employee2(101, "Rahul", 50000)
employee2.display()


# ============================================================
# 3. RECTANGLE - AREA AND PERIMETER
# ============================================================

class Rectangle3:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


rectangle3 = Rectangle3(10, 5)

print("Length:", rectangle3.length)
print("Breadth:", rectangle3.breadth)
print("Area:", rectangle3.area())
print("Perimeter:", rectangle3.perimeter())
print()


# ============================================================
# 4. CIRCLE - AREA AND CIRCUMFERENCE
# ============================================================

class Circle4:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius


circle4 = Circle4(7)

print("Radius:", circle4.radius)
print("Area:", circle4.area())
print("Circumference:", circle4.circumference())
print()


# ============================================================
# 5. BOOK DETAILS
# ============================================================

class Book5:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print()


book1 = Book5(
    101,
    "Python Programming",
    "John Smith",
    500
)

book2 = Book5(
    102,
    "Java Programming",
    "James Gosling",
    600
)

book3 = Book5(
    103,
    "C++ Programming",
    "Bjarne Stroustrup",
    700
)

book1.display()
book2.display()
book3.display()


# ============================================================
# 6. ELECTRICITY BILL
# ============================================================

class ElectricityBill6:
    def __init__(self, consumer_no, consumer_name, units):
        self.consumer_no = consumer_no
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):

        if self.units <= 100:
            bill = self.units * 1.50

        elif self.units <= 200:
            bill = (
                100 * 1.50
                + (self.units - 100) * 2.50
            )

        elif self.units <= 500:
            bill = (
                100 * 1.50
                + 100 * 2.50
                + (self.units - 200) * 4.00
            )

        else:
            bill = (
                100 * 1.50
                + 100 * 2.50
                + 300 * 4.00
                + (self.units - 500) * 6.00
            )

        return bill

    def display(self):
        print("Consumer Number:", self.consumer_no)
        print("Consumer Name:", self.consumer_name)
        print("Units Consumed:", self.units)
        print("Electricity Bill:", self.calculate_bill())
        print()


bill6 = ElectricityBill6(
    1001,
    "Rahul",
    350
)

bill6.display()


# ============================================================
# 7. MOBILE PHONE - SPECIFICATIONS AND DISCOUNT
# ============================================================

class MobilePhone7:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display_specifications(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Price:", self.price)

    def discounted_price(self, discount):
        return self.price - (
            self.price * discount / 100
        )


phone7 = MobilePhone7(
    "Samsung",
    "Galaxy S25",
    "256 GB",
    70000
)

phone7.display_specifications()

print("Price after 10% discount:",
      phone7.discounted_price(10))
print()


# ============================================================
# 8. PATIENT - INFORMATION AND TOTAL BILL
# ============================================================

class Patient8:
    def __init__(
        self,
        patient_id,
        name,
        age,
        disease,
        consultation_fee
    ):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def total_bill(self):
        medicine_charge = 1000
        return self.consultation_fee + medicine_charge

    def display(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Consultation Fee:", self.consultation_fee)
        print("Total Bill:", self.total_bill())
        print()


patient8 = Patient8(
    501,
    "Amit",
    30,
    "Fever",
    500
)

patient8.display()


# ============================================================
# 9. ATM - MENU DRIVEN PROGRAM
# ============================================================

class ATM9:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Current Balance:", self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited:", amount)
            print("New Balance:", self.balance)
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")

        elif amount > self.balance:
            print("Insufficient balance")

        else:
            self.balance -= amount
            print("Amount withdrawn:", amount)
            print("Remaining Balance:", self.balance)

    def display_account(self):
        print("\n--- Account Details ---")
        print("Account Number:", self.account_no)
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


atm9 = ATM9(
    "ACC101",
    "Rahul",
    10000
)

while True:

    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Display Account Details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        atm9.check_balance()

    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        atm9.deposit(amount)

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        atm9.withdraw(amount)

    elif choice == "4":
        atm9.display_account()

    elif choice == "5":
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")


# ============================================================
# 10. VEHICLE RENTAL
# ============================================================

class Vehicle10:
    def __init__(
        self,
        vehicle_no,
        model,
        rental_rate,
        availability=True
    ):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate = rental_rate
        self.availability = availability

    def rent_vehicle(self):
        if self.availability:
            self.availability = False
            print("Vehicle rented successfully")
        else:
            print("Vehicle is not available")

    def return_vehicle(self):
        self.availability = True
        print("Vehicle returned successfully")

    def calculate_rental(self, days):
        return self.rental_rate * days

    def display(self):
        print("Vehicle Number:", self.vehicle_no)
        print("Model:", self.model)
        print("Rental Rate:", self.rental_rate)
        print("Available:", self.availability)


vehicle10 = Vehicle10(
    "MH12AB1234",
    "Toyota Innova",
    2500
)

vehicle10.display()

vehicle10.rent_vehicle()

days = 3
print(
    "Rental Charges for",
    days,
    "days:",
    vehicle10.calculate_rental(days)
)

vehicle10.return_vehicle()
vehicle10.display()


# ============================================================
# 11. SHOPPING CART
# ============================================================

class ShoppingCart11:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = []

    def add_product(self, name, price, quantity):
        product = {
            "name": name,
            "price": price,
            "quantity": quantity
        }

        self.products.append(product)
        print(name, "added to cart")

    def remove_product(self, name):
        for product in self.products:
            if product["name"] == name:
                self.products.remove(product)
                print(name, "removed from cart")
                return

        print("Product not found")

    def calculate_total(self):
        total = 0

        for product in self.products:
            total += (
                product["price"]
                * product["quantity"]
            )

        return total

    def display_cart(self):
        print("\n--- Shopping Cart ---")
        print("Customer:", self.customer_name)
        print("Cart ID:", self.cart_id)

        for product in self.products:
            print(
                product["name"],
                "- Price:",
                product["price"],
                "- Quantity:",
                product["quantity"]
            )

        print("Total Bill:", self.calculate_total())

    def __del__(self):
        print(
            "Shopping cart",
            self.cart_id,
            "has been destroyed."
        )


cart11 = ShoppingCart11(
    "Rahul",
    "CART101"
)

cart11.add_product("Laptop", 60000, 1)
cart11.add_product("Mouse", 1000, 2)
cart11.add_product("Keyboard", 2000, 1)

cart11.display_cart()

cart11.remove_product("Mouse")

cart11.display_cart()


# ============================================================
# 12. FOOD ORDER - CONSTRUCTOR AND DESTRUCTOR
# ============================================================

class FoodOrder12:
    def __init__(
        self,
        order_id,
        customer_name,
        food_item,
        quantity,
        price
    ):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def calculate_bill(self):
        subtotal = self.quantity * self.price
        tax = subtotal * 0.05
        total = subtotal + tax

        return total

    def display(self):
        print("Order ID:", self.order_id)
        print("Customer:", self.customer_name)
        print("Food Item:", self.food_item)
        print("Quantity:", self.quantity)
        print("Price:", self.price)
        print("Total Bill including 5% tax:",
              self.calculate_bill())

    def __del__(self):
        print(
            "Order",
            self.order_id,
            "completed."
        )


order12 = FoodOrder12(
    1001,
    "Amit",
    "Pizza",
    2,
    300
)

order12.display()


# ============================================================
# 13. STUDENT RESULT - CONSTRUCTOR AND DESTRUCTOR
# ============================================================

class StudentResult13:
    def __init__(
        self,
        name,
        m1,
        m2,
        m3,
        m4,
        m5
    ):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5

    def total(self):
        return (
            self.m1
            + self.m2
            + self.m3
            + self.m4
            + self.m5
        )

    def percentage(self):
        return self.total() / 5

    def grade(self):
        percentage = self.percentage()

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        print("Student Name:", self.name)
        print("Total Marks:", self.total())
        print("Percentage:", self.percentage(), "%")
        print("Grade:", self.grade())

    def __del__(self):
        print(
            "Result object for",
            self.name,
            "has been destroyed."
        )


result13 = StudentResult13(
    "Priya",
    85,
    90,
    78,
    88,
    92
)

result13.display()