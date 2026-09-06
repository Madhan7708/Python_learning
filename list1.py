
produ=["laptop","mobile","tv","fridge"]
prices=[100000,10000,25000,32000]
product_name=input("Enter an product name:")
if product_name in produ:
    index=produ.index(product_name)
    print(f"Product is {product_name} and price is {prices[index]}")
else:
    print("Product is not found")

    