from datetime import datetime

def date_validation(date_text):
    try:
        return datetime.strptime(date_text, "%d.%m.%Y")
    except ValueError:
        return None

def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def get_day_of_week(birth_date):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return days[birth_date.weekday() + 1]


people = []

while True:
    Enter = input("Enter name and birth date (dd-mm-yyyy), or 'done' to finish: ")
    if Enter.lower() == 'done':
        break
    
    parts = Enter.split(", ")
    if len(parts) != 2:
        print("Invalid input format. Please use 'Name, ddm.m.yyyy'.")
        continue
    
    name, birth_date_str = parts
    birth_date = date_validation(birth_date_str)
    if not birth_date:
        print(f"Invalid date for {name}.")
        continue
    
    people.append((name, birth_date))

if not people:
    print("No people were entered.")
else:
    for name, birth in people:
        age = calculate_age(birth)
        day_of_week = get_day_of_week(birth)
        print(f"{name} is {age} years old and was born on {day_of_week}")

    oldest_person = min(people, key=lambda x: x[1])
    youngest_person = max(people, key=lambda x: x[1])
    print(f"The oldest one is {oldest_person[0]}")
    print(f"The youngest one is {youngest_person[0]}")
    print(f"Total People: {len(people)}")
