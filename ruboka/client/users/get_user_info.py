import ruboka


class GetUserInfo:

    async def get_user_info(self: "ruboka.Client", object_guid):
        input = {
            "object_guid": object_guid
        }
        return await self.execute("getUserInfo", input)
