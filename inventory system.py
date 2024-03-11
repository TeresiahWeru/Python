from datetime import date 
class Product:
  """Base class representing a product in the inventory."""

  def __init__(self, product_id, name, quantity_in_stock):
    self.product_id = product_id
    self.name = name
    self.quantity_in_stock = quantity_in_stock

  def calculate_value(self):
    """Calculates the total value of the product in stock.

    This method needs to be implemented by derived classes
    based on their specific pricing logic.
    """
    raise NotImplementedError("calculate_value not implemented for base class Product")


class SimpleProduct(Product):
  """Product with a unit price."""

  def __init__(self, product_id, name, quantity_in_stock, unit_price):
    super().__init__(product_id, name, quantity_in_stock)
    self.unit_price = unit_price

  def calculate_value(self):
    """Calculates the total value by multiplying quantity by unit price."""
    return self.quantity_in_stock * self.unit_price


class PerishableProduct(Product):
  """Product with an expiry date and discount based on shelf life."""

  def __init__(self, product_id, name, quantity_in_stock, unit_price, expiry_date):
    super().__init__(product_id, name, quantity_in_stock)
    self.unit_price = unit_price
    self.expiry_date = expiry_date

  def calculate_value(self):
    """Calculates the total value with a discount based on remaining shelf life.

    (Implement your discount logic here based on expiry date)
    This example applies a simple discount based on days remaining.
    """
    discount = 0 
    days_remaining = (self.expiry_date - date.today()).days 
    if days_remaining < 30:
        discount = 0.1  

    discount_factor = 1 - discount
    return (self.quantity_in_stock * self.unit_price) * discount_factor


class DigitalProduct(Product):
  """Product with a single price."""

  def __init__(self, product_id, name, quantity_in_stock, price):
    super().__init__(product_id, name, quantity_in_stock)
    self.price = price

  def calculate_value(self):
    """Calculates the total value based on current price."""
    return self.quantity_in_stock * self.price


apple = SimpleProduct(1, "Apple", 10, 1.5)
milk = PerishableProduct(2, "Milk", 5, 2.0, date(year=2024, month=3, day=15))  # Assuming expiry on 15th March
ebook = DigitalProduct(3, "E-book", 20, 9.99)

print(apple.calculate_value()) 
print(milk.calculate_value())  
print(ebook.calculate_value())  
