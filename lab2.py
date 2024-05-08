"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 2
---------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create a class for a contact in a contact management system.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Create a class named Contact that represents a contact in a contact management system. 
# This class should have an initialiser with attributes for name, phone_number, and email.
# Add a class attribute to keep track of the total number of contacts.

class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email


# Create at least two instances of the Contact class with different data.

Foghorn = Contact("Foghorn Leghorn", "+1 394 392 891", "foghorn30@gmail.com")
Bugs = Contact("Bugs Bunny", "+1 342 452 478", "bugs30@icloud.com")

# Write code that prints out the details of each contact you have created.

print(f"{Foghorn.name}'s phone number is {Foghorn.phone_number} and email is {Foghorn.email}")
print(f"{Bugs.name}'s number is {Bugs.phone_number} and email is {Bugs.email}")

