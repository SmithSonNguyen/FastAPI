from fastapi import FastAPI

app = FastAPI()



# fake_items_db = [ {"item_name": "Foo"}, 
#                   {"item_name": "Bar"}, 
#                   {"item_name": "Baz"}]

# @app.get("/items/")
# async def read_item(skip:int = 0, limit:int = 0):
#   return fake_items_db[skip : skip + limit]

""" Explain
The query is the set of key-value pairs that go after the ? in a URL, separated by & characters
  Ex: http://127.0.0.1:8000/items/?skip=0&limit=10

skip: int = 0 → Default 0, determines how many items to skip.
limit: int = 10 → Default 10, limits how many items to return.
fake_items_db[skip : skip + limit] : slice => get character [start : end]
"""

# 1. Defaults
"""Read docs"""

# Optional parameters
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None):
#   if q:
#     return {"item_id": item_id, "q": q}
#   return {"item_id": item_id}

"""Explain
http://127.0.0.1:8000/items/123?q=hello -> {"item_id": "123",
                                              "q": "hello" }
                                              
q: str | None = None → Optional query parameter:
    The syntax str | None means it can be either a string or None.
    Default value is None, so it's optional.
"""

# 2. Query parameter type conversion
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, k:str | None = None, short:bool = False):
#   item = {"item_id": item_id}
#   if k:
#     item.update( {"k": k} ) #Thêm Obj vào
#   if not short:
#     item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#   return item

"""Explain
k:str | None = None : Default None, but want query, must have ".../..?k=..."
short:bool = False : Default False, but want query, must have ".../..?short=[1 || yes|| True || on]
  Các từ trong [ ] bắt kể viết in hoa hay thường xen lẫn vẫn hiểu
"""

# 3. Multiple path and query parameters
# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item

""" Same topic Query parameter type conversion
"""

# 4. Required query parameters
# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, needy: str):
#     item = {"item_id": item_id, "needy": needy}
#     return item

""" Explain
Here the query parameter 'needy' is a required query parameter of type str.
If URL without 'needy' like: "http://127.0.0.1:8000/items/foo-item" => Will see the error
And URL look like: "http://127.0.0.1:8000/items/foo-item?needy=sooooneedy" => OK (no see err)
"""

@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str, skip: int = 0, limit: int | None = None):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item

"""Explain
In this case, there are 3 query parameters:
    needy, a required str.
    skip, an int with a default value of 0.
    limit, an optional int.
"""
  
  