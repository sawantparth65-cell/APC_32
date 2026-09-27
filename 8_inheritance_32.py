# ============================================================
#                     INHERITANCE
# ============================================================


# ============================================================
# 1. EMPLOYEE -> MANAGER
# ============================================================

class Employee1:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager1(Employee1):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)
        print("Annual Salary:", self.salary * 12)


m1 = Manager1(101, "Rahul", 50000, "IT")
m1.display()


# ============================================================
# 2. VEHICLE -> CAR
# ============================================================

class Vehicle2:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car2(Vehicle2):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def discounted_price(self, discount):
        return self.price - (self.price * discount / 100)

    def display(self):
        super().display()
        print("Fuel Type:", self.fuel_type)
        print("Price:", self.price)
        print("Discounted Price:", self.discounted_price(10))


c2 = Car2("Toyota", "Fortuner", "Diesel", 4000000)
c2.display()


# ============================================================
# 3. ACADEMIC + SPORTS -> STUDENT
# ============================================================

class Academic3:
    def __init__(self, marks):
        self.marks = marks


class Sports3:
    def __init__(self, sports_points):
        self.sports_points = sports_points


class Student3(Academic3, Sports3):
    def __init__(self, marks, sports_points):
        Academic3.__init__(self, marks)
        Sports3.__init__(self, sports_points)

    def performance(self):
        total = self.marks + self.sports_points
        print("Academic Marks:", self.marks)
        print("Sports Points:", self.sports_points)
        print("Overall Performance:", total)


s3 = Student3(85, 10)
s3.performance()


# ============================================================
# 4. PERSONAL DETAILS + PROFESSIONAL DETAILS -> EMPLOYEE
# ============================================================

class PersonalDetails4:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class ProfessionalDetails4:
    def __init__(self, emp_id, designation, salary):
        self.emp_id = emp_id
        self.designation = designation
        self.salary = salary


class Employee4(PersonalDetails4, ProfessionalDetails4):
    def __init__(self, name, age, emp_id, designation, salary):
        PersonalDetails4.__init__(self, name, age)
        ProfessionalDetails4.__init__(
            self, emp_id, designation, salary
        )

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Designation:", self.designation)
        print("Salary:", self.salary)


e4 = Employee4("Amit", 25, 101, "Developer", 60000)
e4.display()


# ============================================================
# 5. PERSON -> STUDENT -> RESEARCH STUDENT
# ============================================================

class Person5:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student5(Person5):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent5(Student5):
    def __init__(self, name, age, roll_no, course, topic, guide):
        super().__init__(name, age, roll_no, course)
        self.topic = topic
        self.guide = guide

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.topic)
        print("Guide:", self.guide)


r5 = ResearchStudent5(
    "Priya", 24, 101, "MCA",
    "Artificial Intelligence", "Dr. Sharma"
)
r5.display()


# ============================================================
# 6. BANK ACCOUNT -> SAVINGS ACCOUNT -> PREMIUM SAVINGS
# ============================================================

class BankAccount6:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance


