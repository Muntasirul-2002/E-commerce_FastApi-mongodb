def contactEntity(item)->dict:
    return{
        "id": (item["_id"]),
        "email":item["email"],
        "desc":item["desc"],
    }

def contactsEntity(items) -> list:
    return[contactEntity(item) for item in items]