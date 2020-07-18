from dataclasses import dataclass
import aiohttp
from datetime import date

TWSE_BASE_URL = 'http://www.twse.com.tw/'
TPEX_BASE_URL = 'http://www.tpex.org.tw/'


@dataclass
class Stock:
    raw_data: dict = None

    async def fetch(self, session, url, params):
        async with session.get(url, params=params) as response:
            return await response.text()

    async def main(self, year, month, sid):
        async with aiohttp.ClientSession() as session:
            date_format = date(year, month, 1).strftime("%Y%m%d")
            params = {'date': date_format, 'stockNo': sid}
            html = await self.fetch(session, TWSE_BASE_URL + 'exchangeReport/STOCK_DAY', params=params)
            return html
