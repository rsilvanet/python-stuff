class Product:
    def __init__(self, cost, code, stock):
        self.cost = cost
        self.code = code
        self.stock = stock
        self.description = 'Product without description'

class Electrical(Product):
    def __init__(self, cost, code, stock, brand, voltage):
        super().__init__(cost, code, stock)
        self.brand = brand
        self.voltage = voltage
        self.description = 'Electrical without description'

class Refrigerator(Electrical):
    def __init__(self, cost, code, stock, brand, voltage, color):
        super().__init__(cost, code, stock, brand, voltage)
        self.color = color
        self.description =  self.color + ' ' + self.brand + ' Refrigerator'

class TV(Electrical):
    def __init__(self, cost, code, stock, brand, voltage, inches):
        super().__init__(cost, code, stock, brand, voltage)
        self.inches = inches
        self.description =  self.inches + '" ' + self.brand +  ' TV'

class Book(Product):
    def __init__(self, cost, code, stock, title, author):
        super().__init__(cost, code, stock)
        self.title = title
        self.author = author
        self.description = self.title + ' Book'

class OrderItem:
    def __init__(self, product, amount):
        self.product = product
        self.amount = amount
        self.description = product.description + ' - ${:.2f} x {} = ${:.2f}'.format(product.cost, amount, self.get_cost())

    def get_cost(self):
        return self.product.cost * self.amount

class Order:
    def __init__(self, items, deliveryFee):
        self.items = items
        self.deliveryFee = deliveryFee

    def get_total_amount(self):
        totalAmount = 0
        for item in self.items:
            totalAmount += item.amount
        return totalAmount

    def get_total_cost(self):
        totalCost = 0
        for item in self.items:
            totalCost += item.get_cost()
        return totalCost + self.deliveryFee

    def get_resume(self):
        resume = '# Order\n'
        for item in self.items:
            resume += '# ' + item.description + '\n'
        resume += '# Delivery Fee = ${:.2f}\n'.format(self.deliveryFee)
        resume += '# Total = ${:.2f} ({} itens)'.format(self.get_total_cost(), self.get_total_amount())
        return resume.strip()

item1 = TV(1000, 123456, 2, 'LG', 220, '40')
item2 = Refrigerator(1500, 789789, 2, 'Eletrolux', 240, 'White')
item3 = Book(50, 789456, 1, 'The Lord of the Rings', 'Tolkien')

orderItem1 = OrderItem(item1, 2)
orderItem2 = OrderItem(item2, 1)
orderItem3 = OrderItem(item3, 3)

order = Order([orderItem1,orderItem2,orderItem3], 50)

print(order.get_resume())
