from typing import Optional
from fastapi import FastAPI
import uvicorn

from service.stock import Stock

app = FastAPI()
stock = Stock()



@app.get("/")
async def read_root():
    return await stock.main(2019, 11, 2330)




@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
