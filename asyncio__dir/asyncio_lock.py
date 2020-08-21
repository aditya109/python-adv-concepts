import asyncio
import time


async def myWorker(local_lock):
    print("Attempting to attain lock")
    # acquire lock
    async with local_lock:
        # run critical section of code
        print("Currently Locked")
        time.sleep(2)
    # our worker releases lock at this poit
    print("Unlocked Critical Section")


async def main():
    # instantiate our local_lock
    local_lock = asyncio.Lock()
    # await the execution of 2 myWorker coroutines
    # each with our same local_lock instance passed in
    await asyncio.wait([myWorker(local_lock), myWorker(local_lock)])


# Start up a simple loop and run our main function
# until it is complete
lock = asyncio.Lock()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print("All Tasks Completed")
loop.close()
