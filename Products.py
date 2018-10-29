class Products:
    def __init__(self, name, description, category, price, discount, quantity, cages):
        self.name = str(name)
        self.description = str(description)
        self.category = str(category)
        self.price = int(price)
        self.discount = float(discount)
        self.quantity = int(quantity)
        self.cages = cages

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getCategory(self):
        return self.category

    def getPrice(self):
        return str(self.price)

    def getDiscount(self):
        return str(self.discount)

    def getQuantity(self):
        return str(self.quantity)

    def getCages(self):
        return str(self.cages)

    def setDiscount(self,newDiscount):
        self.discount = newDiscount

