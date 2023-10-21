import ruboka


class DeleteMessages:

    async def delete_messages(self: "ruboka.Client", object_guid, message_ids, type="Global"):
        input = {
            "object_guid": object_guid,
            "message_ids": message_ids,
            "type": type
        }
        return await self.execute("deleteMessages", input)
