import asyncio, time

async def routine1():
    print("1")

    await asyncio.sleep(5)
    print("100")

def r():
    time.sleep(8)
    return 

async def routine2():
    print("2")

    await r()
    print("200")

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(routine1(), routine2()))
