phone_contacts = {
    "Amal": "1111111111",
    "Mohammed": "2222222222",
    "Khadijah": "3333333333",
    "Abdullah": "4444444444",
    "Rawan": "5555555555",
    "Faisal": "6666666666",
    "Layla": "7777777777"
}

def search_by_num(search_number):
    if not search_number.isdigit() or len(search_number) != 10:
        return "The length of number should be 10 and digits"
    
    for name,phone in phone_contacts.items():
        if phone == search_number:
            return name 

            
    return "Sorry, the number is not found"

def search_by_name(search_name):
    for name, phone in phone_contacts.items():
        if search_name == name:
            return phone

    return "The name id not found"
        
def add_contact(New_name , New_phone):
    if  not New_phone.isdigit() or (len(New_phone) != 10):
        return "The length of number should be 10"
    
    phone_contacts[New_name] = New_phone
    return f"Contact {New_name} with number {New_phone} was added."

while True:
    print("----------------")
    print("Phone Directory")
    print("1. Search by number")
    print("2. Search by name")
    print("3. Add new contact")
    print("4. Exit")
    print("----------------")

    choice = input("Enter your choice: ")

    if choice == "1":
        search_number = input("Enter the phone number: ")
        result = search_by_num(search_number)
        print(result)
    
    elif choice == "2":
        search_name = input("Enter the name: ")
        result = search_by_name(search_name)
        print(result)
    
    elif choice == "3":
        New_name = input("Enter the name: ")
        New_phone =  input("Enter the phone number: ")
        result = add_contact(New_name, New_phone)
        print(result)
    
    elif choice == "4":
        break
    
    else:
        print("Invalid choice. Please try again.")
