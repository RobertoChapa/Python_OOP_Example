def main():
    product1 = 'Milwaukee Drill Gun'
    price = 129.99
    discountPercent = 5.0

    da = discountAmount(price, discountPercent)  # discount amount
    dp = discountPrice(price, da)  # discount price

    print(product1, " Discount Price: ${:.2f}".format(dp))

    return

def discountAmount(price, discountPercent):
    da = price * discountPercent / 100

    return da  # discount amount

def discountPrice(price, da):
    dp = price - da

    return dp  # discount price


if __name__ == '__main__':
    main()