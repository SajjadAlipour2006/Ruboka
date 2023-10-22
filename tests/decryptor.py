from json import dumps, loads

from ruboka.crypto import Encryption

from config import AUTH, PRIVATE_KEY

data = """

""".strip()

crypto = Encryption(AUTH, PRIVATE_KEY)

print(dumps(loads(crypto.decrypt(data)), indent=4))
