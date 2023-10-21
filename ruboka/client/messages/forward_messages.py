from random import randint

import ruboka


class ForwardMessages:

    async def forward_messages(self: "ruboka.Client", from_object_guid, to_object_guid, message_ids):
        input = {
            "from_object_guid": from_object_guid,
            "to_object_guid": to_object_guid,
            "message_ids": message_ids,
            "rnd": str(randint(100000, 999999999))
        }
        return await self.execute("forwardMessages", input)
