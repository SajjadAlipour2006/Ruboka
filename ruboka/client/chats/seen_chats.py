import ruboka


class SeenChats:

    async def seen_chats(self: "ruboka.Client", seen_list):
        input = {
            "seen_list": seen_list
        }
        return await self.execute("seenChats", input)
