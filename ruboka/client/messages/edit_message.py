import ruboka


class EditMessage:

    async def edit_message(self: "ruboka.Client", object_guid, message_id, text):
        input = {
            "object_guid": object_guid,
            "message_id": message_id,
            "text": text
        }
        return await self.execute("editMessage", input)
