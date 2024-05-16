"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 3
---------------------------------------------------------------------------------
- File Name: lab3.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Enhance the Contact class by adding instance and class methods.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# 1. Copy/paste your Contact class from Lab 2.            
# 2. Add a check_email method to check if the email contains an '@'
# 3. Create a class method get_contact_count to retrieve the number of contacts
# 4. Reproduce the instances of the Contact class that you created in Lab 2
# 5. Call your new instance method on one Contact and print the result
# 6. Use the class method to print out the total number of contacts

class Contact:
    total_contacts = 0
    
    def __init__(self, name, phone_number, email):
            self.name = name
            self.phone_number = phone_number
            self.email = email
            Contact.total_contacts += 1
    
    def check_email(self):
     if "@" in self.email:
         print(f"{self.email} is valid")
     else:
         print(f"{self.email} is invalid, no '@' detected!")
         
    @classmethod
    def get_contact_count(cls):
        return cls.total_contacts
    
    def __str__(self):
        return (f"Employee: {self.name}\n" + 
            f"Email: {self.email}\n" + 
            f"Phone Number: {self.phone_number}\n" + 
            "-" * 40)
            
Foghorn = Contact("Foghorn Leghorn", "+1 394 392 891", "foghorn30@gmail.com")
Bugs = Contact("Bugs Bunny", "+1 342 452 478", "bugs30@icloud.com") 

Foghorn.check_email()
Bugs.check_email()

print(f"The total number of contacts is {Contact.get_contact_count()}")
print()
print()
