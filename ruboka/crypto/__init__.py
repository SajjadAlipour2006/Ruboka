from base64 import b64decode, b64encode, urlsafe_b64decode
from json import loads

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Util.Padding import pad, unpad


class Encryption:
    IV = b"\x00" * 16

    @staticmethod
    def replace_char_at(e, t, i):
        return e[0:t] + i + e[t + len(i):]

    @staticmethod
    def change_auth_type(auth_enc):
        n = ""
        lowercase = "abcdefghijklmnopqrstuvwxyz"
        uppercase = lowercase.upper()
        digits = "0123456789"
        for s in auth_enc:
            if s in lowercase:
                n += chr(((32 - (ord(s) - 97)) % 26) + 97)
            elif s in uppercase:
                n += chr(((29 - (ord(s) - 65)) % 26) + 65)
            elif s in digits:
                n += chr(((13 - (ord(s) - 48)) % 10) + 48)
            else:
                n += s
        return n

    @staticmethod
    def decrypt_rsa_oaep(private: str, data_enc: str):
        key_pair = RSA.import_key(private.encode("utf-8"))
        return PKCS1_OAEP.new(key_pair).decrypt(b64decode(data_enc)).decode("utf-8")

    @staticmethod
    def rsa_key_generate():
        key_pair = RSA.generate(1024)
        public = Encryption.change_auth_type(b64encode(key_pair.publickey().export_key()).decode("utf-8"))
        private = key_pair.export_key().decode("utf-8")
        return public, private

    def __init__(self, auth: str, private_key: str):
        self.auth = auth
        self.private_key = private_key
        self.decoded_private_key = loads(b64decode(private_key).decode('utf-8'))['d']
        self.key = bytearray(self.secret(auth), "UTF-8")
        self.keypair = RSA.import_key(self.decoded_private_key.encode("utf-8"))

    def secret(self, e):
        t = e[0:8]
        i = e[8:16]
        n = e[16:24] + t + e[24:32] + i
        s = 0
        while s < len(n):
            e = n[s]
            if "0" <= e <= "9":
                t = chr((ord(e[0]) - ord("0") + 5) % 10 + ord("0"))
                n = self.replace_char_at(n, s, t)
            else:
                t = chr((ord(e[0]) - ord("a") + 9) % 26 + ord("a"))
                n = self.replace_char_at(n, s, t)
            s += 1
        return n

    def encrypt(self, text):
        raw = pad(text.encode("UTF-8"), AES.block_size)
        aes = AES.new(self.key, AES.MODE_CBC, self.IV)
        enc = aes.encrypt(raw)
        result = b64encode(enc).decode("UTF-8")
        return result

    def decrypt(self, text):
        aes = AES.new(self.key, AES.MODE_CBC, self.IV)
        dec = aes.decrypt(urlsafe_b64decode(text.encode("UTF-8")))
        result = unpad(dec, AES.block_size).decode("UTF-8")
        return result

    def make_sign_from_data(self, data_enc: str):
        sha_data = SHA256.new(data_enc.encode("utf-8"))
        signature = pkcs1_15.new(self.keypair).sign(sha_data)
        return b64encode(signature).decode("utf-8")
