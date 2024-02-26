

class FruitManager:
    def __init__(self):
        self.fruit_stock = {}
        self.log_file = "transaction_log.txt"

    def add_fruit_stock(self, fruit, quantity, price):
        """Add fruit stock to the inventory."""
        try:
            if fruit in self.fruit_stock:
                self.fruit_stock[fruit]["quantity"] += quantity
            else:
                self.fruit_stock[fruit] = {"quantity": quantity, "price": price}

            self._log_transaction("Add Fruit Stock", fruit, quantity)
            return True
        except Exception as e:
            print(f"Error during add_fruit_stock: {e}")
            return False

    def view_fruit_stock(self):
        """View the current fruit stock in the inventory."""
        try:
            print("\nFruit Stock:")
            for fruit, details in self.fruit_stock.items():
                print(f"{fruit}: {details['quantity']} units, Price: ${details['price']}")

            self._log_transaction("View Fruit Stock")
        except Exception as e:
            print(f"Error during view_fruit_stock: {e}")

    def update_fruit_stock(self, fruit, quantity, price):
        """Update the quantity and price of a specific fruit in the inventory."""
        try:
            if fruit in self.fruit_stock:
                self.fruit_stock[fruit]["quantity"] = quantity
                self.fruit_stock[fruit]["price"] = price
                self._log_transaction("Update Fruit Stock", fruit, quantity)
                return True
            else:
                print(f"{fruit} not found in stock.")
                return False
        except Exception as e:
            print(f"Error during update_fruit_stock: {e}")
            return False

    def _log_transaction(self, action, fruit=None, quantity=None):
        """Log each transaction to a file."""
        try:
            with open(self.log_file, "a") as file:
                if fruit and quantity:
                    file.write(f"{action}: {fruit} - {quantity} units\n")
                else:
                    file.write(f"{action}\n")
        except Exception as e:
            print(f"Error during logging transaction: {e}")

    def get_all_transactions(self):
        """Get all transactions as a dictionary."""
        return {"add_fruit_stock": self.add_fruit_stock,
                "view_fruit_stock": self.view_fruit_stock,
                "update_fruit_stock": self.update_fruit_stock}