import asyncio
import random
import time


async def myTask(id):
    process_time = random.randint(1, 5)
    await asyncio.sleep(process_time)

    print(f"Coroutine: {id}, has successfully completed after {process_time} seconds")


async def main():
    tasks = []
    for i in range(10):
        tasks.append(asyncio.ensure_future(myTask(i)))

    await asyncio.gather(*tasks)

start_time = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
print(time.time()-start_time)
