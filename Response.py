import requests
import json


class Response:
    __url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"

    def get_response(self):
        try:
            return requests.get(self.__url)
        except Exception:
            return

    @staticmethod
    def parse_content(content):
        try:
            return json.loads(content)
        except Exception:
            return
