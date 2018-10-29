class Cart:
    def __init__(self, name):
        self.name = name
        self.productList = []
        self.insertCart(name)

    def addCart(self, product, quantity, total):
        f = open('Cart.txt','a+')
        content = self.name + '|' + product + '|' + quantity + '|' + str(total) + '|' + '\n'
        f.write(content)
        f.close()

    def total(self):
        total = 0
        for v in productList.values():
            total += y[3]
        return total

    def insertCart(self, user):
        f = open('Cart.txt','r')
        for lines in f:
            productInfo = lines.split('|')
            if productInfo[0] == user:
                self.productList.append(productInfo[1:])
        f.close()

    def getProductList(self):
        return self.productList

    def deleteContent(self):
        with open('Cart.txt', 'r') as r:
            lines = r.readlines()
        with open('Cart.txt', 'w') as w:
            for l in lines:
                cartInfo = l.split("|")
                if self.name != cartInfo[0]:
                    w.write(l)
                else:
                    pass