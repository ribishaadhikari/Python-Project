4.
username = input("Enter your username: ")
pw = input("Enter your password: ")
if username == 'admin' and pw == 'ad123':
    print("Access Granted:Faculty Dashboard")
elif username == 'student' and pw == 'st2026':
    print("Access Granted:Notes and Practice Questions")
else:
    print("Invalid Credentials.Please try again")


5.
total = float(input("Enter the total purchase amount: "))
if total > 5000:
    membership = input("Do you have the membership card (yes/no): ")
    if membership == 'yes':
        discount= total * 0.30
        final_price = total - discount
        print(f'Total saved: Rs.{discount}')
        print(f'Final amount: Rs.{final_price}')
    else:
        print(f'Total amount:{total}\n Discount=0')
else:
    print(f'Total:Rs.{total}')


6.
print("Welcome to the Magic Forest!")
direction = input("Go north or south: ")
if direction == 'north':
    print('GAME OVER')
else:
    stage_2=input('1.Cross the river\n2.Follow the path\nChoose 1 or 2:')
    if stage_2 == '1':
        print("GAME OVER")
    else:
        stage_3 = input('Choose:\nfairy\nogre\nelf\t')
        if stage_3 == 'elf':
            print('CONGRATULATIONS! YOU WON!!')
        else:
            print('GAME OVER')

7.
color = input("Enter the color:")
if color == 'red':
    print("STOP")
elif color =='yellow':
    print("WAIT")
elif color == 'green':
    print("GO")
else:
    print("Invalid color")

8.
num=int(input("Enter a number: "))
match number:
    case 1: 
        print("Spring")
    case 2:
        print("Summer")
    case 3:
        print("Autumn") 
    case 4:
        print("Winter")
    case _:
        print("Unknown")

9.
age = int(input("Enter your age: "))
income = float(input("Enter your monthly salary: "))
cscore = int(input("Enter your credit score: "))
is_valid = True 
if age < 21:
    print("Invalid age")
    is_valid = False
elif income < 30000:
    print("Insufficient salary")
    is_valid = False
elif cscore < 700:
    print("Insufficient credit score.")
    is_valid = False
if is_valid:
    print("Bank loan approved")
else:
    print("Failed. Please try again.")


