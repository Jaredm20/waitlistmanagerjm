# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    def __init__(self, name):
        self.name = name
        self.next = None
    



# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    def __init__(self):
        self.head = None

    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, name):
        new_node = Node(name)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove(self, name):
        current = self.head
        previous = None
        while current:
            if current.name == name:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True
            previous = current
            current = current.next
        return False

    def print_list(self):
        current = self.head
        if not current:
            print("Waitlist is empty.")
            return
        while current:
            print(current.name, end=" -> " if current.next else "")
            current = current.next
        print()
    


def waitlist_generator():
    # Create a new linked list instance
    
    waitlist = LinkedList()
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            waitlist.add_front(name)
            print(f"{name} added to the front")
            # Call the add_front method
            

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            waitlist.add_end(name)
            print(f"{name} added to the end.")

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            if waitlist.remove(name):
                print(f"{name} removed from waitlist.")
            else:
                print(f"{name} not found in waitlist.")
            
        elif choice == "4":
            print("Current waitlist:")
            waitlist.print_list()

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program
waitlist_generator()

'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?
- What role does the head play?
- When might a real engineer need a custom list like this?

My list works by storing each inserted customer as a node. The program works by referencing the position of the head (first item in list essentially) and then going down the list from there. When it comes to adding or subtracting a name from the list, the sequence references the head node and moves from there.
The head is what allows for all the functions in the menu to work, the functions act as pointers around the head. So every person that is added to the list is added after the head, if the head is removed then the next node / person becomes the head node and so on and so forth. To put it blatantly, the list functions off the head node.
Theres multiple ways you could use a list designed like this for, one of them could be a to-do list because engineering jobs typically stack up. Maybe the engineer is making a wait list for a restaurant that needs to have some sort of list that can adapt rather than set in stone. If you look at it from a sports perspective you could rearrange it to function as a depth chart of sorts for any team. The possibilities for engineers and a node list are really endless.
'''
