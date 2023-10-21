from asyncio import run

from ruboka.network import Connection

from config import AUTH, PRIVATE_KEY


async def main():
    c = Connection(AUTH, PRIVATE_KEY)
    await c.start()
    response = await c.post("getChats", {"start_id": None})
    print(response)
    await c.stop()


run(main())