class SavingsAccount6(BankAccount6):
    def __init__(self, account_no, balance, interest_rate):
        super().__init__(account_no, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100


class PremiumSavingsAccount6(SavingsAccount6):
    def __init__(
        self, account_no, balance, interest_rate, benefits
    ):
        super().__init__(account_no, balance, interest_rate)
        self.benefits = benefits

    def display(self):
        print("Account Number:", self.account_no)
        print("Balance:", self.balance)
        print("Interest Rate:", self.interest_rate)
        print("Interest:", self.calculate_interest())
        print("Benefits:", self.benefits)


p6 = PremiumSavingsAccount6(
    12345, 100000, 6, "Free Insurance"
)
p6.display()


# ============================================================
# 7. SHAPE -> CIRCLE, RECTANGLE, TRIANGLE
# ============================================================

class Shape7:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Shape:", self.name)


class Circle7(Shape7):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle7(Shape7):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle7(Shape7):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


c7 = Circle7(5)
r7 = Rectangle7(10, 5)
t7 = Triangle7(8, 6)

c7.display_name()
print("Area:", c7.area())

r7.display_name()
print("Area:", r7.area())

t7.display_name()
print("Area:", t7.area())


# ============================================================
# 8. EMPLOYEE -> MANAGER, DEVELOPER, TESTER
# ============================================================

class Employee8:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary


class Manager8(Employee8):
    def salary(self):
        return self.basic_salary + self.basic_salary * 0.30


class Developer8(Employee8):
    def salary(self):
        return self.basic_salary + self.basic_salary * 0.20


class Tester8(Employee8):
    def salary(self):
        return self.basic_salary + self.basic_salary * 0.15


m8 = Manager8(101, "Rahul", 50000)
d8 = Developer8(102, "Amit", 50000)
t8 = Tester8(103, "Priya", 50000)

print("Manager Salary:", m8.salary())
print("Developer Salary:", d8.salary())
print("Tester Salary:", t8.salary())


# ============================================================
# 9. PERSON -> STUDENT, FACULTY -> TEACHING ASSISTANT
# ============================================================

class Person9:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student9(Person9):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no


class Faculty9(Person9):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject


class TeachingAssistant9(Student9, Faculty9):
    def __init__(self, name, age, roll_no, subject):
        Person9.__init__(self, name, age)
        self.roll_no = roll_no
        self.subject = subject

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Subject:", self.subject)


ta9 = TeachingAssistant9("Rahul", 23, 101, "Python")
ta9.display()


# ============================================================
# 10. VEHICLE -> CAR, BIKE -> SPORTS CAR, ELECTRIC BIKE
# ============================================================

class Vehicle10:
    def __init__(self, brand):
        self.brand = brand


class Car10(Vehicle10):
    def __init__(self, brand, seats):
        super().__init__(brand)
        self.seats = seats


class Bike10(Vehicle10):
    def __init__(self, brand, engine):
        super().__init__(brand)
        self.engine = engine


class SportsCar10(Car10):
    def __init__(self, brand, seats, top_speed):
        super().__init__(brand, seats)
        self.top_speed = top_speed

    def display(self):
        print("Sports Car:", self.brand)
        print("Seats:", self.seats)
        print("Top Speed:", self.top_speed)


class ElectricBike10(Bike10):
    def __init__(self, brand, engine, battery):
        super().__init__(brand, engine)
        self.battery = battery

    def display(self):
        print("Electric Bike:", self.brand)
        print("Battery:", self.battery)


sc10 = SportsCar10("BMW", 2, 300)
eb10 = ElectricBike10("Ola", "Electric", "5 kWh")

sc10.display()
eb10.display()


# ============================================================
# 11. STUDENT -> RESULT
# ============================================================

class Student11:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course


class Result11(Student11):
    def __init__(self, roll_no, name, course, m1, m2, m3):
        super().__init__(roll_no, name, course)
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def display_result(self):
        total = self.m1 + self.m2 + self.m3
        percentage = total / 3

        if percentage >= 75:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        else:
            grade = "D"

        print("Name:", self.name)
        print("Total:", total)
        print("Percentage:", percentage)
        print("Grade:", grade)


result11 = Result11(
    101, "Rahul", "BCA", 80, 75, 90
)
result11.display_result()


# ============================================================
# 12. PRODUCT -> ELECTRONIC PRODUCT
# ============================================================

class Product12:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class ElectronicProduct12(Product12):
    def __init__(
        self, product_id, name, price, brand, warranty
    ):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty = warranty

    def final_price(self, discount):
        return self.price - (self.price * discount / 100)

    def display(self):
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Brand:", self.brand)
        print("Warranty:", self.warranty, "years")
        print("Final Price:", self.final_price(10))


ep12 = ElectronicProduct12(
    101, "Laptop", 60000, "Dell", 2
)
ep12.display()


# ============================================================
# 13. PRINTER + SCANNER -> MULTIFUNCTION DEVICE
# ============================================================

class Printer13:
    def print_document(self):
        print("Printing document...")


class Scanner13:
    def scan_document(self):
        print("Scanning document...")


class MultifunctionDevice13(Printer13, Scanner13):
    def copy_document(self):
        print("Copying document...")


device13 = MultifunctionDevice13()
device13.print_document()
device13.scan_document()
device13.copy_document()


# ============================================================
# 14. CAMERA + PHONE -> SMARTPHONE
# ============================================================

class Camera14:
    def take_photo(self):
        print("Photo taken")


class Phone14:
    def make_call(self, number):
        print("Calling", number)


class Smartphone14(Camera14, Phone14):
    def browse(self):
        print("Browsing Internet")


phone14 = Smartphone14()
phone14.take_photo()
phone14.make_call("9876543210")
phone14.browse()


# ============================================================
# 15. ANIMAL -> DOG, CAT, COW
# ============================================================

class Animal15:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")


class Dog15(Animal15):
    def sound(self):
        print("Dog barks")


class Cat15(Animal15):
    def sound(self):
        print("Cat meows")


class Cow15(Animal15):
    def sound(self):
        print("Cow moos")


dog15 = Dog15("Tommy")
cat15 = Cat15("Kitty")
cow15 = Cow15("Gauri")

dog15.eat()
dog15.sound()

cat15.eat()
cat15.sound()

cow15.eat()
cow15.sound()


# ============================================================
# 16. PERSON -> DOCTOR, PATIENT
#     SURGEON AND MEDICAL RESEARCHER
# ============================================================

class Person16:
    def __init__(self, name):
        self.name = name


class Doctor16(Person16):
    def doctor_info(self):
        print("Doctor:", self.name)


class Patient16(Person16):
    def patient_info(self):
        print("Patient:", self.name)


class Surgeon16(Doctor16, Patient16):
    def surgery(self):
        print(self.name, "performs surgery")


class MedicalResearcher16(Doctor16, Patient16):
    def research(self):
        print(self.name, "conducts medical research")


surgeon16 = Surgeon16("Dr. Amit")
surgeon16.doctor_info()
surgeon16.surgery()

researcher16 = MedicalResearcher16("Dr. Priya")
researcher16.doctor_info()
researcher16.research()


# ============================================================
#                     POLYMORPHISM
# ============================================================


# ============================================================
# 17. SHAPE POLYMORPHISM
# ============================================================

class Shape17:
    def area(self):
        pass


class Circle17(Shape17):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle17(Shape17):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle17(Shape17):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes17 = [
    Circle17(5),
    Rectangle17(10, 4),
    Triangle17(8, 6)
]

for shape in shapes17:
    print("Area:", shape.area())


# ============================================================
# 18. EMPLOYEE SALARY POLYMORPHISM
# ============================================================

class Employee18:
    def calculate_salary(self):
        pass


class Manager18(Employee18):
    def calculate_salary(self):
        return 50000 + 15000


class Developer18(Employee18):
    def calculate_salary(self):
        return 50000 + 10000


class Tester18(Employee18):
    def calculate_salary(self):
        return 50000 + 7500


employees18 = [
    Manager18(),
    Developer18(),
    Tester18()
]

for employee in employees18:
    print("Salary:", employee.calculate_salary())


# ============================================================
# 19. VEHICLE START POLYMORPHISM
# ============================================================

class Vehicle19:
    def start(self):
        pass


class Car19(Vehicle19):
    def start(self):
        print("Car starts with a key")


class Bike19(Vehicle19):
    def start(self):
        print("Bike starts with self-start button")


class Bus19(Vehicle19):
    def start(self):
        print("Bus starts with a heavy engine")


vehicles19 = [Car19(), Bike19(), Bus19()]

for vehicle in vehicles19:
    vehicle.start()


# ============================================================
# 20. ANIMAL SOUND POLYMORPHISM
# ============================================================

class Animal20:
    def sound(self):
        pass


class Dog20(Animal20):
    def sound(self):
        print("Dog: Bark")


class Cat20(Animal20):
    def sound(self):
        print("Cat: Meow")


class Cow20(Animal20):
    def sound(self):
        print("Cow: Moo")


class Lion20(Animal20):
    def sound(self):
        print("Lion: Roar")


animals20 = [
    Dog20(),
    Cat20(),
    Cow20(),
    Lion20()
]

for animal in animals20:
    animal.sound()


# ============================================================
# 21. NOTIFICATION POLYMORPHISM
# ============================================================

class Notification21:
    def send(self):
        pass


class EmailNotification21(Notification21):
    def send(self):
        print("Sending Email")


class SMSNotification21(Notification21):
    def send(self):
        print("Sending SMS")


class PushNotification21(Notification21):
    def send(self):
        print("Sending Push Notification")


notifications21 = [
    EmailNotification21(),
    SMSNotification21(),
    PushNotification21()
]

for notification in notifications21:
    notification.send()


# ============================================================
# 22. STUDENT GRADE POLYMORPHISM
# ============================================================

class Student22:
    def calculate_grade(self, marks):
        pass


class EngineeringStudent22(Student22):
    def calculate_grade(self, marks):
        if marks >= 80:
            return "A"
        elif marks >= 60:
            return "B"
        else:
            return "C"


class MedicalStudent22(Student22):
    def calculate_grade(self, marks):
        if marks >= 85:
            return "Distinction"
        elif marks >= 70:
            return "First Class"
        else:
            return "Pass"


class ManagementStudent22(Student22):
    def calculate_grade(self, marks):
        if marks >= 75:
            return "A"
        elif marks >= 60:
            return "B"
        else:
            return "C"


students22 = [
    EngineeringStudent22(),
    MedicalStudent22(),
    ManagementStudent22()
]

for student in students22:
    print(student.calculate_grade(80))


# ============================================================
# 23. BANK ACCOUNT POLYMORPHISM
# ============================================================

class BankAccount23:
    def calculate_interest(self, balance):
        pass


class SavingsAccount23(BankAccount23):
    def calculate_interest(self, balance):
        return balance * 0.06


class CurrentAccount23(BankAccount23):
    def calculate_interest(self, balance):
        return balance * 0.03


class FixedDepositAccount23(BankAccount23):
    def calculate_interest(self, balance):
        return balance * 0.08


accounts23 = [
    SavingsAccount23(),
    CurrentAccount23(),
    FixedDepositAccount23()
]

for account in accounts23:
    print("Interest:", account.calculate_interest(100000))


# ============================================================
# 24. REPORT POLYMORPHISM
# ============================================================

class Report24:
    def generate(self):
        pass


class PDFReport24(Report24):
    def generate(self):
        print("Generating PDF Report")


class ExcelReport24(Report24):
    def generate(self):
        print("Generating Excel Report")


class HTMLReport24(Report24):
    def generate(self):
        print("Generating HTML Report")


def generate_report24(report):
    report.generate()


generate_report24(PDFReport24())
generate_report24(ExcelReport24())
generate_report24(HTMLReport24())


# ============================================================
# 25. DISTANCE OPERATOR OVERLOADING (+)
# ============================================================

class Distance25:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        inches = self.inches + other.inches
        feet = self.feet + other.feet

        if inches >= 12:
            feet += inches // 12
            inches = inches % 12

        return Distance25(feet, inches)

    def display(self):
        print(self.feet, "feet", self.inches, "inches")


d1_25 = Distance25(5, 8)
d2_25 = Distance25(4, 7)

d3_25 = d1_25 + d2_25
d3_25.display()


# ============================================================
# 26. STUDENT OPERATOR OVERLOADING (>, <)
# ============================================================

class Student26:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __lt__(self, other):
        return self.marks < other.marks


student1_26 = Student26("Rahul", 85)
student2_26 = Student26("Amit", 75)

print("Rahul > Amit:", student1_26 > student2_26)
print("Rahul < Amit:", student1_26 < student2_26)


# ============================================================
# 27. PRODUCT OPERATOR OVERLOADING (==, >)
# ============================================================

class Product27:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price


product1_27 = Product27("Laptop", 60000)
product2_27 = Product27("Mobile", 60000)

print("Prices equal:", product1_27 == product2_27)
print("Laptop more expensive:", product1_27 > product2_27)


# ============================================================
# 28. ONLINE SHOPPING PAYMENT POLYMORPHISM
# ============================================================

class Payment28:
    def make_payment(self, amount):
        pass


class UPIPayment28(Payment28):
    def make_payment(self, amount):
        print("Paid", amount, "using UPI")


class CardPayment28(Payment28):
    def make_payment(self, amount):
        print("Paid", amount, "using Card")


class WalletPayment28(Payment28):
    def make_payment(self, amount):
        print("Paid", amount, "using Wallet")


def process_payment28(payment, amount):
    payment.make_payment(amount)


process_payment28(UPIPayment28(), 1000)
process_payment28(CardPayment28(), 2000)
process_payment28(WalletPayment28(), 500)


# ============================================================
# 29. PERSON -> STUDENT, FACULTY, ADMINISTRATOR
# ============================================================

class Person29:
    def display_role(self):
        pass


class Student29(Person29):
    def display_role(self):
        print("Role: Student")


class Faculty29(Person29):
    def display_role(self):
        print("Role: Faculty")


class Administrator29(Person29):
    def display_role(self):
        print("Role: Administrator")


people29 = [
    Student29(),
    Faculty29(),
    Administrator29()
]

for person in people29:
    person.display_role()


# ============================================================
# 30. MEDIA POLYMORPHISM
# ============================================================

class Media30:
    def play(self):
        pass


class Audio30(Media30):
    def play(self):
        print("Playing Audio")


class Video30(Media30):
    def play(self):
        print("Playing Video")


class Podcast30(Media30):
    def play(self):
        print("Playing Podcast")


media30 = [
    Audio30(),
    Video30(),
    Podcast30()
]

for item in media30:
    item.play()


# ============================================================
# 31. SMART DEVICE POLYMORPHISM
# ============================================================

class SmartDevice31:
    def turn_on(self):
        pass

    def turn_off(self):
        pass


class Light31(SmartDevice31):
    def turn_on(self):
        print("Light turned ON")

    def turn_off(self):
        print("Light turned OFF")


class Fan31(SmartDevice31):
    def turn_on(self):
        print("Fan turned ON")

    def turn_off(self):
        print("Fan turned OFF")


class AC31(SmartDevice31):
    def turn_on(self):
        print("AC turned ON")

    def turn_off(self):
        print("AC turned OFF")


class TV31(SmartDevice31):
    def turn_on(self):
        print("TV turned ON")

    def turn_off(self):
        print("TV turned OFF")


devices31 = [
    Light31(),
    Fan31(),
    AC31(),
    TV31()
]

for device in devices31:
    device.turn_on()
    device.turn_off()


# ============================================================
#                     ABSTRACTION
# ============================================================

from abc import ABC, abstractmethod


# ============================================================
# 32. ABSTRACT SHAPE
# ============================================================

class Shape32(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle32(Shape32):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle32(Shape32):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle32(Shape32):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes32 = [
    Circle32(5),
    Rectangle32(10, 5),
    Triangle32(8, 6)
]

for shape in shapes32:
    print("Area:", shape.area())


# ============================================================
# 33. ABSTRACT VEHICLE
# ============================================================

class Vehicle33(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car33(Vehicle33):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")


class Bike33(Vehicle33):
    def start(self):
        print("Bike started")

    def stop(self):
        print("Bike stopped")


class Bus33(Vehicle33):
    def start(self):
        print("Bus started")

    def stop(self):
        print("Bus stopped")


vehicles33 = [
    Car33(),
    Bike33(),
    Bus33()
]

for vehicle in vehicles33:
    vehicle.start()
    vehicle.stop()


# ============================================================
# 34. ABSTRACT BANK ACCOUNT
# ============================================================

class BankAccount34(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount34(BankAccount34):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")


class CurrentAccount34(BankAccount34):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        self.balance -= amount
        print("Withdrawn:", amount)


account34 = SavingsAccount34(10000)

account34.deposit(2000)
account34.withdraw(3000)

print("Balance:", account34.balance)


# ============================================================
# 35. ABSTRACT FOOD ORDER
# ============================================================

class FoodOrder35(ABC):

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass


class RestaurantOrder35(FoodOrder35):
    def calculate_bill(self):
        return 500

    def delivery_charge(self):
        return 0


class HomeDeliveryOrder35(FoodOrder35):
    def calculate_bill(self):
        return 500

    def delivery_charge(self):
        return 50


orders35 = [
    RestaurantOrder35(),
    HomeDeliveryOrder35()
]

for order in orders35:
    total = (
        order.calculate_bill()
        + order.delivery_charge()
    )
    print("Total Bill:", total)


# ============================================================
# 36. ABSTRACT PATIENT
# ============================================================

class Patient36(ABC):

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def treatment(self):
        pass


class InPatient36(Patient36):
    def calculate_bill(self):
        return 10000

    def treatment(self):
        print("In-patient treatment")


class OutPatient36(Patient36):
    def calculate_bill(self):
        return 2000

    def treatment(self):
        print("Out-patient treatment")


class EmergencyPatient36(Patient36):
    def calculate_bill(self):
        return 20000

    def treatment(self):
        print("Emergency treatment")


patients36 = [
    InPatient36(),
    OutPatient36(),
    EmergencyPatient36()
]

for patient in patients36:
    patient.treatment()
    print("Bill:", patient.calculate_bill())


# ============================================================
# 37. ABSTRACT TRANSPORT
# ============================================================

class Transport37(ABC):

    @abstractmethod
    def calculate_fare(self, distance):
        pass


class Bus37(Transport37):
    def calculate_fare(self, distance):
        return distance * 2


class Train37(Transport37):
    def calculate_fare(self, distance):
        return distance * 1.5


class Taxi37(Transport37):
    def calculate_fare(self, distance):
        return distance * 10


class Flight37(Transport37):
    def calculate_fare(self, distance):
        return distance * 15


transports37 = [
    Bus37(),
    Train37(),
    Taxi37(),
    Flight37()
]

for transport in transports37:
    print(
        "Fare for 100 km:",
        transport.calculate_fare(100)
    )


# ============================================================
# 38. ABSTRACT QUESTION
# ============================================================

class Question38(ABC):

    @abstractmethod
    def evaluate_answer(self, answer):
        pass


class MCQQuestion38(Question38):
    def evaluate_answer(self, answer):
        if answer == "B":
            print("Correct MCQ answer")
        else:
            print("Wrong MCQ answer")


class TrueFalseQuestion38(Question38):
    def evaluate_answer(self, answer):
        if answer == "True":
            print("Correct True/False answer")
        else:
            print("Wrong True/False answer")


class DescriptiveQuestion38(Question38):
    def evaluate_answer(self, answer):
        if len(answer) > 20:
            print("Descriptive answer accepted")
        else:
            print("Answer needs more explanation")


mcq38 = MCQQuestion38()
tf38 = TrueFalseQuestion38()
desc38 = DescriptiveQuestion38()

mcq38.evaluate_answer("B")
tf38.evaluate_answer("True")
desc38.evaluate_answer(
    "Python supports object oriented programming"
)


# ============================================================
# 39. ABSTRACT AUTHENTICATION
# ============================================================

class Authentication39(ABC):

    @abstractmethod
    def authenticate(self):
        pass


class PasswordAuthentication39(Authentication39):
    def authenticate(self):
        print("Authenticated using Password")


class OTPAuthentication39(Authentication39):
    def authenticate(self):
        print("Authenticated using OTP")


class BiometricAuthentication39(Authentication39):
    def authenticate(self):
        print("Authenticated using Biometric")


authentication_methods39 = [
    PasswordAuthentication39(),
    OTPAuthentication39(),
    BiometricAuthentication39()
]

for method in authentication_methods39:
    method.authenticate()


# ============================================================
# 40. ABSTRACT CLOUD STORAGE
# ============================================================

class CloudStorage40(ABC):

    @abstractmethod
    def upload_file(self, filename):
        pass

    @abstractmethod
    def download_file(self, filename):
        pass

    @abstractmethod
    def delete_file(self, filename):
        pass


class GoogleDrive40(CloudStorage40):
    def upload_file(self, filename):
        print(filename, "uploaded to Google Drive")

    def download_file(self, filename):
        print(filename, "downloaded from Google Drive")

    def delete_file(self, filename):
        print(filename, "deleted from Google Drive")


class Dropbox40(CloudStorage40):
    def upload_file(self, filename):
        print(filename, "uploaded to Dropbox")

    def download_file(self, filename):
        print(filename, "downloaded from Dropbox")

    def delete_file(self, filename):
        print(filename, "deleted from Dropbox")


storage40 = GoogleDrive40()

storage40.upload_file("notes.pdf")
storage40.download_file("notes.pdf")
storage40.delete_file("notes.pdf")

storage40 = Dropbox40()

storage40.upload_file("photo.jpg")
storage40.download_file("photo.jpg")
storage40.delete_file("photo.jpg")


# ============================================================
# 41. ABSTRACT APPOINTMENT
# ============================================================

class Appointment41(ABC):

    @abstractmethod
    def book_appointment(self):
        pass

    @abstractmethod
    def calculate_fee(self):
        pass


class GeneralAppointment41(Appointment41):
    def book_appointment(self):
        print("General appointment booked")

    def calculate_fee(self):
        return 500


class SpecialistAppointment41(Appointment41):
    def book_appointment(self):
        print("Specialist appointment booked")

    def calculate_fee(self):
        return 1000


class EmergencyAppointment41(Appointment41):
    def book_appointment(self):
        print("Emergency appointment booked")

    def calculate_fee(self):
        return 2000


appointments41 = [
    GeneralAppointment41(),
    SpecialistAppointment41(),
    EmergencyAppointment41()
]

for appointment in appointments41:
    appointment.book_appointment()
    print("Fee:", appointment.calculate_fee())