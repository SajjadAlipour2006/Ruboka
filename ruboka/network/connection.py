from json import dumps, loads

from aiohttp import ClientSession

from ..crypto import Encryption


class Connection:
    TIMEOUT = 20
    URL = "https://messengerg2c149.iranlms.ir"

    def __init__(self, auth, private_key, timeout=None, url=None):
        self.crypto = Encryption(auth, private_key)
        self.client_session = None
        self.is_started = False
        self.timeout = timeout or self.TIMEOUT
        self.url = url or self.URL

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

    async def post(self, api_version, method, input, client, **kwargs):
        json = {
            "api_version": api_version,
            "auth": self.crypto.auth,
            "data_enc": {
                "method": method,
                "input": input,
                "client": client
            }
        }
        json["data_enc"] = self.crypto.encrypt(dumps(json["data_enc"]))
        json["sign"] = self.crypto.make_sign_from_data(json["data_enc"])
        async with self.client_session.post(
                self.url,
                json=json,
                timeout=self.timeout,
                **kwargs
        ) as response:
            response_json = await response.json()
            if "data_enc" in response_json:
                response_json = loads(str(self.crypto.decrypt(response_json["data_enc"])))
            if response_json.get("status") != "OK":
                raise Exception(response_json.get("status_det"))
            return response_json
