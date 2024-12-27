# Problem: Write a Python program to create a class representing a shopping cart.
# Include methods for adding and removing items, and calculating the total price.

# Define the class for the shopping cart
class shopping_cart():
    # A dictionary containing item prices (predefined items and their costs)
    item_price = {
        'mobile_phone': 26000,
        'laptop': 100000,
        'charger': 500,
        'keyboard': 5000,
        'camera': 40000,
        'gaming_chair': 20000
    }

    def __init__(self):
        # Initialize an empty list to store items added to the cart
        self.item_list: list = []

    # Method to calculate the total price of all items in the cart
    def cal_total_price(self):
        total_price = 0  # Initialize total price to zero
        # Loop through the items in the cart and add their prices
        for item in self.item_list:
            total_price += self.item_price[item]
        return total_price  # Return the total price

    # Method to add an item to the cart
    def add_item(self, item_name):
        self.item_list.append(item_name)  # Add the item to the cart
        # Print the updated total price after adding the item
        print(f"Added: {item_name.upper()}, Total price of your cart is: {self.cal_total_price()}")

    # Method to remove an item from the cart
    def remove_item(self, item_name):
        self.item_list.remove(item_name)  # Remove the item from the cart
        # Print the updated total price after removing the item
        print(f"Removed: {item_name.upper()}, Total price of your cart is: {self.cal_total_price()}")


# Example usage:

# Create a shopping cart instance
shopping = shopping_cart()
# Add a laptop to the cart
shopping.add_item('laptop')
# Add a charger to the cart
shopping.add_item('charger')
# Remove the laptop from the cart
shopping.remove_item('laptop')

# Create another shopping cart instance
shop = shopping_cart()
# Add a camera to the cart
shop.add_item('camera')
# Remove the camera from the cart
shop.remove_item('camera')