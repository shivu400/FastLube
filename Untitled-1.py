class ShopInventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_id, name, price, quantity):
        """Add a new item to inventory or update existing item"""
        self.inventory[item_id] = {
            'name': name,
            'price': price,
            'quantity': quantity
        }

    def remove_item(self, item_id):
        """Remove an item from inventory"""
        if item_id in self.inventory:
            del self.inventory[item_id]
            return True
        return False

    def update_quantity(self, item_id, quantity):
        """Update quantity of an item"""
        if item_id in self.inventory:
            self.inventory[item_id]['quantity'] = quantity
            return True
        return False

    def get_item(self, item_id):
        """Get item details"""
        return self.inventory.get(item_id)

    def list_items(self):
        """List all items in inventory"""
        return self.inventory

    def check_stock(self, item_id):
        """Check if item is in stock"""
        if item_id in self.inventory:
            return self.inventory[item_id]['quantity'] > 0
        return False

    def update_price(self, item_id, new_price):
        """Update price of an item"""
        if item_id in self.inventory:
            self.inventory[item_id]['price'] = new_price
            return True
        return False

# Example usage:
if __name__ == "__main__":
    shop = ShopInventory()
    
    # Add items
    shop.add_item(1, "T-Shirt", 19.99, 50)
    shop.add_item(2, "Jeans", 49.99, 30)
    
    # Update quantity
    shop.update_quantity(1, 45)
    
    # Check stock
    print(shop.check_stock(1))  # True
    
    # Get item details
    print(shop.get_item(1))  # {'name': 'T-Shirt', 'price': 19.99, 'quantity'
    

