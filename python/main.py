from purchase import Purchase

def main():
    data_file = "data.json"
    purchase = Purchase(data_file)
    purchase.purchase_car()

if __name__ == "__main__":
    main()
