def cartEntity(item) -> dict:
    return{
        "id": (item["_id"]),
        "firstName":item["firstName"],
        "lastName":item["lastName"],
        "email":item["email"],
        "product":item["product"],
        "address":item["address"],
        "address2":item["address2"],
        "country":item["country"],
        "state":item["state"],
        "zip":item["zip"],
        "cc-name":item["cc-name"],
        "cc-number":item["cc-number"],
        "cc-expiration":item["cc-expiration"],
         "cc-cvv":item["cc-cvv"]
    }
def cartsEntity(items) -> list:
    return[cartEntity(item) for item in items]