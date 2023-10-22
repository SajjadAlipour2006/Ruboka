import ruboka


class GetGroupAllMembers:

    async def get_group_all_members(self: "ruboka.Client", group_guid):
        input = {
            "group_guid": group_guid
        }
        return await self.execute("getGroupAllMembers", input)
