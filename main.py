from fastapi import FastAPI, File, UploadFile
from typing import Annotated, Union
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    nome_sushi: str
    descricao_sushi: str
    preco_sushi: float
    is_offer: Union[bool, None] = None

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"nome_sushi": item.nome_sushi, "descircao_sushi": item.descricao_sushi, "preco_sushi": item.preco_sushi, "item_id": item_id}
    
@app.post("/files/")
async def create_file(files: Annotated[list[bytes], File()]):
    return {"file_sizes": [len(file) for file in files]}

