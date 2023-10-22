import ruboka


class GetObjectByUsername:

    async def get_object_by_username(self: "ruboka.Client", username):
        input = {
            "username": username
        }
        return await self.execute("getObjectByUsername", input)
