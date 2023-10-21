from asyncio import run

from ruboka import Client

from config import AUTH, PRIVATE_KEY


async def main():
    c = Client(AUTH, PRIVATE_KEY)
    async with c:
        response = await c.execute("getChats", {"start_id": None})
    print(response)


run(main())