10.
weight = int(input("Enter your weight: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height * height)
if bmi<18.5:
    status=("Underweight")
elif 18.5 <= bmi <= 25:
    status=("Normal weight")
elif 25 <= bmi <= 30:
    status=("Overweight")
else:
    status=("Obese")
print(f'Weight:{weight}')
print(f'Height:{height}')
print(f'BMI:{bmi} {status}')

11.
age = int(input("Enter your age: "))
membership = input("Do you have the membership card? ")
if age < 12:
    print("Ticket is free!")
elif 12 <= age < 60 and membership == 'yes':
    print("Cost: Rs.150")
elif 12 <= age < 60 and membership == 'no':
    print("Cost: Rs.200")
else:
    print("Cost: Rs.100")

12.
salary = int(input("Enter your salary: "))
year = int(input("Enter the year of service you have provided: "))
if year > 5:
    bonus = 5/100 * salary 
    print(f'Bonus amount :Rs.{bonus}')
else:
    print("Insufficient year of service.")

13.
radius = float(input("Enter the radius of circle:"))
area = 3.14 * radius ** 2
print(f'Area of the circle {area}cm^2')

14.
age = int(input("Enter your age: ")) 
gender = input("Enter your gender(M/F): ") 
days = int(input("Enter the number of days: ")) 
if 18 <= age < 30: 
    if gender == 'M': 
        wages = 700 * days 
    else: 
        wages = 750 * days 
elif 30 <= age <= 40: 
    if gender == 'M': 
        wages = 800 * days 
    else: 
        wages = 850 * days 
print(f"Wages for {days} days is Rs.{wages}") 

15.
num = int(input("Enter the number: ")) 
if num % 3 ==0 and num % 5 ==0: 
    print("Fizz Buzz") 
elif num % 3 == 0 and num % 5 !=0: 
    print("Fizz") 
elif num % 5 ==0 and num % 3!=0: 
    print("Buzz") 
else: 
    print(f'{num}')

16.
units = int(input("Enter your electricity units: "))
if units < 100:
    cost = 5 * units
elif 100 <= units <= 300:
    cost = (100 * 5) + ((units - 100)*8)
else:
    cost = (100 * 5) + (200 * 8) + ((units - 300) * 10)
print(f'Electricity charges:Rs.{cost}')

17.
p1 = input("Enter your move (rock,paper,scissor):")
p2 = input("Enter your move (rock,paper,scissor):")
if p1 == p2:
    print("It's a tie.")
elif p1 =='rock'and p2 == 'scissor':
    print("Players one wins")
elif p1 == 'paper' and p2 == 'rock':
    print("Players two wins")
elif p1 =='scissor' and p2 =='paper':
    print("Players one wins")
else:
    print("Players two wins")

18.
num = int(input("Enter a number: "))
if num > 0:
    if num % 2 == 0:
        print("The number is positive even number.")
    else:
        print("The number is positive odd number.")
else:
    print("The number is negative number.")

19.
total = float(input("Enter the total purchase amount: "))
if total > 1000:
    membership = input("Do you have the membership card (yes/no): ")
    if membership == 'yes':
        discount = total * 0.20
    else:
        discount = total * 0.10

    final_price = total - discount
    print(f'Total saved: Rs.{discount}')
    print(f'Final amount: Rs.{final_price}')
else:
    print(f'Total:Rs.{total}')

20.
weight = float(input("Enter your weight in Earth: "))
planet = int(input("1. Mercury  2. Venus  3. Mars 4. Jupiter  5. Saturn  6. Uranus  7. Neptune\nEnter the destination planet(1-7): "))
if planet == 1:
    new = weight * 0.38
    print(f'Your weight on Mercury is {new}kg')
elif planet == 2:
    new = weight * 0.91
    print(f'Your weight on  Venus is {new}kg')
elif planet == 3:
    new = weight * 0.38
    print(f'Your weight on Mars is {new}kg')
elif planet == 4:
    new = weight * 2.53
    print(f'Your weight on Jupiter is {new}kg')
elif planet == 5:
    new = weight * 1.07
    print(f'Your weight on Saturn is {new}kg')
elif planet == 6:
    new = weight * 0.89
    print(f'Your weight on Uranus is {new}kg')
elif planet == 7:
    new = weight * 1.14
    print(f'Your weight on Neptune is {new}kg')
else:
    print("Invalid planet number.")

21.
m1 = int(input("Enter the marks of first subject:"))
m2 = int(input("Enter the marks of second subject:"))
m3 = int(input("Enter the marks of third subject:"))
m4 = int(input("Enter the marks of forth subject:"))
total_marks = m1 + m2 + m3 + m4
percentage = (total_marks/400) * 100
if percentage > 70:
    grade = 'Distinction'
elif percentage > 60:
    grade = 'First'
elif percentage > 40:
    grade = 'Pass'
else:
    grade = 'Fail'
print(f'Total marks:{total_marks}')
print(f'Percentage:{percentage}%')
print(f'Grade obtained:{grade}')

22.
is_valid = True
balance = 5000
correct_pin = 123
print("Welcome to Global Bank ATM")
if is_valid:
    user_pin = int(input("Enter your PIN: "))
    if user_pin == correct_pin:
        print("1. Withdraw")
        print("2. Check Balance")
        print("3. Exit")
        choice = int(input("Enter your choice (1-3): "))
        if choice == 1:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"Please collect your cash: Rs.{amount}")
                print(f"Remaining balance: Rs.{balance}")
            else:
                print("Insufficient balance")
        elif choice == 2:
            print(f"Your current balance is Rs.{balance}")
        elif choice == 3:
            print("Thank you for visiting")
        else:
            print("Invalid option")
    else:
        print("Wrong PIN")
else:
    print("Invalid card")

23.
floor = int(input("Press a floor number:(0-10) "))
if floor>10 and floor<=0:
    print("Invalid floor.")
else:
    weight = int(input("Enter the total weight in kg: "))
    if weight > 500:
        print("Overweight.Lift cannot move.")
    else:
        door = input("Is door closed? ")
        if door == 'no':
            print("Warning! Close the door.")
        else:
            print(f"Activate elevator motion")  
              
24.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
email = input("Enter you email address: ")
reemail = input("Re-enter the email address: ")
pw = input("Enter your password: ")

if not (first_name and last_name and email and reemail and pw):
    print('All fields are mandatory.')
elif not (first_name.isalpha() and last_name.isalpha()):
    print('Must enter or type letters only.')
elif not ('@' in email and '.' in email and '@' in reemail and '.' in reemail):
    print('Invalid email address.')
elif not email!=reemail:
    print('Emails do not match.')
elif len(pw)<6:
    print('Password must be longer than 6 characters.')
else:
    print('Registered successfully.')




