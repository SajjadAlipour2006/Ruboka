import ruboka


class SendChatActivity:

    async def send_chat_activity(self: "ruboka.Client", object_guid, activity="Typing"):
        input = {
            "object_guid": object_guid,
            "activity": activity
        }
        return await self.execute("sendChatActivity", input)
