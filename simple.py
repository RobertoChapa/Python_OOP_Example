product1 = 'Milwaukee Drill Gun'
price = 129.99
discountPercent = 5.0

discountAmount = price * discountPercent / 100
discountPrice = price - discountAmount

print(product1, "Discount Price: ${:.2f}".format(discountPrice))
