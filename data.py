1.
student = {'ram' : 'ram12@gmail.com','sita' : 'sita34@gmail.com','rita' : 'rita98@gmail.com'}
name = input("Enter your name: ")
if name in student:
    print(student[name])
else:
    print("Contact not found")

2.
shopping_list = {"Milk", "Bread", "Eggs"}
bought = {"Bread", "Eggs"}
a = shopping_list.difference(bought)
print(a)

3.
class_list = ["ram","sita","laxman"]
new = input("Enter your name: ")
if new not in class_list:
    class_list.append(new)
    print("Student added successfully.")
else:
    print("Already exists.")

4.
votes = ["Blue", "Red", "Blue", "Green", "Blue"]
count = votes.count('Blue')
if count >= 3:
    print("Blue wins")
else:
    print("Blue did not win")

5.
grades = {"Ram": 92, "Sita": 88}
student = input("Enter student name: ")
if student in grades.keys():
    print("Grade:",grades[student])
else:
    print("Grade not available.")

6.
applicant = { "name": "Priya", "skills": ["Java", "SQL"], "experience_years": 1}
required_skills = {"Python", "Java"}
required = list(required_skills)
common_skills = required_skills.intersection(applicant["skills"])
if common_skills and applicant["experience_years"] >= 2:
    print("Priya qualifies")
else:
    print("Priya does not qualify")
 
7.
banned_items = {"scissors", "knife", "lighter"}
weight = int(input("Enter the baggage's weight in kg: "))
items = input("What are the items in the baggage: ").lower()
if weight <= 7 and items not in banned_items:
    print("Bag allowed")
else:
    print("Bag not allowed")

8.
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Shyam', 'salary': 500}
}
sample_dict['emp3']['salary']=8500
print(sample_dict)

9.
ram = {'pen','black','mango'}
laxman = {'pencil','white','mango'}
a = ram.isdisjoint(laxman)
if a:
    print("They picked completely different items.")
else:
    print("There have some common items.")

10.
mylist = [10,20,30]
mytuple = (10,20,30)
myset = {10,20,30}
mydict = {'a':10,'b':20,'c':30}
val = 20
if val in mylist and mytuple:
    if 'b' in mydict and val not in myset:
        print("Path A")
    else:
        print("Path B")
else:
    print("Path C")

11. The value for a becomes 30.

12. [1,2,3]

13. Not Found

14. 2

15. my_set.add(40)

16.
menu = {'Pizza': 15, 'Burger': 10, 'Salad': 8}
order = 'Pizza'
if menu.get(order):
    print(menu[order])
else:
    print("Item not found.")

17. 
student_data = {"name": "Sam", "score": 85}
if student_data['score'] >= 80:
    student_data.update({'status': 'Pass'})
    print(student_data)
else:
    student_data.update({'status': 'Review'})
    print(student_data)

18.
database = {"admin": "1234", "user": "abcd"}
user_input = 'admin'
user_pass = '1234'
if user_input in database:
    if database[user_input] == user_pass:
        print('Login successful')
    else:
        print('Login Failed')
else:
    print('Invalid input')

19.
emails =['ram123@gmail.com', 'hari77@gmail.com']
blacklisted_emails = {'hari77@gmail.com'}
current_email = 'hari77@gmail.com'
if current_email in emails and current_email not in blacklisted_emails:
    print("Email Sent")
else:
    print("Blocked")

20.
inventory = {'A1': 50, 'B2': 0, 'C3': 10}
restricted_zones = {'B2', 'Z9'}
target = 'B2'
if target in inventory:
    if target not in restricted_zones and inventory[target] > 0:
        print("Dispatch item")
    else:
        print("Stock error")
else:
    print("Invalid zone")

21.
valid_courses = {'python', 'robotics', 'java'}
hs_grades = [9, 10, 11, 12]
name = input("Enter your name: ")
course = input("Enter your course: ").lower()
grade = int(input("Enter your grade: "))
student_records = {
    'name': name,
    'course': course,
    'grade': grade
}
if course not in valid_courses:
    print(f"{name} selected an invalid course.")
else:
    if grade < 9:
        print(f"{name} is not eligible for {course} grade too low")
    elif grade > 12:
        print(f"{name} is not eligible for {course} grade too high")
    else:
        if course == "robotics" and grade == 9:
            print(f"{name} is not eligible for {course}")
        else:
            print(f"{name} is approved for {course}")
