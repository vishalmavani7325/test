

from customer import Customer


def display_menu():
    """Display the main menu of the Fruit Store application."""
    print("\nMenu:")
    print("1. Add Fruit Stock")
    print("2. View Fruit Stock")
    print("3. Update Fruit Stock")
    print("4. Exit")


def execute_transaction(transaction_type, *args):
    """Execute the specified transaction based on the user's choice."""
    try:
        transaction_functions = customer.fruit_manager.get_all_transactions()
        if transaction_type in transaction_functions:
            transaction_functions[transaction_type](*args)
            print(f"{transaction_type.replace('_', ' ')} executed successfully.")
        else:
            print("Invalid transaction type.")
    except Exception as e:
        print(f"Error during transaction execution: {e}")


def view_fruit_stock():
    """View the fruit stock."""
    execute_transaction("view_fruit_stock")


def welcome_message():
    """Welcome message for the Fruit Store application."""
    print("Welcome to the Fruit Market!")
    print("1. Manager")
    print("2. Customer")


def select_role():
    """Prompt the user to select their role."""
    while True:
        try:
            role_choice = int(
                input("Select your role (1 for Manager, 2 for Customer): "))
            if role_choice == 1:
                return "manager"
            elif role_choice == 2:
                return "customer"
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    try:
        welcome_message()
        role = select_role()

        if role == "manager":
            while True:
                display_menu()
                choice = input("Enter your choice: ")

                if choice == '1':
                    fruit = input("Enter the fruit name: ")
                    quantity = int(input("Enter the quantity: "))
                    price = float(input("Enter the price per unit: $"))
                    execute_transaction("add_fruit_stock",
                                        fruit, quantity, price)

                elif choice == '2':
                    view_fruit_stock()

                elif choice == '3':
                    fruit = input("Enter the fruit name: ")
                    quantity = int(input("Enter the new quantity: "))
                    price = float(input("Enter the new price per unit: $"))
                    execute_transaction(
                        "update_fruit_stock", fruit, quantity, price)

                elif choice == '4':
                    print("Exiting the Fruit Store Console application.")
                    break

                else:
                    print("Invalid choice. Please enter a valid option.")

        elif role == "customer":
            # Code for customer interactions can be added here
            pass

        else:
            print("Invalid role selection.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")


if __name__ == "__main__":
    customer = Customer()
    main()