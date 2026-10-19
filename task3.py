3. Власний метаклас для логування
Створіть метаклас LoggingMeta, який під час створення
кожного класу виводить повідомлення:
Створюється клас: назва_класу
Створіть із його допомогою класи Customer, Order і
Payment.
Перевірте, що повідомлення з'являються під час оголошення
класів, а не під час створення їхніх екземплярів.
Мета: зрозуміти, як працює __new__() метакласу.

class LoggingMeta(type):
    def __new__(mcs, name, bases, namespace):
        print(f"Створюється клас: {name}")
        return super().__new__(mcs, name, bases, namespace)


class Customer(metaclass=LoggingMeta):
    pass


class Order(metaclass=LoggingMeta):
    pass


class Payment(metaclass=LoggingMeta):
    pass


print("--- Класи оголошено, тепер створюємо екземпляри ---")

customer = Customer()
order = Order()
payment = Payment()

print("--- Екземпляри створено ---")
