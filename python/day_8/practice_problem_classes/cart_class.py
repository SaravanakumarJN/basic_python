class ShoppingCart():
    items_present_in_cart = {}
    def __init__(self, customer_id):
        self.customer_id = customer_id
    
    def add_item(self,product, price):
        if self.items_present_in_cart.get(product) == None:
            self.items_present_in_cart[product] = price
            print("%s added successfully" %(product))
        else:
            print("%s is already present" %(product))

    def remove_item(self, product):
        if self.items_present_in_cart.get(product) == None:
            print("%s not present in the cart." %(product))
        else:
            self.items_present_in_cart.pop(product)
            print("%s removed succesfully" %(product))


shopping_cart_instance_1 = ShoppingCart("12345")

shopping_cart_instance_1.add_item("Bread", 20)
shopping_cart_instance_1.add_item("Milk", 30)
print(shopping_cart_instance_1.items_present_in_cart)

shopping_cart_instance_1.remove_item("Milk")
print(shopping_cart_instance_1.items_present_in_cart)


