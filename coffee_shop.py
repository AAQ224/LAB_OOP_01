class Drink:
    def __init__(self, name: str, price: float, size: str):
        self.name = name
        self.price = price
        self.size = size

    def display_info(self):
        print(f"{self.name} ({self.size}) - {self.price:.1f} SAR")

    def change_price(self, new_price):
        self.price = new_price

    def apply_discount(self, percentage: float):
        self.price = self.price * (1 - percentage / 100)


Drink1 = Drink("Latte", 18, "Medium")
Drink2 = Drink("Espresso", 12, "Small")
Drink3 = Drink("Cappuccino", 22, "Large")


print("=== Coffee Shop Menu ===")
Drink1.display_info()
Drink2.display_info()
Drink3.display_info()
Drink1.change_price(20)
Drink3.apply_discount(25)
print("=== Updated Menu ===")
Drink1.display_info()
Drink3.display_info()