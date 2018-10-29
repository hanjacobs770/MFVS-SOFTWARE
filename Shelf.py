class Shelf:
    def __init__(self):
        self.productLists= {}
        self.insertProducts()

    def addProducts(self, product):
        f = open('productList.txt', 'a+')
        self.productLists[product.getName()] = product
        productInfo = product.getName() + '|' + product.getDescription() + '|' + product.getCategory() + '|' + product.getPrice() + '|' + product.getDiscount() + '|' + product.getQuantity() + '|' + product.getCages() + '|' + '\n'
        f.write(productInfo)
        f.close()

    def insertProducts(self):
        self.productLists = {}
        f = open('productList.txt', 'r')
        for line in f:
            productInfo = line.split("|")
            self.productLists[productInfo[0]] = productInfo[1:7]
        f.close()

    def search(self, requirement, target='product'):
        if target == 'product':
            try:
                cat = self.productLists[requirement]
                words = "Product: " + requirement + '\nPrice:' + cat[2] + '\nDiscount:' + cat[3] + '\nQuantity:' + cat[4] + '\nOne-Pack:' + cat[5]\
                + '\nDescription:' + cat[0] + '\n*************************'
                print(words)
            except:
                print('No such product')
        if target == 'category':
            for pds,cat in self.productLists.items():
                if cat[1] == requirement:
                    words = "Product: " + pds + ', Price:' + cat[2] + ', Discount:' + cat[3] + ', Quantity:' + cat[4] + ', One-Pack:' + cat[5] + ', Description:' + cat[0]
                    print(words)
        # else:
        #     print("Please input the defined target")

    def getProductLists(self):
        return self.productLists

    def deleteContent(self, name, type, variation):
        with open('productList.txt', 'r') as r:
            lines = r.readlines()
        with open('productList.txt', 'w') as w:
            for l in lines:
                productInfo = l.split("|")
                if name != productInfo[0]:
                    w.write(l)
                else:
                    productInfo[type] = variation
                    words = productInfo[0] + '|' + productInfo[1] + '|' + productInfo[2] + '|' + productInfo[3] + '|' + productInfo[4] + '|' + productInfo[5] + '|' + productInfo[6]
                    w.write(words)


