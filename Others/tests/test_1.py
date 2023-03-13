from enum import Enum

HTTPStatusCode = Enum(
    value="HTTPStatusCode",
    names=[
        ("OK", 200),
        ("CREATED", 201),
        ("BAD_REQUEST", 400),
        ("NOT_FOUND", 404),
        ("SERVER_ERROR", 500),
        ])

class mixed_status_code(int, Enum):
    OK = 200
    NEW = 103
    MIXED  = OK | NEW

def root(mono : HTTPStatusCode):
    return {"message": "Hello World",
            "used_method" : mono, 
            "list_method" : list(HTTPStatusCode)
            }
"""
input = 200
for status in HTTPStatusCode:
    if status.value == input:
        print (status.name, status.value)
"""

print(mixed_status_code.MIXED.NEW)
