def get_info(self):
    return f"Product: {self.name}, price: {self.price} UAH"


Product = type(
    "Product",
    (),
    {
        "name": "Laptop",
        "price": 35000,
        "get_info": get_info
    }
)


product1 = Product()
product2 = Product()
product2.price = 32000

print(product1.get_info())
print(product2.get_info())
print(type(Product))