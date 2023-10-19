from aiohttp import ClientSession

BASE_URL = "https://messengerg2c217.iranlms.ir/"


class Connection:

    def __init__(self, timeout=20, base_url=None):
        self.client_session = None
        self.timeout = timeout
        self.base_url = base_url or BASE_URL
        self.is_started = False

    def start(self):
        if self.is_started:
            raise ConnectionError("Connection is already started")
        self.is_started = True
        self.client_session = ClientSession()

    def stop(self):
        if not self.is_started:
            raise ConnectionError("Connection is already stopped")
        self.is_started = False
        self.client_session.close()
        self.client_session = None
