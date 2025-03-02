#!/usr/bin/python

class ItemToPurchase:
    def __init__(self, item_name="none", item_description="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity
    
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    
    def add_item(self, item):
        self.cart_items.append(item)
    
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")
    
    def modify_item(self, modified_item):
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                if modified_item.item_price != 0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity != 0:
                    item.item_quantity = modified_item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")
    
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)
    
    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)
    
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart():.2f}")

def update_cart(cart):
    while True:
        done = input("\nAre you done updating the cart? Enter 'yes' to proceed to checkout or 'no' to make changes: ").lower()
        if done == 'yes':
            checkout = input("\nWould you like to check out? Enter 'yes' to finalize purchase or 'no' to make more changes: ").lower()
            if checkout == 'yes':
                print("\nFinal Cart Summary:")
                cart.print_total()
                print("Thank you for shopping!")
                return
            
        print("\nOPTIONS")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        
        choice = input("Choose an option: ")
        if choice == 'a':
            add_items_to_cart(cart)
        elif choice == 'r':
            name = input("Enter name of item to remove: ")
            cart.remove_item(name)
        elif choice == 'c':
            name = input("Enter the item name: ")
            quantity = int(input("Enter the new quantity: "))
            cart.modify_item(ItemToPurchase(name, item_quantity=quantity))
        else:
            print("Invalid option, please try again.")

def add_items_to_cart(cart):
    while True:
        name = input("Enter the item name: ")
        description = input("Enter the item description: ")
        price = float(input("Enter the item price: "))
        quantity = int(input("Enter the item quantity: "))
        cart.add_item(ItemToPurchase(name, description, price, quantity))
        more_items = input("Would you like to add another item? (yes/no): ").lower()
        if more_items != 'yes':
            break

def main():
    customer_name = input("Enter customer's name: ")
    date = input("Enter today's date: ")
    cart = ShoppingCart(customer_name, date)
    add_items_to_cart(cart)
    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {date}")
    update_cart(cart)

if __name__ == "__main__":
    main()


