class Drink:
    def __init__(self, name: str, price: float, size: str):
        self.name = name
        self.price = price
        self.size = size

    def display_info(self):
        return f"{self.name} ({self.size}) - {self.price:.1f} SAR"

    def change_price(self, new_price: float):
        self.price = new_price

    def apply_discount(self, percentage: float):
        self.price = self.price * (1 - percentage / 100)


latte = Drink("Latte", 18, "Medium")
espresso = Drink("Espresso", 12, "Small")
cappuccino = Drink("Cappuccino", 22, "Large")


print("=== Coffee Shop Menu ===")
print(latte.display_info())
print(espresso.display_info())
print(cappuccino.display_info())
latte.change_price(20)
cappuccino.apply_discount(25)
print("=== Updated Menu ===")
print(latte.display_info())
print(espresso.display_info())
print(cappuccino.display_info())