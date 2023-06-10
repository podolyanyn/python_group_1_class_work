import aiohttp
import asyncio
import time
import multiprocessing


async def fetch_currency(session, url):
    async with session.get(url) as response:
        return await response.text()


async def usd():
    url_usd = 'https://bank.gov.ua/NBU_Exchange/exchange_site?start=20230605&end=20230605&valcode=usd&sort' \
              '=exchangedate&order=desc&json'
    async with aiohttp.ClientSession() as session:
        response = await fetch_currency(session, url_usd)
        print(response)


async def eur():
    url_eur = 'https://bank.gov.ua/NBU_Exchange/exchange_site?start=20230605&end=20230605&valcode=eur&sort' \
              '=exchangedate&order=desc&json'
    async with aiohttp.ClientSession() as session:
        response = await fetch_currency(session, url_eur)
        print(response)


async def gbr():
    url_gbr = 'https://bank.gov.ua/NBU_Exchange/exchange_site?start=20230605&end=20230605&valcode=gbp&sort' \
              '=exchangedate&order=desc&json'
    async with aiohttp.ClientSession() as session:
        response = await fetch_currency(session, url_gbr)
        print(response)


async def main():
    start = time.time()
    # await usd()
    # await eur()
    # await gbr()
    await asyncio.gather(usd(), eur(), gbr())

    finish = time.time() - start
    print(finish)


if __name__ == '__main__':
    asyncio.run(main())


async def fibonacci(n):
    if n <= 0:
        return []

    fibonacci_sequence = [0, 1]

    if n <= 2:
        return fibonacci_sequence[:n]

    async def calculate_fibonacci():
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
            fibonacci_sequence.append(b)

    await asyncio.gather(calculate_fibonacci())

    return fibonacci_sequence


async def main():
    start = time.time()
    n = 10
    sequence = await fibonacci(n)
    print(f"{sequence}")
    end = time.time()
    finish = end - start
    print(f" time: {finish}")


if __name__ == '__main__':
    asyncio.run(main())


def fibonacci(n):
    if n <= 0:
        return []

    fibonacci_sequence = [0, 1]

    if n <= 2:
        return fibonacci_sequence[:n]

    with multiprocessing.Pool() as pool:
        results = pool.map(_calculate_fibonacci, range(n - 2))

    fibonacci_sequence.extend(results)

    return fibonacci_sequence


def _calculate_fibonacci(i):
    a, b = 0, 1
    for _ in range(i):
        a, b = b, a + b
    return b


if __name__ == '__main__':
    start = time.time()
    n = 10
    sequence = fibonacci(n)
    print(f"Fibonacci sequence up to {n}: {sequence}")
    end = time.time()
    fin = end - start
    print(f'time: {fin}')
