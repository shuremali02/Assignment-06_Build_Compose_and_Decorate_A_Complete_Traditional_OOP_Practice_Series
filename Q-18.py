# <!-- ### 18. **Property Decorators: `@property`, `@setter`, and `@deleter`**

# **Assignment:**  
# Create a class `Product` with a private attribute `_price`. Use `@property` to get the price, `@price.setter` to update it, and `@price.deleter` to delete it.

# ----------

class Product:
    def __init__(self,price):
        self._price=price
    @property    
    def price(self):
        return self._price
    
    @price.setter
    def price(self,new_price):
        if new_price <= 0:
            raise ValueError("price must be greater then 0")
        self._price=new_price

    @price.deleter
    def price(self):
        print("Deleting price!")
        del self._price    


    


p=Product(15)
print(p.price)
p.price=20
print(p.price)
del p.price #AttributeError: 'Product' object has no attribute '_price'.

print(p.price)
