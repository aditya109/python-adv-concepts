import asyncio


async def myWorker(number):
    return number * 2


async def main(coros):
    for fs in asyncio.as_completed(coros):
        print(await fs)


coros = [myWorker(1) for i in range(5)]

try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(coros))
except KeyboardInterrupt:
    pass
finally:
    loop.close()
