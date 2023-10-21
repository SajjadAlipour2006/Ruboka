from random import randint

import ruboka


class SendMessage:

    async def send_message(self: "ruboka.Client", object_guid, text):
        input = {
            "object_guid": object_guid,
            "rnd": str(randint(100000, 999999999)),
            "text": text
        }
        return await self.execute("sendMessage", input)
