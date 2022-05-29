import asyncio
import aiohttp
import aiofile
from timer import timer
from urls import urls


async def getJson(url, filename):
    async with aiohttp.ClientSession() as session:
        print("Getting html from:", url)
        async with session.get(url) as response:
            html = await response.text()

    async with aiofile.async_open(filename, "w+") as afp:
        print("Writing html to file:", filename)
        await afp.write(html)


async def getAll():
    tasks = []
    for i, url in enumerate(urls):
        tasks.append(asyncio.create_task(getJson(url, f"{i+1}.html")))
    await asyncio.wait(tasks)


@timer
def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getAll())


if __name__ == '__main__':
    main()
