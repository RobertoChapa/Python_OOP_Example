class Product:
    # constructor
    def __init__(self, name, price, discountPercent):
        self.name = name
        self.price = price
        self.discountPercent = discountPercent

    def getDiscountAmount(self):
        discountAmount = self.price * self.discountPercent / 100

        return discountAmount

    def getDiscountPrice(self):
        discountPrice = self.price - self.getDiscountAmount()
        str_discountPrice = "{:.2f}".format(discountPrice)

        return str_discountPrice