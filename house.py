def predict_price(area, bedrooms):
   price = (area * 2500) + (bedrooms * 400000) + 1000000
    return price


if __name__ == "__main__":
    area = int(input("Enter area: "))
    bedrooms = int(input("Enter bedrooms: "))
    print("Estimated Price:", predict_price(area, bedrooms))
