from typing import Optional
from fastapi import FastAPI
import uvicorn

from service.stock import TWSEFetcher, TPEXFetcher

app = FastAPI()
TWSE_fetcher = TWSEFetcher()
TPEX_fetcher = TPEXFetcher()


@app.get("/stock")
async def get_stock_info():
    return await TWSE_fetcher.main(2019, 11, 2330)
    # return await TPEX_fetcher.main(2019, 11, 2330)


@app.get("/purify")
async def get_purify_data():
    raw_data = await TWSE_fetcher.main(2019, 11, 2330)
    return TWSE_fetcher.purify(raw_data=raw_data)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
