"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 4
---------------------------------------------------------------------------------
- File Name: lab4.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Implement the ContactManager class and perform CRUD operations.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# 1. Import the ContactManager class here.
from contact_manager import ContactManager

# 2. Go to the 'contact_manager.py' file and implement the TODO in the display_contacts method.
# i did it
# 3. Create two contacts using the ContactManager.
def main():
    CM = ContactManager()
    print("---Contact List---")
    print()
    
    CM.add_contact("Charles", "CharlesSmith@gmail.com", "+1 412 788 645")
    CM.add_contact("Lenny", "LennySummers@icloud.com", "+1 423 948 362")
    CM.add_contact("Micah", "MicahBell@bigpond.com", "+1 4382 739 921")
    print()
    print("Current Contact List")
    # 4. Display all contacts.
    CM.display_contacts()
    # 5. Update the email address of one contact.
    CM.update_contact("Charles", new_email= "CharlesSmith@icloud.com")
    print()
    # 6. Remove one of the contacts.
    CM.remove_contact("Lenny")
    print()
    # 7. Display all contacts again.
    print("Updated Contact List:")
    CM.display_contacts()
if __name__ == "__main__":
    main()

