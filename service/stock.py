from dataclasses import dataclass, field, asdict
import aiohttp
from datetime import date
import json

from abc import ABCMeta, abstractmethod
from typing import List

TWSE_BASE_URL = 'http://www.twse.com.tw/'
TPEX_BASE_URL = 'http://www.tpex.org.tw/'

@dataclass
class TESEField:
    stat: str = None
    date: date = None
    title: str = None
    fields: list = None
    data: List[list] = field(default_factory=list)
    notes: List[str] = field(default_factory=str)



class Fetcher:
    raw_data: dict = None

    async def fetch(self, session, url, params):
        async with session.get(url, params=params) as response:
            return await response.text()

    @abstractmethod
    async def main(self, year, month, sid):
        raise NotImplemented


class TWSEFetcher(Fetcher):
    async def main(self, year, month, sid):
        async with aiohttp.ClientSession() as session:
            date_format = date(year, month, 1).strftime("%Y%m%d")
            params = {'date': date_format, 'stockNo': sid}
            html = await self.fetch(session, TWSE_BASE_URL + 'exchangeReport/STOCK_DAY', params=params)
            return html

    def api_response_format(self, data):
        data = json.loads(data)
        TESE = TESEField(**data)
        return asdict(TESE)

    def purify(self, raw_data):
        format_data = self.api_response_format(data=raw_data)
        return format_data

class TPEXFetcher(Fetcher):
    pass


class Stock:
    def base_info(self):
        pass
