import asyncio

import httpx, time

start = time.time()
async def req():
    # res = httpx.get("http://localhost:8000/app_1/a/index_1/") # 0.35 - 0.7 s (5 requests), with asyncio.sleep(1) 0.32-0.42
    res = httpx.get("http://localhost:8000/app_1/a/") # 0.27-0.34s (5 requests)
    print('res = ', res)

async def gather_tasks():
    await asyncio.gather(
                req(),
                req(),
                req(),
                req(),
                req(),
            )

asyncio.run(gather_tasks())
print(f'time = {time.time() - start}')


async def async_sleep():
    # loop = asyncio.get_event_loop()
    # loop.create_task(http_call_async())
    for num in range(1, 4):
        print(num)
        await asyncio.sleep(1)
        print(num)
    # return HttpResponse("Non-blocking HTTP request")
# asyncio.run(async_sleep())

async def main():
    loop = asyncio.get_event_loop()
    # loop.create_task(async_sleep()) #
    # t = loop.create_task(async_sleep()) #
    # t1 = loop.create_task(async_sleep()) # можна створюват таски і на loop. Правда, перший раз не запустився (не видав 1), але потім все ніби ок.
    # await t
    # await t1
# asyncio.run(main())
