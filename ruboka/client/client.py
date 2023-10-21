from ..network import Connection


class Client:
    API_VERSION = "6"
    PLATFORM = "web.rubika.ir"
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    CLIENT = {
        "app_name": "Main",
        "app_version": "4.4.5",
        "platform": "Web",
        "package": "web.rubika.ir",
        "lang_code": "fa"
    }

    def __init__(
            self,
            auth,
            private_key,
            timeout=None,
            url=None,
            api_version=None,
            platform=None,
            user_agent=None,
            client=None
    ):
        self.connection = Connection(auth, private_key, timeout, url)
        self.api_version = api_version or self.API_VERSION
        self.platform = platform or self.PLATFORM
        self.user_agent = user_agent or self.USER_AGENT
        self.client = client or self.CLIENT

    async def connect(self):
        await self.connection.start()

    async def disconnect(self):
        await self.connection.stop()

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, *args):
        try:
            await self.disconnect()
        except ConnectionError:
            return

    async def execute(self, method, input=None):
        headers = {
            "Origin": f"https://{self.platform}",
            "Referer": f"https://{self.platform}/",
            "Host": self.connection.url.replace("https://", ""),
            "User-Agent": self.user_agent
        }
        return await self.connection.post(self.api_version, method, input, self.client, headers=headers)
