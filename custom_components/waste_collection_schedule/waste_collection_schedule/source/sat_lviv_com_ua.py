import requests
from waste_collection_schedule import Collection  # type: ignore[attr-defined]
from waste_collection_schedule.service.ICS import ICS

TITLE = "SAT - Lviv"
DESCRIPTION = "Special Autotrans - Lviv"
URL = "https://sat-lviv.com.ua//"
TEST_CASES = {
    "Vynnyky, Zabava str ": {"id": 1000},
    "Lviv. Motorna str": {"id": 10000},
}

ICON_MAP = {
    "rubbish": "mdi:trash-can",
    "recycling": "mdi:recycle",
}

# API_URL = "https://www.abfall-havelland.de/ics.php"
API_URL = "https://sat-lviv.com.ua/stan-rakhunku?keyword={id}"
ICS_URL = "https://sigma.com.ua/waste/waste.ics"

class Source:
    def __init__(self, id: str | int):
        self._id: str | int = id
        self._ics = ICS()

    def fetch(self) -> list[Collection]:
        # ics content
        args = {}
        r = requests.get(ICS_URL, params=args)
        r.raise_for_status()
        r.encoding = "utf-8"
        dates = self._ics.convert(r.text)
        entries = []
        for d in dates:
            bin_type = d[1]
            entries.append(
                Collection(d[0], bin_type, ICON_MAP.get(bin_type.split()[0].lower()))
            )

        if not entries:
            raise Exception(
                "Записи не знайдено. Переконайтеся, що адреса точно збігається з адресою, запропонованою тут: https://sat-lviv.com.ua/ics.php"
            )

        return entries
