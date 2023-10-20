from json import dumps, loads

from aiohttp import ClientSession

from ..crypto import Encryption


class Connection:
    URL = "https://messengerg2c208.iranlms.ir"
    PLATFORM = "web.rubika.ir"
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0"
    CLIENT = {
        "app_name": "Main",
        "app_version": "4.3.3",
        "platform": "Web",
        "package": "web.rubika.ir",
        "lang_code": "fa"
    }

    def __init__(self, auth, private_key, timeout=20, url=None):
        self.crypto = Encryption(auth, private_key)
        self.client_session = None
        self.timeout = timeout
        self.url = url or self.URL
        self.is_started = False

    async def start(self):
        if self.is_started:
            raise ConnectionError("Connection is already started")
        self.is_started = True
        self.client_session = ClientSession()

    async def stop(self):
        if not self.is_started:
            raise ConnectionError("Connection is already stopped")
        self.is_started = False
        await self.client_session.close()
        self.client_session = None

    async def post(self, method, input=None):
        headers = {
            "Origin": f"https://{self.PLATFORM}",
            "Referer": f"https://{self.PLATFORM}/",
            "Host": self.url.replace("https://", ""),
            "User-Agent": self.USER_AGENT
        }
        json = {
            "api_version": "6",
            "auth": self.crypto.auth,
            "data_enc": {
                "method": method,
                "input": input,
                "client": self.CLIENT
            }
        }
        print("ruboka1 =", dumps(json, indent=4))
        json["data_enc"] = self.crypto.encrypt(dumps(json["data_enc"]))
        json["sign"] = self.crypto.make_sign_from_data(json["data_enc"])
        print("ruboka2 =", dumps(json, indent=4))
        async with self.client_session.post(
                self.url,
                json=json,
                timeout=self.timeout,
                headers=headers
        ) as response:
            response_json = await response.json()
            if "data_enc" in response_json:
                response_json = loads(str(self.crypto.decrypt(response_json["data_enc"])))
            if response_json.get("status") != "OK":
                raise Exception(response_json.get("status_det"))
            return response_json
