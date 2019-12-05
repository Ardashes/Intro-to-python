import productcheck as prod

def buy(product, num, price):
    if prod.check(product, num):
        print("You bought " + product + " and spent ", num * price)
    else:
        print("Sorry! We are out of this product.")

def main():
    buy('candy', 10, 10)

main()