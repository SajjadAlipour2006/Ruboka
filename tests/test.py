from asyncio import run

from ruboka import Client

from config import AUTH, PRIVATE_KEY, GUID


async def main():
    c = Client(AUTH, PRIVATE_KEY)
    async with c:
        msg = await c.send_message(GUID, "hello")
        print(msg)
        msg = msg["message_update"]
        response = await c.edit_message(GUID, msg["message_id"], "edited hello")
        print(response)
        response = await c.forward_messages(GUID, GUID, [msg["message_id"]])
        print(response)
        response = await c.delete_messages(GUID, [msg["message_id"]])
        print(response)


run(main())
