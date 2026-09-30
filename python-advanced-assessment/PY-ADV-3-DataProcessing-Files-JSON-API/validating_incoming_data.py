# Function to validate product data
def validate_product(product):
    errors = []

    if not product.get("title"):
        errors.append("Title is required.")

    if not isinstance(product.get("price"), (int, float)):
        errors.append("Price must be a number.")
    elif product["price"] <= 0:
        errors.append("Price must be greater than 0.")

    if not isinstance(product.get("stock"), int):
        errors.append("Stock must be an integer.")
    elif product["stock"] < 0:
        errors.append("Stock cannot be negative.")

    if errors:
        return False, errors

    return True, ["Data is valid."]

products = [
    {
        "title": "Wireless Mouse",
        "price": 29.99,
        "stock": 15
    },
    {
        "title": "",
        "price": -10.00,
        "stock": "out of stock"
    }
]

for product in products:
    valid, messages = validate_product(product)

    print("Product:", product)

    if valid:
        print("Result: Valid")
    else:
        print("Result: Invalid")

    for message in messages:
        print("-", message)

    print()