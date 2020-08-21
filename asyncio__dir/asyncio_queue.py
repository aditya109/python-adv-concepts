import asyncio
import random


async def newsProducer(MyQueue):
    while True:
        await asyncio.sleep(1)
        print("Putting news item onto queue")
        await MyQueue.put(random.randint(1, 5))


async def newsConsumer(Id, MyQueue):
    print(MyQueue)
    while True:
        print("Consumer: {} Attempting to get from queue".format(Id))
        item = await MyQueue.get()
        if item is None:
            # the producer emits None to indicate that it is done
            break
        print("Consumer: {} consumed article with id: {}".format(Id, item))


loop = asyncio.get_event_loop()
myQueue = asyncio.Queue(loop=loop, maxsize=10)
try:
    loop.run_until_complete(asyncio.gather(newsProducer(myQueue), newsConsumer(1, myQueue), newsConsumer(2, myQueue)))
except KeyboardInterrupt:
    pass
finally:
    loop.close()
