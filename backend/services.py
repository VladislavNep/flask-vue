import uuid

PRODUCTS = [
    {
      "id": uuid.uuid4().hex,
      "name": "Сапоги дет. синие sh100 x-warm",
      "quantity": "2",
      "currency": "RUB",
      "price": "1690"
    },
    {
        "id": uuid.uuid4().hex,
        "name": "Куртка муж. чер. sh500 u-warm",
        "quantity": "1",
        "currency": "USD",
        "price": "236"
    },
    {
        "id": uuid.uuid4().hex,
        "name": "Палатка для кемпинга arpenaz",
        "quantity": "1",
        "currency": "EUR",
        "price": "138"
    },
]


def remove_product(product_id):
    for product in PRODUCTS:
        if product["id"] == product_id:
            PRODUCTS.remove(product)
            return True
    return False


def add_product(post_data):
    PRODUCTS.append({
        "id": uuid.uuid4().hex,
        "name": post_data.get('name'),
        "quantity": post_data.get('quantity'),
        "currency": post_data.get('currency'),
        "price": post_data.get('price')
    })