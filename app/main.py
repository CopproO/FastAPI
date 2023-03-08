from fastapi import FastAPI
from enum import Enum
from typing import Union

    
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
    
app = FastAPI()


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

"""HTTPStatusCode  = Enum(
    "HTTPStatusCode", {
    "GET": "GET.this",
    "POST" : "POST.this", 
    "PUSH" : "PUSH.this",
    "PATCH" : "PATCH.this", 
    "DELETE" : "DELETE.this"
})
"""

class HTTPStatusCode (Enum):
    OK =  200
    CREATED = 201
    BAD_REQUEST = 400
    NOT_FOUND = 404
    SERVER_ERROR = 500
    EVERY = OK | CREATED | BAD_REQUEST | NOT_FOUND | SERVER_ERROR



@app.get('/{statusCode:int}')
async def root(statusCode : HTTPStatusCode): 
    return {"message": "Hello World",
            "used_method" : f"Responce: {statusCode.name}, status code: {statusCode.value}",
            "list_of_methods" : list(HTTPStatusCode)
            }

@app.get('/hello')
async def mono():
    return {"message": "Monogatari no Tomodachi Game"}

@app.get("/items/")
async def read_item(skip : int = 0, limit : int = 10):

    if skip < limit:
        return {"item_id": fake_items_db[skip : skip + limit]}
    
    else:
        return {"error_message": f"skip: {skip} > limit: {limit}, please insert a skip value less than {limit}"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/item/{item_id}")
async def read_item(
    item_id: str, 
    q: Union[str, None] = None, 
    short: bool = False
    ):

    item = {"item_id": item_id}

    if q:
        return {"item_id": item_id, "q": q}
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
 
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, 
    item_id: str,
    model_names : Union[ModelName, None]= None,
    q: Union[str, None] = None, 
    short : bool = False

    ):

    item = {
        "item_id": item_id, 
        "owner_id": user_id,
        }
    
    if model_names is ModelName.alexnet:
        item.update({
            "model_name": model_names,
            "message": "Deep Learning FTW!"
            })
        
    if q:
        item.update({"q": q})

    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )

    return item

