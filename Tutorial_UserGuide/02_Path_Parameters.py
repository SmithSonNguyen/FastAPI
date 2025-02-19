#Step 1: import FastAPI
from fastapi import FastAPI

# Step 2: create a FastAPI "instance"
app = FastAPI()




# http method 'get'
# @: decorator
# async: bien code thanh bat dong bo => Cho phép nhiều request được xử lý đồng thời mà không cần chờ request trước hoàn tất.
# @app.get("/items/{item_id}") 
# async def read_item(item_id):
#   return {"item_id": item_id}

# --------------------------------------------------------
# Path parameters with types
# Chỉ định kiểu giá trị cho item_id
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#   return {"item_id": item_id}

# ----------------------------------------------------------
# Data conversion (chuyển đổi data)
# Notice that the value your function received (and returned) is 3, as a Python int, not a string "3".
# So, with that type declaration, FastAPI gives you automatic request "parsing".

# ------------------------------------------
# Data validation (xác nhận data)

# ---------------------------------------------
## Order matters
# b1
# @app.get("/users/me")
# async def read_user_me():
#   return {"user_id": "the current user"}

# @app.get("/users/{user_id}")
# async def read_user(user_id: int):
#   return {"user_id": user_id}

# b2
# @app.get("/users")
# async def read_users():
#   return ["Rick", "Morty"]

# @app.get("/users")
# async def read_users2():
#     return ["Bean", "Elfo"]
# -> Chung path => ham nao khai bao truoc se dc tra ket qua

# ----------------------------------------
# Predefined values
# You want the possible valid path parameter values to be predefined, you can use a standard Python Enum.
# from enum import Enum
# class ModelName(str, Enum): #Enum: Create a collection of name/value pairs.
#   alexnet = "alexnet"
#   resnet = "resnet"
#   lenet = "lenet"

# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#   if model_name is ModelName.alexnet:
#     return {"model_name": model_name, "message": "Deep Learning FTW!"}
#   if (model_name.value == "lenet"):
#     return {"model_name": model_name, "message": "LeCNN all the images"}
#   return {"model_name": model_name, "message": "Have some residuals"}

# -------------------------------------------------
# Path convertor
@app.get("/files/{file_path: path}")
async def read_file(file_path: str):
  return {"file_path": file_path}
# -> Trả ra toàn vẹn path phía sau /files/...




