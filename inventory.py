
#  ========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        # Initialise attributes

        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        # Return cost of the shoe

        return self.cost

    def get_quantity(self):
        # Return quantity of shoes

        return self.quantity

    def __str__(self):
        # String representation of the shoe object

        return (f"Country: {self.country}, Code: {self.code}, "
                f"Product: {self.product}, Cost: {self.cost}, "
                f"Quantity: {self.quantity}")


#  =============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


#  ==========Functions outside the class==============
def read_shoes_data():
    """Reads inventory.txt and populates shoe_list with Shoe objects."""
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()[1:]  # skip header line
            for line in lines:
                data = line.strip().split(",")
                if len(data) == 5:
                    country, code, product, cost, quantity = data
                    shoe = Shoe(country, code, product, cost, quantity)
                    shoe_list.append(shoe)
    except FileNotFoundError:
        print("Error: inventory.txt file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def capture_shoes():
    """Allows user to input new shoe data and add to shoe_list."""
    country = input("Enter country: ")
    code = input("Enter product code: ")
    product = input("Enter product name: ")
    cost = input("Enter cost: ")
    quantity = input("Enter quantity: ")

    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    print("Shoe captured successfully!")


def view_all():
    """Displays all shoes in shoe_list."""
    for shoe in shoe_list:
        print(shoe)


def re_stock():
    """Finds shoe with lowest quantity and allows restocking."""
    if not shoe_list:
        print("No shoes available.")
        return

    lowest_shoe = min(shoe_list, key=lambda s: s.quantity)
    print("Lowest stock item:", lowest_shoe)

    choice = input("Do you want to restock this item? (yes/no): ").lower()
    if choice == "yes":
        add_qty = int(input("Enter quantity to add: "))
        lowest_shoe.quantity += add_qty
        print(f"Updated quantity: {lowest_shoe.quantity}")


def search_shoe():
    """Searches for a shoe by code."""
    code = input("Enter shoe code to search: ")
    for shoe in shoe_list:
        if shoe.code == code:
            print("Shoe found:", shoe)
            return
    print("Shoe not found.")


def value_per_item():
    """Calculates and prints total value of each shoe."""
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product} ({shoe.code}) - Total Value: {value}")


def highest_qty():
    """Finds shoe with highest quantity and marks it for sale."""
    if not shoe_list:
        print("No shoes available.")
        return

    highest_shoe = max(shoe_list, key=lambda s: s.quantity)
    print(f"Product on sale: {highest_shoe.product} ({highest_shoe.code}) "
          f"with quantity {highest_shoe.quantity}")


# ==========Main Menu=============

def main_menu():
    read_shoes_data()  # load data at start

    while True:
        print("\n===== Warehouse Menu =====")
        print("1. View all shoes")
        print("2. Capture new shoe")
        print("3. Restock lowest quantity shoe")
        print("4. Search shoe by code")
        print("5. Calculate value per item")
        print("6. Show product with highest quantity")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_all()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            re_stock()
        elif choice == "4":
            search_shoe()
        elif choice == "5":
            value_per_item()
        elif choice == "6":
            highest_qty()
        elif choice == "7":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the menu
if __name__ == "__main__":
    main_menu()
