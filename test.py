from fastapi import FastAPI,Query , Cookie
from typing import Union,Annotated
from pydantic import BaseModel,AfterValidator

class Book(BaseModel):
    isbn: str|None = None
    Title:str
    description:str|None = None
    price:float

    model_config = {
            "json_schema_extra": {
                "examples": [
                    {
                        "isbn ": "Foo",
                        "Title": "A very nice Item",
                        "description": 'hu',
                        "price": 3.2,
                    }
                ]
            }
        }

class Author(BaseModel):
    name:str
    summary:str
    age:int
    books:list[Book]


def validate_query(i:int):
    if i:
        if i > 10:
            raise ValueError("number should be > 10")
        return i
    else:
        raise ValueError("number should be less than 10 and greater that zero")

books = [
    {"Title":"Ay Haga",
     "price":0,
     "description":"ay Haga bardo"
     }
]
app = FastAPI()

@app.get("/")
async def hello_world(param1:Annotated[int|None,Query(alias="query",lt=10,gt=0,description="This parameter Tala3 3enena :D")]=None):
    return {"data":"Hello","parameter":param1}


@app.get("/books/{book_id}")
def getbook(book_id:int=0):
    return Book(*books[book_id])


@app.post("/books")
def add_book(book:Book):
    return{
        "Title":book.Title,
        "price":book.price,
        "description":book.description
    }

    
@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}

@app.post("/authors/{author_name}")
def add_author(*,index:int=Query(default=0,include_in_schema=False),author_name:str,author: Author):
    return {
        "Nick Name":author_name,
        "name":author.name,
        "books":author.books
    }
@app.get("/add_books")
def add_book(book:Annotated[Book,Query()]):
    return{
        "Title":book.Title,
        "price":book.price,
        "description":book.description
    }