from objects import Product as P

def main():
    product1 = P("Milwaukee Drill Gun", 129.99, 5.0)
    product2 = P("Milwaukee Impact Gun", 155.99, 3.7)

    print()
    print("Product data")
    print("Name: {:s}".format(product1.name))
    print("Price: {:.2f}".format(product1.price))
    print("Discount percent: {:.2f}".format(product1.discountPercent))
    print("Discount amount: {0:.2f}".format(product1.getDiscountAmount()))
    print("Discount price: ", product1.getDiscountPrice())

    print()
    print("Name: {:s}".format(product2.name))
    print("Price: {:.2f}".format(product2.price))
    print("Discount percent: {:.2f}".format(product2.discountPercent))
    print("Discount amount: {0:.2f}".format(product2.getDiscountAmount()))
    print("Discount price: ", product2.getDiscountPrice())

    return


if __name__ == '__main__':
    main()