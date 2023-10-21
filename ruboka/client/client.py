from ..network import Connection


class Clinet:

    def __init__(
            self,
            auth,
            private_key,
            timeout=None,
            url=None,
            platform=None,
            user_agent=None,
            client=None
    ):
        self.connection = Connection(auth, private_key, timeout, url, platform, user_agent, client)
